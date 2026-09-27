opt=input("enter the option (+,-,*,/)\n")
if(opt=='+'):
    print("it is a addition")
elif(opt=='-'):
    print("it is subs")
elif(opt=='*'):
    print("it is mult")
elif(opt=='/'):
    print("it is div")
n1=int(input("enter n1\n")) # Correcting the input value for n1 in the given code block.
n2=int(input("enter n2\n"))
match(opt):
    case '+':
        res=n1+n2
        print("add of 2 no's is ",res)
    case '-':
        res=n1-n2
        print("sub of 2 no's is ",res)
    case '*':
        res=n1*n2
        print("mult of 2 no's is ",res)
    case '/':
        res=n1/n2
        print("div of 2 no's is ",res)
    case _:
        print("invalid input")

