def score(x, y):
    distance = ((x**2) + (y**2)) ** 0.5
    if distance > 10:
        return 0
    elif 5 < distance <= 10:
        return 1
    elif 1 < distance <= 5:
        return 5
    elif  0 <= distance <= 1:
        return 10
