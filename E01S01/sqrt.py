import math
tolerance = 1.0e-16
lower = 0.0
upper = 2.0
uncertanly = upper - lower
while uncertanly > tolerance:
    middle = (lower + upper) / 2
    if middle ** 2 < 2.0:
        lower = middle
    else:
        upper = middle
    print(lower, upper)
    uncertanly = upper - lower
print(math.sqrt(2))