# CONDICIONALES MULTIPLES EJEMPLERIZACION
print ('programa para determinar el desempeño de un estudiante')

n1 = input ('¿Cuál es su nombre? ')

m1 = int (input ('¿Cuál es su nota de matemáticas? '))
f1 = int (input ('¿Cuál es su nota de física? '))
e1 = int (input ('¿Cuál es su nota de español? '))

p1 = round(( m1 + f1 + e1 ) / 3 , 0)

if p1 == 4 :
    print ('Felicitaciones ' + n1 + ' aprobaste con "excelente" ' , p1 )
elif p1 == 3:
    print ('Felicitaciones ' + n1 + ' aprobaste con "alto" ' , p1 )
elif p1 == 2:
    print ('Te puedes esforzar más, ' + n1 + ' aprobaste con "básico" ' , p1 )
else:
    print ('Lo sentimos ' + n1 + ' reprobaste con "bajo" ' , p1 )