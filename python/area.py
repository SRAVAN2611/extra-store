#area of triangle
def arotri():
    base_of_triangle=int(input("enter the base of triangle: "))
    height_of_triangle=int(input("enter the height of triangle: "))
    arotri=1/2*base_of_triangle*height_of_triangle
    print(arotri)
arotri()

#area of rectangle
def arorec():
    length_of_rectangle=int(input("enter the length of rec: "))
    breadth_of_rectangle=int(input("enter the breadth of rec: "))
    arorec=length_of_rectangle*breadth_of_rectangle
    print(arorec)
arorec()

#area of square
def arosq():
    side_of_square=int(input("enter of square: "))
    arosq= side_of_square**2
    print(arosq)
arosq()

#area of parellogram
def aropg():
    base_of_par=int(input("enter the base of par: "))
    height_of_par=int(input("enter the height of par: "))
    aropg= base_of_par*height_of_par
    print(aropg)
aropg()

#area of trapezoid
def arot():
    a_of_tr=int(input("enter the a_of_tr: "))
    b_of_tr=int(input("enter the b_of_tr: "))
    h_of_tr=int(input("enter the h_of_tr: "))
    arot=1/2*(a_of_tr+b_of_tr)*h_of_tr
    print(arot)
arot()

#area of circle
def aroc():
    pi=3.142
    r_of_c=int(input("enter radius of circle: "))
    aroc=pi*r_of_c**2
    print(aroc)
aroc()

#area of ellipse
def aroe():
    pi=3.142
    a_of_e=int(input("enter a of e: "))
    b_of_e=int(input("enter b of e: "))
    aroe=pi*a_of_e*b_of_e
    print(aroe)
aroe()

#area of sector
def arose():
    theta_of_se=int(input("enter theta of sec: "))
    rad_of_se=int(input("enter radius of se: "))
    arose=1/2*rad_of_se**2*theta_of_se
    print(arose)
arose()

    
    
    


    
    