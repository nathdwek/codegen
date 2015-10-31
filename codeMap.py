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
        res = ''
        if symbol in self._map:
            res = self._map[symbol]
        return res

    def kraft(self):
        res = 0
        for symbol in self._map:
            res += 2**-len(self.codeOf(symbol))
        return res
