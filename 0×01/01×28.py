#!/usr/bin/env python

x = "123"
y = int(x)

x = "123.456"
y = float(x)
y = int(x) # This should blow up!
y = int(y)
