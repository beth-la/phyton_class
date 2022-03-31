# Name: Calculo de porcentaje de nucleotidos
# Version: 1.0
# Author: Lopez A. Brenda E.
# Descripcion: Programa que calcula el porcentaje de nucleotidos de una cadena de ADN almacenada en un archivo con extension .txt. 
# Category: 
# Usage:
# Arguments:
# See also:

# Pedimos la ruta del archivo al usuario, esto se guardara en la variable my_file. 

my_file= input("Inserta la ruta del archivo en el que se encuentra la secuencia ")

# Con with open no es necesario cerrar el archivo al final
# Del archivo obtenemos la longitud de la secuencia y la secuencia.
# La longitud del archivo la obtenemos con la funcion len() y guardamos el resultado en la variable longitud_secuencia
# .read() nos merpite almacenar el contenido del archivo en una variable, en este caso secuencia_adn 

with open(my_file) as archivo:
    secuencia_adn  = archivo.read()
    longitud_secuencia = len(secuencia_adn)

# Calculamos el porcentaje de AT con una regla de tres:
    
porcentaje_AT = ((secuencia_adn.count('A') + secuencia_adn.count('T')) * 100 )/(longitud_secuencia)

# El porcentaje de CG es el complemento: 

porcentaje_GC = (100 - porcentaje_AT)

# Imprimimos los resultados obtenidos: 

print(f"La proporción de AT y GC de la secuencia {secuencia_adn} es AT: {porcentaje_AT} GC: {porcentaje_GC}") 

    
    
    
