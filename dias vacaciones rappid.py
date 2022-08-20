# Programa para calcular las vacaciones de empleado de RAPPID
print ("\n======================================")
print ("Cálculo de vacaciones empleados RAPPID")
print ("======================================= \n")

nombreEmpleado = input ("¿Cuál es el nombre del empleado?  ")
claveDepartamento = int (input ("¿ \nCuál es la clave de su departamento? "))
antiguedadTrabajador = float (input (" \n¿Cuántos años ha trabajado en el empresa? "))

if claveDepartamento == 1:
    if antiguedadTrabajador == 1 and antiguedadTrabajador < 2:
        print ("El empleado " + nombreEmpleado + " tiene derecho a 6 días de vacaciones")
    elif antiguedadTrabajador >= 2 and antiguedadTrabajador <= 6:
        print ("El empleado " + nombreEmpleado + " tiene derecho a 14 días de vacaciones")
    elif antiguedadTrabajador >= 7:
        print ("El empleado " + nombreEmpleado + " tiene derecho a 20 días de vacaciones")
    else:
        print("El empleadp, " + nombreEmpleado + ", aun no tiene derecho a vacaciones")


elif claveDepartamento == 2:
    if antiguedadTrabajador == 1 and antiguedadTrabajador < 2:
        print ("El empleado " + nombreEmpleado + " tiene derecho a 7 días de vacaciones")
    elif antiguedadTrabajador >= 2 and antiguedadTrabajador <=6:
        print ("El empleado " + nombreEmpleado + " tiene derecho a 15 días de vacaciones")
    elif antiguedadTrabajador >= 7:
        print ("El empleado " + nombreEmpleado + " tiene derecho a 22 días de vacaciones")
    else:
        print("El empleadp, " + nombreEmpleado + ", aun no tiene derecho a vacaciones")


elif claveDepartamento == 3:
    if antiguedadTrabajador == 1 and antiguedadTrabajador < 2:
        print ("El empleado " + nombreEmpleado + " tiene derecho a 10 días de vacaciones")
    elif antiguedadTrabajador >= 2 and antiguedadTrabajador <= 6:
        print ("El empleado " + nombreEmpleado + " tiene derecho a 20 días de vacaciones")
    elif antiguedadTrabajador >= 7:
        print ("El empleado " + nombreEmpleado + " tiene derecho a 30 días de vacaciones")
    else:
        print("El empleadp, " + nombreEmpleado + ", aun no tiene derecho a vacaciones")

else:
    print (" \nClave errada, inténtelo otra vez \n")
    