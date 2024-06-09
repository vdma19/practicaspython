Gryffindor_house = 0
Ravenclaw_house = 0
Hufflepuff_house = 0
Slyhterin_house = 0


print ("Te gusta el amanecer o el anochecer?")
print ("1. Amanecer")
print ("2. Anochecer")
respuesta1=int(input("Su respuesta es: "))
if respuesta1==1:
    Gryffindor_house +=1 
    Ravenclaw_house +=1
elif respuesta1==2:
    Hufflepuff_house +=1
    Slyhterin_house +=1
else:
    print("Respuesta invalida")

print ("Cuando muera, quiero que la gente me recuerde como: ")
print ("1. El bien")
print ("2. El grande")
print ("3. El sabio")
print ("4. El audaz")
respuesta2=int(input("Su respuesta es:  "))
if respuesta2==1:
    Hufflepuff_house +=2
elif respuesta2==2:
    Slyhterin_house +=2
elif respuesta2==3:
    Ravenclaw_house +=2
elif respuesta2==4:
    Gryffindor_house +=2
else:
    print("Respuesta invalida")

print ("Cual tipo de instrumento musical te gusta escuchar?:")
print ("1. El violin")
print ("2. La trompeta")
print ("3. El piano")
print ("4. El tambor")
respuesta3=int(input("Su respuesta es:  "))
if respuesta3==1:
    Hufflepuff_house +=4
elif respuesta3==2:
    Slyhterin_house +=4
elif respuesta3==3:
    Ravenclaw_house +=4
elif respuesta3==4:
    Gryffindor_house +=4
else:
    print("Respuesta invalida")

winning_house = "" #Declaro esta variable vacia para ir llenandola a continuacion

if Gryffindor_house > 0:
    winning_house = "Gryffindor"
elif Ravenclaw_house >0:
    winning_house = "Ravenclaw"
elif Slyhterin_house > 0:
    winning_house="Slytherin"
elif Hufflepuff_house >0:
    winning_house="Hufflepuff"
print ("Felicidades, la casa a la que tienes mas afinidas es " + winning_house + "!!")