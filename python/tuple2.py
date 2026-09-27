fruits=('banana','apple','mango','grapes')
x=list(fruits)
print(x)

x.append('pine apple')
print(x)

x.insert(2,'orange')
print(x)

x.remove('apple')
print(x)

x.pop(1)
print(x)

del x[2]
print(x)

fruits=tuple(x)
print(fruits)
