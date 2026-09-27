num=int(input("enter a number"))
sum_of_digits=0
while num>0:
    digit=num%10
    sum_of_digits=sum_of_digits+digit
    num=num//10
print("the sum of digits in a number is",sum_of_digits)
    