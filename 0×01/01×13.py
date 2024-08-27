#!/usr/bin/env python

x = y = [577, 587, 593]
print(x, y)
print(hex(id(x)), hex(id(y)))
x[1] = 599
print(x, y)
print(hex(id(x)), hex(id(y)))
