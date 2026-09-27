num=5
print(id(num))
name='navin'
print(id(name))
a=10
b=a
print(id(a))
print(id(b))
# if 2 different variable have same value/data then their id is same
print(id(10))
# adress(id) does not depend on variable name it depends on the value

a=9
print(id(a))
print(id(b))
# here id of a is changed as 'a' value is updated but 'b' has its old value

# if we assign 'b' value as 8 then value of 10 is stored in memory which is unused so id of 10 is known as garbage value i.e., it is garbage collected value 

# output
# 135390682037288
# 135390669744688
# 135390682037448
# 135390682037448
# 135390682037448
# 135390682037416
# 135390682037448
