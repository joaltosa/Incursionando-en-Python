# programa para elegir el número mayor
print ("=====================================")
print ("Seleccionar el mayor de tres números")
print ("=====================================")

num1 = int (input (" \nIntroduzca el 1er número  "))
num2 = int (input (" \nIntroduzca el 2do número  "))
num3 = int (input (" \nIntroduzca el 3er número  "))

if num1 > num2 and num2 > num3:
    print ("El número mayor es, ", num1 )
elif num2 > num3 and num3 > num1:
    print ("El número mayor es,  " , num2)
else:
    print ("\n El número mayor es\n  ", num3)
