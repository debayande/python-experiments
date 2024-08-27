#!/usr/bin/env python

from collections import defaultdict

capitals = defaultdict(lambda: "not set")

capitals["Arkansas"]   = "Little Rock"
capitals["California"] = "Sacramento"
capitals["Colorado"]   = "Denver"
capitals["Georgia"]    = "Atlanta"

print(capitals)
print(capitals["California"])
print(capitals["Massachusetts"])
