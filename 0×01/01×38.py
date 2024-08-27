#!/usr/bin/env python

s = input("<-- ")
try:
    s = float(s)
    print(f"--> {s / 2}")
except ValueError:
    print(f"--> {s}")
