age=int(input("enter your age\n"))
id=input("enter the id\n")
if(age>=18):
    print("your age matches")
   
    if(id=="voter id"):
      
        print("you can vote")
    else:
        print("you cannot vote")
else:
    print("this is not right age to vote")