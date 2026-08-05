def is_valid(isbn):
    num=10
    sum=0
    count=0
    for i in isbn:
        if i.isdigit():
            sum+=int(i)*num
            num-=1
            count+=1
        if i.isalpha():
            num-=1
    if isbn.endswith("X"):
         sum+=10*1
         count+=1
    if sum%11==0and sum!=0and count==10:
        return True
    return False
            
