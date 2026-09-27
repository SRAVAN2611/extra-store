# import customer1
# import customer2
# customer1.details("sravan")
# customer1.details("abhiram")
# customer2.phone(1234)
nterm=int(input("How many times\n"))
n1,n2=0,1
count=0

if(nterm<1):
    print("please enter positive number")
elif(nterm==1):
    print("Fibonacci sequence upto nterms",nterm)
else:
    print("Fibonacci sequence")
    while(count<nterm):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1