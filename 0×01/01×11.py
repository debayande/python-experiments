#!/usr/bin/env python

x = y = z = 42

print(x, y, z)
print(hex(id(x)), hex(id(y)), hex(id(z)))

y = 84
print(x, y, z)
print(hex(id(x)), hex(id(y)), hex(id(z)))
