# break
av=5
x=int(input("how many candies you want?"))
i=1
while i<=x:
    if i>av:
        print("out of stock")
        break
    print("candy")
    i+=1
print("bye")

# continue
for i in range(1,101):
    if i%3==0 and i%5==0:
        continue
    print(i)
    
# pass
for i in range(1,101):
    if(i%2!=0):
        pass
    else:
        print(i)
        