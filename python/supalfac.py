num=986959
sum=0
while num>0:
    rem=num%10
    sum=sum+rem
    num=num//10
    
print("the sum of given number is = ",sum)
temp=sum
copy=temp
rev=0
while temp>0:
    r=temp%10    
    rev=(rev*10)+r
    temp=temp//10
if(copy==rev):
    print("it is a palindrome")
else:
    print("it is not a palindrome")
copy2=rev
sum1=0
while copy2>0:
    re=copy2%10
    sum1=sum1+re
    copy2=copy2//10
print("the sum of reverse number is = ",sum1)
fact=1
while sum1>0:
    fact=fact*sum1
    sum1=sum1-1
print("factorial of given number",fact)
    