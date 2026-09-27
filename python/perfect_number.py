num=int(input("enter a num "))
sum=0
for i in range(1,num):
    if(num%i==0):
        sum=sum+i
if(num==sum):
    print(num,"it is a perfect number")
else:
    print(num,"it is not a perfect number")