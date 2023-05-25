import math

def meinefunktion(n):
  return lambda a : a * n

verdoppler = meinefunktion(2)
verdreifacher = meinefunktion(3)

print(verdoppler(11),"\n")

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y,"\n")

z = abs(-7.25)

print(z, "\n")

w = pow(4, 3)

print(w,"\n")

d = 5

print(math.isfinite(d),"\n")

g = 30.22233332335343

print(math.frexp(g),"\n")

o = 16
p = 8

print(math.gcd(o, p))

wert1 = input("Wert 1 eingeben: ")
wert2 = input("Wert 2 eingeben: ")
wert3 = int(wert1) + int(wert2)
print(wert3)