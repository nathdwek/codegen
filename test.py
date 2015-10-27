from symbol import Symbol
from source import Source
from algos import weaver, fanno
from benchmark import benchmark

a = Symbol('A', 0.3)
b = Symbol('b', 0.25)
c = Symbol('c', 0.2)
d = Symbol('d', 0.1)
e = Symbol('e', 0.1)
f = Symbol('f', 0.05)

g = Symbol('g', 0.8)
h = Symbol('h', 0.15)
i = Symbol('i', 0.05)

j = Symbol('j', 0.5)
k = Symbol('k', 0.25)
l = Symbol('l', 0.125)
m = Symbol('m', 0.125)

s = Source(d, b, f, a, e, c)
s = Source(h, g, i)
s = Source(j, k, l, m)
c = weaver(s)
c2 = fanno(s)


for sym in s.sorted():
    print(sym.name(), ' ', c.codeOf(sym), ' ', c2.codeOf(sym))
benchmark(s, c)
benchmark(s, c2)
