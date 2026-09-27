x=int(input("enter x integer "))
y=int(input("enter y integer "))
sum1=0
sum2=0
for i in range(1,x):
    if(x%i==0):
        sum1=sum1+i
for j in range(1,y):
    if(y%j==0):
        sum2=sum2+j
if(sum1==y and sum2==x):
    print("it is a amicable number")
else:
    print("it is not a amicable number")
    