# single level inheritance

# class father:
#     def disp(self):
#         print("i have a car")
# class son(father):  # by calling father inside son it inherits all properties present inside the father
#     #disp(self)
#     def cool(self):
#         print("i have a bike")
        

# s1=son()
# s1.disp()
# s1.cool()


# multi level inheritance

# class grandfather:
#     def tester(self):
#         print("i have a home")
# class father(grandfather):
#     def disp(self):
#         print("i have a car")
# class son(father):  # by calling father inside son it inherits all properties present inside the father
#     #disp(self)
#     def cool(self):
#         print("i have a bike")
        

# s1=son()
# s1.disp()
# s1.cool()
# s1.tester()

# hierarchial inheritance
# class father():
#     def disp1(self):
#         print("car")
# class son(father):
#     def disp2(self):
#         print("i have bike")
# class daughter(father):
#     def disp3(self):
#         print("i have scooty")
# s1=son()
# s1.disp2()
# s1.disp1()
# d1=daughter()
# d1.disp3()
# d1.disp1()


# multiple inheritance
# class father:
#     def disp1(self):
#         print("100")
# class mom:
#     def disp2(self):
#         print("500")
# class son(father,mom):
#     def disp3(self):
#         print("money")

# s1=son()
# s1.disp2()

# hybrid inheritance
# class sample:
#     def disp1(self):
#         print("1")
# class demo(sample):
#     def disp2(self):
#         print("2")
# class dingi(sample):
#     def disp3(self):
#         print("4")
# class tester(demo):
#     def disp4(self):
#         print("3")
# s1=tester()
# s1.disp1()

        


