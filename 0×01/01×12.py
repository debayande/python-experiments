#!/usr/bin/env python

x = y = [503, 509, 521]

print(x, y)
print(hex(id(x)), hex(id(y)))

y = [181, 191, 193]
print(x, y)
print(hex(id(x)), hex(id(y)))
