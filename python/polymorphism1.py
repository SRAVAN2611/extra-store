class dingi:
    def beh(self):
        print("some behaviour")
class temple(dingi):
    def beh(self):
        print("devotee behaviour")
class spa(dingi):
    def beh(self):
        print("customer behaviour")
class college(dingi):
    def beh(self):
        print("student behaviour")
def dinga(d1):
    d1.beh()
# main function
t1=temple()
s1=spa()
c1=college()
dinga(t1)
dinga(s1)
dinga(c1)

# 1)
# class Bike:
#     def beh(self):
#         print("some behaviour")

# class Sound(Bike):
#     def beh(self):
#         print("devotee behaviour")

# class Pulsar(Bike):
#     def beh(self):
#         print("customer behaviour")

# class BMW(Bike):
#     def beh(self):
#         print("student behaviour")

# def veh_sound(v1):
#     v1.beh()

# # main function
# s1 = Sound()
# p1 = Pulsar()
# b1 = BMW()

# veh_sound(s1)
# veh_sound(p1)
# veh_sound(b1)

# 4)                                                                                                                                         

class bookmyshow:
    def beh(self):
        print("movie")
class bollywood(bookmyshow):
    def beh(self):
        print("B")
class sandalwood(bookmyshow):
    def beh(self):
        print("S")
class hollywood(bookmyshow):
    def beh(self):
        print("H")
def booking(d1):
    d1.beh()
# main function
t1=bollywood()
s1=sandalwood()
c1=hollywood()
dinga(t1)
dinga(s1)
dinga(c1)

        