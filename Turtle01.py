import turtle

miTortuga = turtle.Turtle()

seleccion = input("Triangulo o Cuadrado (T/C) ")

if seleccion == "C":
    for r in range(4) :
        
        miTortuga.forward(50)
        miTortuga.left(90)
        
    print("Cuadrado terminado ;-)")
    
elif seleccion == "T":
    for r in range(3) :
        
        miTortuga.forward(50)
        miTortuga.left(120)
        
    print("Triangulo terminado :-)")

else:
    print("Pues nada")
    
    
print("Fin")
    

