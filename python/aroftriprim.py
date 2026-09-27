def area():
    b = 5
    h = 10
    area = 11 * b * h
    return area

num = area()

if num <= 1:
        print("It is not a prime number")
elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print("It is not a prime number")
                break
else:
            print("It is a prime number")   