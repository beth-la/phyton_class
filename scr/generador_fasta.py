''' Name 
    Contador de nucleotidos con input.
    
Version
    1.0
    
Author 
    Lopez A. Brenda E.
    
Descripcion
    Programa que genera un archivo fasat a parit de un archivo con extensión .txt que 
    contiene una secuencia de ADN.
    
Category
    DNA sequence
    
Usage
    None
    
Arguments
    None
    
See also
    None
    
'''


# Abrir el archivo.
# Se guarda el contenido del archivo.

with open('data/dna.txt','r') as archivo:
    ADN= archivo.read()

# Creamos un nuevo archivo que tendra el formato fasta.
# Escribimos el encabezado y la secuencia que esta contenida en la variable ADN
# Cerramos el arhivo. 

my_file= open("data/dna.fasta","w")
my_file.write(">sequence_name \n")
my_file.write(ADN)
my_file.close()
    
