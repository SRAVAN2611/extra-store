# y=10
# x=9
# z=x+y
# # here _ is used for previous operation i.e., z here (this is used in terminal but in few places other than terminal it may or may not work) 
# print(_+y)

# variables can also be used for concatenation of 2 strings
# name="youtube"
# print(name+"rocks")
# print(name+"5")

# srings in python are immutable
#  name="youtube"
#  name[0:3]='r'
#  print(name)
 
# but we change like this :-
# name="youtube"
# x='my'+name[3:]
# print(x)

result=eval(input("enter a expression: "))
print(result)
