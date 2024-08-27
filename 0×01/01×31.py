#!/usr/bin/env python

# This should blow up; `bytes` can only contain ASCII literal characters.
v = (
  b"We anticipated it, as you people are such clichés and the fact that "
  b"you're a rat for the Feds is also tolerable, Little John. What we will "
  b"not tolerate is getting nothing for our money. No information, no "
  b"protection, no assurances. You understand, Little Johnny?"
)

print(v)
