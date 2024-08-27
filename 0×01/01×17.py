#!/usr/bin/env python

import random
import sys

a, b = random.randint(0, sys.maxsize), random.randint(0, sys.maxsize)

print(f"› a = {a}, b = {b}")

if a > b:
  print(f"› {a}")
else:
  print(f"› {b}")
