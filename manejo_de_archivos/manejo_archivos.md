# ¿Cómo trabajar con archivos?
En el mundo de la programación hay diferentes tipos de archivo

## modos de apertura
* R ->lectura. Ver todo lo que tiene que ver nuestro archivo por dentro
* W -> escritura (sobre escribir) para poder escribir en un archivo nuevo pero que sobre escribe
* A -> Escritura (agregar al final)

```python
with open("./rut/del/archivo.text","r") as f:
```
* ***with*** manejador contextual del archivo. Esto hace que si el archivo finaliza inesperadamente, hace que el archivo no se rompa
* **open** abre un archivo con varios parametros pero los obligatorios son dos: el primero que es la ruta del archivo que estará en formato de string. Y el segundo parámetro que es el modo de apretura(r,w,a)
* **as** darle un nombre hipótetico al archivo.
---
código:

```python
def read():
    numbers = []
    with open("./direccion/archivo.txt, "r" encoding="utf-8") as f:
        for line in f:
            number.append(int(line))
    print(numbers)

def write():
    names = ["roberto","alberto","el pepe"]
    with open("./direction/archivo.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    write()