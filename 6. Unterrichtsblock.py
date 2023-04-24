def meinefunktion(n):
  return abs(n - 50)

meinezahlen = [100, 50, 65, 82, 23]
meinezahlen.sort(key = meinefunktion)
print(meinezahlen)