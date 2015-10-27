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
