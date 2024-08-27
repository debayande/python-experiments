#!/usr/bin/env python

x    = (1, 2, 3)
y    = ("a", 1, "Zig", (2, 3))
y[2] = "Python" # This should blow up; tuples are immutable.

print(y)
