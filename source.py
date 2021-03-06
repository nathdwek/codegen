from math import log2 as bb
from decimal import Decimal as d


class Source(object):
    def __init__(self, *symbols):
        self._symbols = []
        self._entropy = d(0)
        for symbol in symbols:
            self.addSymbol(symbol)

    def addSymbol(self, symbol):
        self._symbols.append(symbol)
        self._entropy -= symbol.proba()*d(bb(symbol.proba()))

    def names(self):
        return list(map(lambda sym: sym.name(), self._symbols))

    def entropy(self):
        return self._entropy

    def check(self):
        tot = d(0)
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
