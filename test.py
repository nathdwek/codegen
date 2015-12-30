from symbol import Symbol
from source import Source
from algos import weaver, fanno, huffman, block
from benchmark import benchmark

a = Symbol('A', 2**-5)
b = Symbol('b', 2**-5)
c = Symbol('c', 2**-5)
d = Symbol('d', 2**-5)
e = Symbol('e', 2**-4)
f = Symbol('f', 2**-4)

g = Symbol('g', 2**-2)
h = Symbol('h', 2**-1)
i = Symbol('i', 0.05)

j = Symbol('j', 0.5)
k = Symbol('k', 0.25)
l = Symbol('l', 0.125)
m = Symbol('m', 0.125)

s = Source(d, b, f, a, e, c, g, h)
c = block(s)


for sym in s.sorted():
    print(sym.name(), ' ', c.codeOf(sym))

benchmark(s, c)
