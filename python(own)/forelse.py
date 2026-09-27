nums = [12, 16, 18, 20, 25]
for num in nums:
    if num % 5 == 0:
        print(num)
 
#gives only 1st num which is divisible by 5 as we are using break 
nums = [12, 16, 18, 20, 25]
for num in nums:
    if num % 5 == 0:
        print(num)
        break
else:       #else here gives runs when no num is divisible by 5
    print("not found")  #if else part is written inside for along with if then we get not found 5 times
