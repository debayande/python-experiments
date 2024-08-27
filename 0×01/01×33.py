#!/usr/bin/env python

v = []
w = [2, 3, 5, 7]
x = [2, "Three", 5.0, None]
y = ["Nikolai Itchenko", "Teddy Rensen"]
z = [["Nikolai Itchenko", "Teddy KGB", "Viggo Tarasov"], [11, 13, 17, 19]]

print(x[2])
print(y[0])
print(z[0][1])
print(w[-4], x[-1])

y[1] = "Yorgi"
y.sort()
print(y)

y.append("Jarda")
y.sort()
print(y)

z[0].insert(1, "Ivan Simanov")
z[0].sort()
print(z)

# Can a list inside a tuple be mutated?
a = (["Sergei Petrovsky", "Valentin Dimitrovich Zukovsky"], 3.141592654)
a[0].append("Vladimir Pushkin")
print(a)

a[0].remove("Sergei Petrovsky")
print(a)

print(a[0].index("Valentin Dimitrovich Zukovsky"))
print(len(a[0]))

f = [0, 1, 1, 2, 3, 5, 8]
print(f.count(1))
print(f.reverse())
print(f[::-1]) # Performs the same action as f.reverse().
print(f.pop())

for name in z[0]:
  print(name)
