def is_armstrong_number(number):
    line=str(number)
    sum=0
    for i in line:
        sum+=int(i)**len(line)
    if sum==number:
        return True
    return False
  
    

