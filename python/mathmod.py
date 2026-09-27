# import math
# y=math.sqrt(112)
# print(y)
# m=math.ceil(2.3)
# print(m)
# n=math.floor(6.7)
# p=math.pi
# print(p)



# home work

z=pow(7,3)+pow(9,3)
print(z)
    
num=z
temp=num
rev=0
while num>0:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
if temp==rev:
    print("the number is palindrome",rev)
else:
     print("the number is not a palindrome")
num2=rev
rev2=0
while num2>0:
    rem2=num2%10
    rev2=rev2+rem2
    num2=num2//10
print(rev2)
num3=rev2
sum=0
for i in range(1,num3):
    if(num3%i==0):
        sum=sum+i
if(num3==sum):
    print(num3,"it is a perfect number")
else:
    print(num3,"it is not a perfect number")
 
           


    



