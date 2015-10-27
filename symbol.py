class Symbol(object):

    def __init__(self, name, proba):
        self._name = name
        self._proba = proba

    def proba(self):
        return self._proba

    def name(self):
        return self._name
