import turtle

miTortuga = turtle.Turtle()

def poligono (nL, LongLado):
    for _ in range(nL):
        miTortuga.forward(LongLado)
        miTortuga.left(360/nL)
        
        
numLados = 5

for rr in range(12) :
        poligono(numLados, 100)
        miTortuga.left(30)
            
    

