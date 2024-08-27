#!/usr/bin/env python

def f(n, x):
  n.append(x)

j = [2, 3]
f(j, 5)
print(j == [2, 3])

k = (2, 3)
f(k, 5)
print(k == (2, 3))
