# Example: Approximate PI using the relative areas of a circle inside
# a square
#   o Uses simple arithmetic
#   o Generate random points in [-1,1]x[-1,1]
#   o Hits are inside circle, i.e. x2+y2⩽1
#   o Tries are total number of tries
#   o Ratio is 4 x Hits / Tries
#       • N.B. 4 is the area of the square
from random import random

TRIES = 10000

hits = 0
for i in range(TRIES):
    r = random()
    x = -1 + 2 * r
    r = random()
    y = -1 + 2 * r

    if x * x + y * y <= 1:
        hits += 1

piEstimate = 4.0 * hits / TRIES
print('Estimate for pi:', piEstimate)
