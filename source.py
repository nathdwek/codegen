from math import log2 as bb


class Source(object):
    def __init__(self, *symbols):
        self._symbols = []
        self._entropy = 0
        for symbol in symbols:
            self.addSymbol(symbol)

    def addSymbol(self, symbol):
        self._symbols.append(symbol)
        self._entropy -= symbol.proba()*bb(symbol.proba())

    def entropy(self):
        return self._entropy

    def check(self):
        tot = 0
        for symbol in self._symbols:
            tot += symbol.proba()
        if tot != 1:
            raise NameError('Total des probas différent de 1, tocard!')

    def sorted(self):
        return sorted(self._symbols, key=lambda s: s.proba(), reverse=True)

    def __iter__(self):
        return self._symbols.__iter__()

    def __len__(self):
        return len(self._symbols)
