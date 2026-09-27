# patterns:-

# rows=4
# for i in range(rows):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


# rows=4
# for i in range(rows):
#     for j in range(i+1):
#         print(i+1,end=" ")
#     print()


# rows=4
# for i in range(rows):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()


# rows=4
# num=1
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num=num+1
#     print()

# execute each block to get different type of pattern


# reverse star pattern

rows=4
for i in range(rows,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()
