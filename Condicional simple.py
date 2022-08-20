"""# Sentencias condicionals simples
nom = input('Intruduzca su nombre completo')
print ('bienvenido ', nom , ', establecera condicionales simples')
n1 = int (input ('introduzca el 1er número:  '))
n2 = int (input ('introduzca el 2do número:  '))
if n1 > n2 :
    print ('el 1er número es mayor que el 2do')
else: 
    print ('el 1er número es menor que el 2do')
print ('Gracias, ' , nom)"""
# calcular la valoración promedio de un estudiante
print ('SISTEMA PARA CALCULO DE NOTA PROMEDIO')
n1 = input ('¿cuál es su nombre: ')
mat = float (input('¿Cuál es su valoración en matemáticas?  '))
fis = float (input ('y ¿Cuál en física?  '))
esp = float (input ( 'y ¿en español?  '))
d1 = ( mat + fis + esp )/3
if d1 >= 3:
    print ('felicitaciones, ' , n1 , 'ha aprobado con: ' , round ( d1 , 2 ))
else:
    print ('lo sentimos, ' , n1 , 'usted ha perdido con, ' , round ( d1 , 2))