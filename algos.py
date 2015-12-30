from codeMap import CodeMap
from math import ceil, log2 as bb


def weaver(source):
    source.check()
    code = ''
    codeMap = CodeMap('Shannon-Weaver')
    for symbol in source.sorted()[:-1]:
        codeMap.mapSymbol(symbol, code+'0')
        code += '1'
    codeMap.mapSymbol(source.sorted()[-1], code)
    return codeMap


def fanno(source):
    source.check()
    codeMap = CodeMap('Shannon-Fanno')
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
    codeMap = CodeMap('Huffman')
    return _huffman(source.sorted(), codeMap)


def _huffman(sortedSymbols, codeMap):
    pair = _miniPair(sortedSymbols)
    for symbol in _flatten(pair[0]):
        codeMap.mapSymbol(symbol, codeMap.codeOf(symbol)+'0')
    for symbol in _flatten(pair[1]):
        codeMap.mapSymbol(symbol, codeMap.codeOf(symbol)+'1')
    if len(sortedSymbols) < 2:
        return codeMap
    else:
        return _huffman(sortedSymbols, codeMap)


def _miniPair(aggregatedSymbols):
    minimum = 2  # Sum of probas always == 1 => init minimum too high
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
        res = aggregatedSymbols.proba()
    return res


def _flatten(ls):
    res = []
    if type(ls) == list:
        for elem in ls:
            res += _flatten(elem)
    else:
        res = [ls]
    return res


def block(source):
    source.check()
    codeMap = CodeMap('Blockcode')
    count = 0
    blockLength = ceil(bb(len(source)))
    for symbol in source.sorted():
        codeMap.mapSymbol(symbol, _paddedBinary(count, blockLength))
        count += 1
    return codeMap


def _paddedBinary(number, length):
    res = bin(number)[2:]
    if len(res) < length:
        res = '0' * (length-len(res)) + res
    return res
