def square(number):
    if 0 < number <= 64:
        return 2**(number - 1)
    else:
        raise ValueError("Square must be between 1 and 64")
        
def total():
    grains = 0
    for square in range(64):
        grains += 2**square
    return grains
