# Parte 1: El Club “PICA-PICA”

## Run

Dentro del directorio _jugadores_ se deben encontrar el archivo de jugadores junto con los archivos de preferencias de los mismos

__Gale-Shapley__
```bash
$ python3 picapica.py gs 4 jugadores.rank 
```
o

```bash
$ python3 picapica.py gale-shapley 4 jugadores.rank 
```

__Matching estable__
```bash
$ python3 picapica.py sm 4 jugadores.rank 
```
o
```bash
$ python3 picapica.py me 4 jugadores.rank 
```
o
```bash
$ python3 picapica.py stable-matching 4 jugadores.rank 
```
o
```bash
$ python3 picapica.py matching-estable 4 jugadores.rank 
```

### Clean

Remueve **__pycache__**, _matching-estable.txt_ y _parejas.txt_

```bash
$ ./clean.sh
 
```
