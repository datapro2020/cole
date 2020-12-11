# In

strNum1 = input('Introduce el 1er num ')
if strNum1.isdigit():
    Num1 = int(strNum1)/10
else:
    print(strNum1, 'Debe de ser un entero:')
    quit()

strNum2 = input('Introduce el 2nd num ')
if strNum2.isdigit():
    Num2 = int(strNum2)/10
else:
    print(strNum2, 'Debe de ser un entero:')
    quit()  

#Proccess
Suma = round(Num1 + Num2, 2)
Resta = round(Num1 - Num2, 2)
Div = round(Num1/Num2, 2)
Mult = round(Num1*Num2, 2)

#Out
print('Suma->', Num1, '+' ,Num2 , '=', Suma)
print('Resta->', Num1, '-' ,Num2 , '=', Resta)
print('Multi->', Num1, 'x' ,Num2 , '=', Mult)
print('Div->', Num1, ':' ,Num2 , '=', Div)


