# def cube(x, y):
#     z = pow(x, 3) + pow(y, 3)
#     return z

# num = cube(7, 9)
# temp = num
# rev = 0
# while num > 0:
#     rem = num % 10
#     rev = (rev * 10) + rem
#     num = num // 10

# if temp == rev:
#     print("The number is a palindrome:", rev)
# else:
#     print("The number is not a palindrome")

# num2 = temp
# rev2 = 0
# while num2 > 0:
#     rem2 = num2 % 10
#     rev2 = (rev2 * 10) + rem2
#     num2 = num2 // 10

# print(rev2)

# num3 = rev2
# sumofdigits = 0
# while num3 > 0:
#     digit = num3 % 10
#     sumofdigits = sumofdigits + digit
#     num3 = num3 // 10

# num4 = sumofdigits
# sum3 = 0
# for i in range(1, num4):
#     if num4 % i == 0:
#         sum3 = sum3 + i

# if num4 == sum3:
#     print(num4, "is a perfect number")
# else:
#     print(num4, "is not a perfect number")



# num3=rev2
# sumofdigits=0
# while num3>0:
#     digit=num%10
#     sumofdigits=sumofdigits+digit
#     num3=num3//10
# sumofdigits=num4
# sum3=0
# for i in range(1,num4):
#     if(num%i==0):
#         sum=sum+i
#         if(num4==sum3):
#             print(num4,"is a perfect number")
#         else:
#             print(num4,"not a perfect number")
            