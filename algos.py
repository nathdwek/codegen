from codeMap import CodeMap


def weaver(source):
    source.check()
    code = ''
    codeMap = CodeMap()
    for symbol in source.sorted()[:-1]:
        codeMap.mapSymbol(symbol, code+'0')
        code += '1'
    codeMap.mapSymbol(source.sorted()[-1], code)
    return codeMap


def fanno(source):
    source.check()
    codeMap = CodeMap()
    _fanno(source.sorted(), '', codeMap)
    return codeMap


def _fanno(symbols, prefix, codeMap):
    if len(symbols) == 1:
        codeMap.mapSymbol(symbols[0], prefix)
    else:
        medianIndex = _medianIndex(symbols)
        _fanno(symbols[:medianIndex], prefix + '0', codeMap)
        _fanno(symbols[medianIndex:], prefix + '1', codeMap)


def _medianIndex(sortedSymbols):
    index = 0
    leftTotal = 0
    rightTotal = 0
    for symbol in sortedSymbols:
        rightTotal += symbol.proba()
    diff = rightTotal - leftTotal
    newDiff = 1
    while newDiff > 0:
        leftTotal += sortedSymbols[index].proba()
        rightTotal -= sortedSymbols[index].proba()
        diff = newDiff
        newDiff = rightTotal - leftTotal
        index += 1
    if -newDiff > diff:
        index -= 1
    return index


def huffman(source):
    source.check()
    codeMap = CodeMap()
    return _huffman(source.sorted(), codeMap)


def _huffman(sortedSymbols, codeMap):
    pair = _miniPair(sortedSymbols)
    for symbol in pair[0]:   # todo need sometg flat here
        codeMap.mapSymbol(symbol.codeOf(symbol)+'0')
    for symbol in pair[1]:
        codeMap.mapSymbol(symbol.codeOf(symbol)+'1')
    if len(sortedSymbols) <= 2:
        return codeMap
    else:
        return _huffman(sortedSymbols, codeMap)


def _miniPair(aggregatedSymbols):
    minimum = 100  # Sum of probas always == 1
    pair = ()
    pairIndexes = ()
    for i in range(len(aggregatedSymbols)):
        for j in range(i+1, len(aggregatedSymbols)):
            testValue = _flatSum(aggregatedSymbols[i]) + _flatSum(aggregatedSymbols[j])
            if testValue < minimum:
                pair = [aggregatedSymbols[i], aggregatedSymbols[j]]
                pairIndexes = (i, j)
                minimum = testValue
    del aggregatedSymbols[max(pairIndexes)]
    del aggregatedSymbols[min(pairIndexes)]
    aggregatedSymbols.append(pair)
    return pair


def _flatSum(aggregatedSymbols):
    res = 0
    if type(aggregatedSymbols) == list:
        for elem in aggregatedSymbols:
            res += _flatSum(elem)
    else:
        res = aggregatedSymbols
    return res
