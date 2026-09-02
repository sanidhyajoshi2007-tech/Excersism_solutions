def square_of_sum(number):
    sum=0
    for num in range(number):
        sum+=num+1
    return sum**2
        
def sum_of_squares(number):
    sum=0
    for num in range(number):
        sum+=(num+1)**2
    return sum

def difference_of_squares(number):
    diff=square_of_sum(number)-sum_of_squares(number)
    return diff
