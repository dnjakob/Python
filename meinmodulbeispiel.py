import math
from datetime import datetime as dt
import gruss as g
import auto as car
from meinmodul import person1 as RS6
from objektmodul import *

print(RS6['stadt'])

P = Person("Daniel", 24)
P.vorstellen()

a = math.radians(45)
print(a)

b = math.sqrt(64)
print(b)

c = dt.now()
print(c)

g.sage_hallo()

car1 = car.auto
car1.hupe()