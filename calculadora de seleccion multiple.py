# Calculadora de seleccion multiple
print ('==================================')
print ('Calculadora de selección multiple')
print ('===================================')

print (" ¿Qué desea hacer? ")
print ("1.  Suma ")
print ("2.  Resta")
print ("3.  Multiplicación")
print ("4.  División ")
print ("5.  División entera")
print ("6.  Módulo residuo división")
print ("7   Potenciación")

num = int (input (" \nseleccione la opción deseada \n"))

if num == 1:
    print ("elegiste 'suma' \n")
    num = int ( input ("Introduce el primer número  "))
    num += int (input (" \nintroduce el segundo número  " ))
    print (" \nEl resultado de la suma es ", num) 
    
elif num == 2:
    print ("elegiste 'Resta' \n")
    num = int ( input ("Introduce el primer número  "))
    num -= int (input (" \nintroduce el segundo número  " ))
    print (" \nEl resultado de la resta es ", num)

elif num == 3:
    print ("elegiste 'Multiplicación' \n")
    num = int ( input ("Introduce el primer número  "))
    num *= int (input (" \nintroduce el segundo número  " ))
    print (" \nEl resultado de la multiplicación es ", num)

elif num == 4:
    print ("elegiste 'División' \n")
    num = int ( input ("Introduce el primer número  "))
    num /= int (input (" \nintroduce el segundo número  " ))
    print (" \nEl resultado de la división es ", num)

elif num == 5:
    print ("elegiste 'División Entera' \n")
    num = int ( input ("Introduce el primer número  "))
    num //= int (input (" \nintroduce el segundo número  " ))
    print (" \nEl resultado de la división entera es ", num)

elif num == 6:
    print ("elegiste 'Módulo residuo de división' \n")
    num = int ( input ("Introduce el primer número  "))
    num %= int (input (" \n introduce el segundo número  " ))
    print (" \nEl resultado del módulo residuo de división es ", num)

elif num == 7:
    print ("elegiste 'Potenciación' \n")
    num = int ( input ("Introduce el primer número  "))
    num **= int (input (" \nintroduce el segundo número  " ))
    print (" \nEl resultado de la potenciación es ", num)

else:
    print ("Esa opción NO está disponible")
    print (" INTÉNTELO NUEVAMENTE ")
