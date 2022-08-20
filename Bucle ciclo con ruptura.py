# Ciclo o bucle con ruptura o pare de programa "break"

print ("Ciclo con ruptura")

contador = 0

while contador <= 20:
    contador += 1
    if contador == 11:
        break
    print ("El valor actual de la variable es: " , contador)


# Ciclo o bucle que continúa

print ("Ciclo con continuar")

contador = 0

while contador <= 20:
    contador += 1
    if contador == 11:
        continue
    print ("El valor actual de la variable es: " , contador)
