def square(number):
    if number not in range(1,65):
             raise ValueError("square must be between 1 and 64")
    if number==1:
        return 1
    return 2*square(number-1)


def total():
    sum=0
    for i in range(1,65):
        sum+= square(i)
    return sum
