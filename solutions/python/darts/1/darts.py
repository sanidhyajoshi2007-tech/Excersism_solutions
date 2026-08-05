def score(x, y):
    import math
    if math.sqrt(x**2+y**2)>10:
        return 0
    if math.sqrt(x**2+y**2)>5:
        return 1
    if math.sqrt(x**2+y**2)>1:
        return 5
    else:
        return 10
