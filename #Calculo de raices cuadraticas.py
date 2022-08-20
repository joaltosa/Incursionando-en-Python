#Calculo de raices de funciones cuadraticas
print("=====================================")
print("cálculo de las raices de ecuacion cuadratica")
print("====================================")

A = int ( input ( "introduzca el valor de A " ))
B = int ( input ( "introduzca el valor de B " ))
C = int ( input ( "introduzca el valor de C " ))

resul1 = (-B+(B**2-4*A*C)**0.5)/(2*A)
resul2 = (-B-(B**2-4*A*C)**0.5)/(2*A)

print("la solución es " , resul1)
print("la solución es " , resul2)