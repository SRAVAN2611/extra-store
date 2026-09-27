# num=6
# flag=False

# if num==1:
#     print(num,"it is not a prime number")
# elif num>1:
#     for i in range(2,num):
#         if(num%i==0):
#             flag=True
#             break
# if flag:
#     print(num,"it is not a prime number")
# else:
#     print(num,"it is a prime number")


def is_prime(num):
    if num <= 1:
        print("It is not a prime number")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print("It is not a prime number")
                break
        else:
            print("It is a prime number")   

num = int(input("Enter a number: "))
is_prime(num)
