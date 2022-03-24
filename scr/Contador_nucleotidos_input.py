# Name: Contador de nucleotidos con input.
# Version:
# Author: Lopez A. Brenda E.
# Descripcion: Programa que dada una secuencia de ADN mediante un input, cuenta la frecuencia de los nucleotidos.
# Category: 
# Usage:
# Arguments:
# See also:

# Pedimos al usuario ingrese una secuencia de ADN 

ADN= input("Introduce una secuencia de ADN: ")

# Tomando la secuencia guardada en la variable ADN, utilizamos el metodo count para contar la aparicion de cada letra dentro de la secuencia. 

print(f"La secuencia tiene estos nucleotidos: A:{ADN.count('A')} C:{ADN.count('C')} T:{ADN.count('T')} G:{ADN.count('G')}")