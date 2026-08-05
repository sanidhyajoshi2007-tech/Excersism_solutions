def convert(number):
    line=""
    if number % 3==0:
        line+="Pling"
    if number %5==0:
        line+="Plang"
    if number %7==0:
        line+="Plong"
    if number % 3!=0 and number %5!=0 and number %7!=0:
        return str(number)
    return line
