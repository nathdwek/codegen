class CodeMap(object):
    def __init__(self):
        self._map = {}

    def meanLength(self):
        meanLength = 0
        for symbol in self._map:
            meanLength += symbol.proba()*len(self._map[symbol])
        return meanLength

    def mapSymbol(self, symbol, code):
        self._map[symbol] = code

    def __iter__(self):
        return self._map.__iter__()

    def codeOf(self, symbol):
        return self._map[symbol]
