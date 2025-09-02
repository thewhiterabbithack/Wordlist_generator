#!/usr/bin/env python3
import argparse
import sys
from termcolor import colored
import pyfiglet

banner = pyfiglet.figlet_format("THE WHITERABBIT")
print(banner)

# Introducimos la palabra y el número a combinar

parser = argparse.ArgumentParser(description="Generador de wordlist")
parser.add_argument('-p', '--palabra', help="Palabra para combinar")
parser.add_argument('-n', '--numero', type = int, help="Número para combinar")
args = parser.parse_args()

 

archivo_salida = 'wordlist.txt'
try:            
    with open(archivo_salida, 'w') as f:
        for i in range (args.numero):
            combinacion = args.palabra + str(i)
            f.write(combinacion + '\n')

    print (colored(f'El wordlist se ha creado en: {archivo_salida}', 'red'))
except:
   print (colored('No se ha podido generar el archivo, faltan argumentos.', 'green'))


   

