#!/usr/bin/env python

capitals = {
  "England": "London",
  "Northern Ireland": "Belfast",
  "Scotland": "Edinburgh",
  "Wales": "Cardiff",
}

print(capitals["England"])
print(capitals.keys())
print(capitals.values())

for country in capitals.keys():
  print(f"{capitals[country]} is the capital of {country}.")
