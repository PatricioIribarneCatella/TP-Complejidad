# Parte 2: Funciones matemáticas / estadísticas

## Setup

- Dependencias:  [venv](https://docs.python.org/3.6/library/venv.html)

```bash
$ python3 -m venv venv

$ source venv/bin/activate
$ pip3 install --upgrade pip
$ pip3 install -r requirements.txt
```

## Run

```bash
$ ./num-generator.py [--file=FILE_NAME(numeros.txt) | --cant=CANTIDAD(3)]
$ ./main.py --comando=COMANDO [--fille=FILE_NAME(numeros.txt) |
			       --arg=VARIACIONES_ARG(2) |
			       --output=FILE_NAME(resultado.txt)]
```

### Clean

Remueve **__pycache__**, _numeros.txt_ y _resultados.txt_

```bash
$ ./clean.sh
 
```

