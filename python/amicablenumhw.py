# l1 = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "jackfruit", "kiwi", "lemon", "mango", "nectarine"]
# l2 = [12, 34, 56, 78, 90, 123, 456, 789, 1023, 2048, 4096, 8192, 16384, 32768, 65536, 131072]
# a=len(l1)
# b=len(l2)
# print(a,b)
# c=pow(a,3)
# d=pow(b,3)
# print(c,d)
# num1=c
# rev1=0
# while num1>0:
#     rem1=num1%10
#     rev1=(rev1*10)+rem1
#     num1=num1//10
# print("the reverse number is",rev1)
# num2=d
# rev2=0
# while num2>0:
#     rem2=num2%10
#     rev2=(rev2*10)+rem2
#     num2=num2//10
# print("the reverse number is",rev2)


# x=rev1
# y=rev2
# sum1=0
# sum2=0
# for i in range(1,x):
#     if(x%i==0):
#         sum1=sum1+i
# for j in range(1,y):
#     if(y%j==0):
#         sum2=sum2+j
# if(sum1==y and sum2==x):
#     print("it is a amicable number")
# else:
#     print("it is not a amicable number")




# amicable,sum,palidrome

a=int(input("enter a integer "))
b=int(input("enter b integer "))
sum1=0
sum2=0
for i in range(1,a):
    if(a%i==0):
        sum1=sum1+i
for j in range(1,b):
    if(b%j==0):
        sum2=sum2+j
if(sum1==b and sum2==a):
    print("it is a amicable number")
else:
    print("it is not a amicable number")
    
c=a+b

temp=c
rev=0
while c>0:
    rem=c%10
    rev=(rev*10)+rem
    c=c//10
if temp==rev:
    print("the number is palindrome",rev)
else:
    print("it is not a palindrome")
