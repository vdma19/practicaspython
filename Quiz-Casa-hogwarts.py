def Q1 ():
    print ("Te gusta el amanecer o el anochecer?")
    print ("1. Amanecer")
    print ("2. Anochecer")
    respuesta1=int(input("Su respuesta es: "))
    if respuesta1==1:
        print( "Gryffindor y Ravenclaw +1 ")
    elif respuesta1==2:
        print ("Hufflepuff y Slytherin +1")
    else:
        print("Respuesta invalida")
Q1()
def Q2 ():
    print ("Cuando muera, quiero que la gente me recuerde como: ")
    print ("1. El bien")
    print ("2. El grande")
    print ("3. El sabio")
    print ("4. El audaz")
    respuesta2=int(input("Su respuesta es:  "))
    if respuesta2==1:
        print("Hufflepuff +2")
    elif respuesta2==2:
        print("Slytherin +2")
    elif respuesta2==3:
        print("Ravenclaw +2")
    elif respuesta2==4:
        print("Gryffindor +2")
    else:
        print("Respuesta invalida")
Q2()
def Q3():
    print ("Cual tipo de instrumento musical te gusta escuchar?:")
    print ("1. El violin")
    print ("2. La trompeta")
    print ("3. El piano")
    print ("4. El tambor")
    respuesta3=int(input("Su respuesta es:  "))
    if respuesta3==1:
        print("Hufflepuff +4")
    elif respuesta3==2:
        print("Slytherin +4")
    elif respuesta3==3:
        print("Ravenclaw +4")
    elif respuesta3==4:
        print("Gryffindor +4")
    else:
        print("Respuesta invalida")
Q3()

