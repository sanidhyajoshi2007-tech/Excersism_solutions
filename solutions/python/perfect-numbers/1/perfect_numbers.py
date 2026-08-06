def classify(number):
    if number<1:
        raise ValueError("Classification is only possible for positive integers.")

    divisors=[]
    sum=0
    for i in range(1,number):
        if number%i==0:
            divisors.append(i)
    for i in divisors:
        sum+=i
    if number == sum:
        return "perfect"
    if number<sum:
        return "abundant"
    if number > sum:
        return "deficient"


    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

