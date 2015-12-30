class CodeMap(object):
    def __init__(self, name):
        self._map = {}
        self._name = name

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
        return self._map.get(symbol, '')

    def kraft(self):
        res = 0
        for symbol in self._map:
            res += 2**-len(self.codeOf(symbol))
        return res

    def name(self):
        return self._name

    def algo(self):
        return self._name
