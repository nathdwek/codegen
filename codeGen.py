from symbol import Symbol
from source import Source
from algos import weaver, fanno, huffman, block
from benchmark import benchmark
from string import ascii_uppercase as alphabet


def _sourceFromInput():
    source = Source()
    i = 0
    stop = False
    autoProba = _createAutoProba(source)
    autoName = _createAutoName(i, source)
    while not stop:
        name = getNameFromUser(autoName)
        proba = getProbaFromUser(autoProba)
        source.addSymbol(Symbol(name, proba))
        i += 1
        autoProba = _createAutoProba(source)
        autoName = _createAutoName(i, source)
        stop = autoProba == 0
    return source


def getNameFromUser(autoName):
    name = _sanitizeName(input('Enter next symbol name [{}]: '
                               .format(autoName)),
                         autoName)
    return name


def getProbaFromUser(autoProba):
    proba = _sanitizeProba(input('Enter next symbol proba [{}]: '
                                 .format(autoProba)),
                           autoProba)
    while proba == -1:
        proba = _sanitizeProba(input('Enter next symbol proba [{}]: '
                                     .format(autoProba)),
                               autoProba)
    return proba


def _sanitizeName(name, autoName):
    name = name.strip()
    if name == '':
        name = autoName
    return name


def _sanitizeProba(probaString, autoProba):
    probaString = probaString.strip()
    try:
        proba = eval(probaString)
        if proba < 0 or proba > autoProba:
            proba = -1
    except:
        if probaString == '':
            proba = autoProba
        else:
            proba = -1
    return proba


def _createAutoProba(source):
    total = 0
    for sym in source:
        total += sym.proba()
    return 1 - total


def _createAutoName(count, source):
    autoName = alphabet[count]
    while autoName in source.names():
        count += 1
        autoName = alphabet[count]
    return autoName


def _present(source, codeMap):
    print('\n--{}--\n'.format(codeMap.algo()))
    pad = max(map(lambda name: len(name), source.names()))
    for sym in source.sorted():
        print(sym.name(),
              ' '*(pad - len(sym.name())) + ': ',
              codeMap.codeOf(sym))
    benchmark(source, codeMap)

if __name__ == "__main__":
    source = _sourceFromInput()
    b = block(source)
    w = weaver(source)
    f = fanno(source)
    h = huffman(source)
    for codeMap in (b, w, f, h):
        _present(source, codeMap)
