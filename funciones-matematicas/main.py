#!python3

import sys
import argparse
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from reader import read_data
from writer import write_data
from functions import Functions

def main(file_path, comando, arg, output):

    data = read_data(file_path)

    funcs = Functions()

    f = funcs.get(comando)

    res = f(data, arg)

    write_data(res, output)

if __name__  == "__main__":

    parser = argparse.ArgumentParser(
                description='Funciones matemáticas',
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--file',
                        default="numeros.txt",
                        help="Nombre del archivo con los números")

    parser.add_argument('--comando',
                        help="Nombre del comando")

    parser.add_argument('--arg',
                        type=int,
                        default=None,
                        help="Argumento del comando VARIACIONES")

    parser.add_argument('--output',
                        default='resultado.txt',
                        help="Nombre del archivo de salida")

    args = parser.parse_args()

    main(args.file, args.comando, args.arg, args.output)

