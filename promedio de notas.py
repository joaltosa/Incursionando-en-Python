def notaMinima (nota1:float,nota2:float)->str:

    notaQueLleva = 0.3 * nota1 + 0.4 * nota2
    pasacon = (3.0 - (notaQueLleva)) / 0.3
 
    
    return "La nota que usted lleva es ", notaQueLleva , " y la nota mínima aprobatoria es " , pasacon
 
 
print (notaMinima (3.0 , 3.5))
print (notaMinima (2.4 , 3.8))
print (notaMinima (1.0 , 1.0))