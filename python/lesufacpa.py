l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',1,2,3,4,5,6,7,8]
m=len(l)
print(m)

sum=0
while m>0:
    digit=m%10
    sum=sum+digit
    m=m//10
print("the sum of digits in a number is",sum)

fact=1
while sum>0:
    fact=fact*sum
    sum=sum-1
print("factorial of given number",fact)

temp=fact
rev=0
while fact>0:
    rem=fact%10
    rev=(rev*10)+rem
    fact=fact//10
if temp==rev:
    print("the number is palindrome",rev)
else:
    print("it is not a palindrome")
    