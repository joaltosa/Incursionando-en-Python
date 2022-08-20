# programa para determinar si un numero es par o impar
print ("\n==============================")
print ("Paridad e imparidad de numeros")
print ("==============================\n")

num = int (input ("Introduzca el número que desea probar  "))

eval = num % 2

if eval == 0:
    print (" \nel número " , num , ", es par")
else:
    print (" \nEl número  ", num , ",  es impar \n")
