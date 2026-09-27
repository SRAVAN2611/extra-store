def ishappynumber(num):
    sum=0
    while(num>0):
        rem=num%10
        sum=sum+(rem*rem)
        num=num//10
    return sum
num=32
result=num
while(result !=1 and result !=4):
    result=ishappynumber(result)
if(result==1):
    print(num,"it is a happy number")
elif(result==4):
    print(num,"it is not a happy number")