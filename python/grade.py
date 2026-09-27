def student_marks(m):
    if(m>75 and m<=100):
        return 'A'
    elif(m>60 and m<=75):
        return 'B'
    elif(m>50 and m<=59):
        return 'C'
    elif(m>40 and m<=49):
        return 'D'
    elif(m>36 and m<=40):
        return 'E'
    elif(m<35):
        return 'F'
    else:
        print("Invalid marks")
mark=int(input("enter the marks\n"))
grade=student_marks(mark)
print("the student grade is ",grade)
    



    
    

    
    