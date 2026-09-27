import math
print(math.sqrt(25))
# the above is same as below
import math as m
print(m.sqrt(25))
# we can import all functions of math , but if we want only some functions we can do it as
from math import sqrt,pow        # as we are specified functions above we dont want to mention as math.sqrt etc
print(pow(4,5))
print(sqrt(25))