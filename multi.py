from random import *



puntos = 1

for rr in range(0,10):
    a = randint(5,10)
    b = randint(5,10)
    print( a, 'x' , b, '=')
    strNum1 = input('Introduce el resultado: ')

    Num1 = int(strNum1)

    if Num1 == a*b:
        puntos = puntos + 1
        print('Correcto. Tienes', puntos)
        print('___________VAMOS________')
        
    else:
        print('Error. ATENTO HIJO El numero es', a*b)
        print('Sigues con', puntos, 'puntos')
        print('___________Atento________')
        

if puntos>8:
    print(' *************************')
    print('MUY BIEN. Tienes', puntos, 'puntos!!!')
    print(' :-)')
    
else:
    print(' *************************')
    print('Tienes que mejorar Miguel con', puntos, 'puntos. ANIMO')
    print(' :-(')