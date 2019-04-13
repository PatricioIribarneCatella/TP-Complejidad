#!python3

#
# Genera números random
# de acuerdo a la cantidad
# que se le indique
#

import sys
import random
import argparse

def main(file_path, cantidad):
    
    with open(file_path, "w") as f:
        for i in range(cantidad):
            f.write(str(random.randint(0,99)) + '\n')

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
                description='Generador de números',
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--file',
                        default="numeros.txt",
                        help="Nombre del archivo con los números")

    parser.add_argument('--cant',
                        type=int,
                        default=3,
                        help="Cantidad de números")

    args = parser.parse_args()

    main(args.file, args.cant)

