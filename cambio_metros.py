from random import *

puntos = 0

units = ['km', 'hm', 'dam', 'm', 'dm', 'mm']

def calc (uno, dos, Num1):
    if uno>dos:
        print(10**(uno-dos))
        calculo= Num1/10**(uno-dos)
    else:
        calculo=Num1*10^(dos-uno)
    return calculo

a = randint(0,10)
b = randint(0,5)
pregunta= randint(0,5)
print( a, units[b], 'en', units[pregunta])
strNum1 = input('Introduce el resultado:' )




Num1 = int(strNum1)
Sol = calc(a, b, pregunta)

if Num1 == Sol:
    print('Correcto. Tienes', puntos)
    print('___________VAMOS________')
        
else:
    print('Error. ATENTO HIJO El numero es', Sol)
    print('Sigues con', puntos, 'puntos')
    print('___________Atento________')
        

    