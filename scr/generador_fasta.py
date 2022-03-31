# Name: Generador de un archivo fasta
# Version: 1.0 
# Author: Lopez A. Brenda E.
# Descripcion: Programa que genera un archivo fasta a partir de un archivo con extension .txt que contiene una secuencia de ADN.
# Category: 
# Usage:
# Arguments:
# See also:

# Abrir el archivo con with open cierra automaticamente el archvio. 
# Se guarda el contenido del archivo utilizando el metodo .read() en la variable ADN

with open('data/dna.txt','r') as archivo:
    ADN= archivo.read()

# Creamos un nuevo archivo que tendra el formato fasta, abriendolo como "write"
# Escribimos el encabezado y la secuencia que esta contenida en la variable ADN, con .write
# Cerramos el arhivo. 

my_file= open("data/dna.fasta","w")
my_file.write(">sequence_name \n")
my_file.write(ADN)
my_file.close()
    
