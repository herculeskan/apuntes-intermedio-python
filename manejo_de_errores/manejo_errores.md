# Manejo de errores

Modulo exclusivo para aprender a manejar errores.
Estos se pueden dividir en:
* cuando python nos avisa
  * El lenguaje nos devuelve un trace back
* cuando no nos avisa
  * Sencillamente lo que sucede es que programamos mal, nuestro algoritmo no funciona y hay algún paso donde las cosas están fallando. Lo que debemos hacer es revisar nuestro programa de principio a fin hasta encontrar el punto donde todo falla. A esto se le llama debuggin o depuración.

En otras palabras podemos decir que los errores se clasifican en *syntax error* y *excepciones*

* ***syntax error***
  * cuando escribimos mal, la diferencia de las excepciones es que el syntax error detiene el programa y python nisiquiera ejecuta la primera línea 

* ***exception***
  *  La diferencia con los errores de sintaxis si sucede en torno de nuestro programa haciendo que se rompa toda la lógica.
        1. **KeyboardInterrupt**: Excepcion que sucede cuando precionamos Ctrl + c en la consola interactiva de python. Significa que cortamo el proceso de python. En otras palabras ***eleva***(crea objeto tipo excepcion y lo mueve en nuestro programa en los bloques de código desde dentro hasta fuera)
        2. **KeyError**: sucede cuando queremos acceder a una llave de un diccionario que no existe
        3. **IndexError**: Sucede cuando estamos trabajando con una lista y accedemos a un índice que no existe
        4. **FileNotFoundError**: cuándo abrimos un archivo que no existe
        5. **ZeroDivisionError**: tratar de dividir un número entre 0
        6. **ImportError**: Sucede cuándo intentamos intentar importar un módulo y algo falla.
### ¿De qué manera python nos muestra una exception?
 ```python
 TraceBack (most resent call last):
  File "<stdin>", line1, in <module>
  ZeroDivisionError: division by zero
  ```
### ¿Cómo se lee un Traceback?
lo correcto es leer desde el final hasta el principio. Desde la última línea hasta la primera 

---

## Debuggin
Resolver errores de lógica. La mejor técnica para arreglar esto hay una técnica que se llama debuggin.
*notas*:
* por lo general se usa el debbugin de vs code, seleccionamos pausa y podemos navegar en nuestro código
### breakpoints
A la izquierda del VS code le podemos hacer un click para colocarle un punto rojo. Significa que cuando corramos el debugger, se va a cortar donde dejamos el punto

---

## Manejo de excepciones

Palabras clave (*raise, try, except y finally)

### try, except
 ```python
 def palindrome(string):
     return string == string[::-1]

try:
    print(palindrome(1))
except TypeError:
    print("solo se pueden ingresar strings")

```
* El bloque *try* son las declaraciones que te gustaría ejecutar. En caso tal de que fallen, el python salta este pedazo de bloque y se va para el *except*

* el bloque *except* se activa cuando el bloque try falla debido a una excepción. Contiene un conjunto de declaraciones que a menudo le dan un contexto sobre lo que salió mal dentro del bloque try. En otras palabras, el except es solo para los errores de tipo *TypeError*.

### raise
```python
def palindrome(string):
    try:
        f len(string) == 0:
        raise ValueError("no se puede ingresar una cadena vacía"
    return string == string[::-1]
    except Value Error as ve:
        print(ve)
        return false

try:
    print(palindrome(""))
    except TypeError: 
        print("Solo se pueden ingresar strings")
```
Es una forma de crear nuestros propios errores cuando detectemos algo en nuestro programa que no debería 

### finally
```python
try:
    f = open("archivo.txt")
    # buscar cualquier cosa dentro del archivo

finally:
    f.close()
```
Hacer algo si sucede un error o no 

---
## Assert Statements
```python
assert condición, mensaje de error
```
afirmo que: esta condición es verdadera, sino, imprime este mensaje de error

```python
def palindrome(string):
    assert len(string)>0, "No se puede ingresar una cadena vacía"
    return string == string[::-1]
print(palindrome(""))
#output
AssertionError: "No se puede ingresar una cadena vacía"
```