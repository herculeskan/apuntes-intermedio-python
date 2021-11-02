# 1. List comprehesions

Las List comprehesions son la manera más elegante de escribir una lista iterable en Pyhton.

Por lo general es una sola línea que encierra el código en "[]"
Se puede usar para filtrar, formatear, modificar y todo lo que se puede hacer con la iteración. Para funcionar necesita estos 3 componentes
1. ciclo for
2. condición y expresion
3. output

![list](images/list2.png)

### Ejemplos
Reocrrer los valores del 1st al último
```python
1st = [1,2,3,4,5,6,7,8,9,10]

a = [x for x in 1st]
print(a)

#output
[1,2,3,4,5,6,7,8,9,10]
```
El equivalente sería ese
```python
for x in 1st:
    a.append(x)
```
Nos damos cuenta que ya no estamos necesitando append en nuestra lista.

Podemos usar list comprehesions para modificar cualquier elemento en *1st*
```python3
# add any number to every elements of lst and store it in a
a = [x+1 for x in lst]
 
# subtract any number to every elements of lst and store it in a
a = [x-1 for x in lst]
 
# multiply any number to every elements of lst and store it in a
a = [x*2 for x in lst]
```
### List Comprehesions with Single and Nested if condition
Podemos usar if para ayudarnos a filtrar data, por ejemplo. En el siguiente código estamos guardando todos los valores 1st en lsta c los valores que sean mayores que 4
```python3
lst = [1,2,3,4,5,6,7,8,9,10]
#con la condición if
c = [x for x in 1st if x > 4]
print(c)

#output
[5,6,7,8,9,10]
```
El equivalente sería
```python
for x in 1st:
    if x > 4:
        a.append(x)
```
 ### List Comprehesions with Single and Multiple If and Else Conditions

  Se le puede añadir múltiples if a estas listas
  ``` python3
  1st = [1,2,3,4,5,6,7,8,9,10]
  #con if condition
  e = [x if x > 4 else "less than 4" for x in 1st]
  #output
  ['less than 4', 'less than 4', 'less than 4', 'less than 4', 5, 6, 7, 8, 9, 10]
  ```

Esto serpia equivalente a:
```python
for x in 1st:
    if x > 4:
        d.append(x)
    else:
        d.append("less than 4")
```
Ahora, en el ejemplo de abajo habrá una list comprehesion con multiples *if and else*.
Vamos a almacenar en el string "Dos" si el valor es divisible por dos, "tres" si el valor es divisile por 3, lo demás estará almacenado en el valor "no 2 ni 3"

```python
f = ["Two" if x%2 else "Three" if x%3 == 0 else "not 2 & 3" for x in 1st  ]
print(f)
#output
['not 2 & 3', 'Two', 'Three', 'Two', 'not 2 & 3', 'Two', 'not 2 & 3', 'Two', 'Three', 'Two']
```
Esto funciona porque se divide toda la condicipon por 3 donde, después de cada else
```python
'Two' if x%2 == 0 else "Three" if x%3 == 0 else 'not 2 & 3'
```
si la primer condición if es true, tomarpa el valor de "Two", de no ser así se moverá a la segunda condición if, que guardará cualquier valor, como la condición elif.

Para la segunda condición if, guardará el valor "Three" si la condición resulta ser ciert. De lo contrario, va a revisar la siguiente condición, la cual no tenemos. Así que cualquieraque sea el valor que venga después del else, va a ser guardado, lo cual es el string "not 2 & 3".

la manera tradicional sería:

```python
for x in 1st:
    if x%2 == 0:
        f.append('two')
    elif x%3 == 0:
        f.append("Three")
    else:
        f.append("not 2 & 3)

```
### List Comprehension with a Nested For Loop

Para entender como funciona esto, haremos una serie de combinaciones posibles cn los números [1,2,3] y [3,2,1]

```python
lst =[1,2,3]
lst_rev = [3,2,1]
g = [(x,y) for x in lst for y in lst_rev]
print(g)
#output
[(1, 3), (1, 2), (1, 1), (2, 3), (2, 2), (2, 1), (3, 3), (3, 2), (3, 1)]
```
la tradicional sería:
```python
for x in lst:
    for y in lst_rev:
        f.append((x,y))
```
# List comprehesions
>generar listas sin ciclos
```python
def run():
    # squares = []

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    
    print(squares)


if __name__ == "__main__":
    run()
``` 
![comprehesions](images/comprehesions.png)

```python
[element for element in iterable if condition]
#El element representa a cada uno de los elementos a poner en la nueva lista
``` 
1. En elements representa a cada uno de los elementos a poner en la nueva lista
2. del < for elements in iterable >, el ciclo a partir del cual se extraerá elementos qde otra lista o cualqueier iterable.
3. < if condition> condición opcional para filtrar elementos del ciclo

```python
[i**2 for in range(1,101) if i % 3 !=0]
``` 
>para cada i de los números del 1 al 100 voy a guardar esa i al cuadtrado solamente si no es divisible por 3

* ***reto***
* crer, con un list comprehesion, una lista de todos los múltiplos de 4 que a la vez también son múltiplos de 6 y de 9, hasta llegar a los 5 digitos
  
```python
def run():
    my_list = [i for in range(1, 10000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(my_list)

if __name__ == '__main__':
    run()
```
# 2. Dictionary Comprehesion
# dictionary comprehesions

![dict_comprehesions](images/comprehesions.png)

1. En lugar de corchetes se pone llaves
2. en lugar de tener un elemento al principio, se tieen llave y valor
3. los primeros elementos llave y valor, son los que van a colocar en el nuevo diccionario

> para cada elemento de un iterable, yo voy a colocar una llave y un valor, solamente si se cumple una condición.

```python
def run():
    # my_dict = {}

    # for i in range(1, 101):
    #     if i % 3 !=0:
    #         my_dict[i] = i**2

    # print(my_dict)

    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    print(my_dict)


if __name__ == "__main__":
    run()
``` 
* crear, con un dictionary comprehesion, un diccionario cuyas llaves sean los 1000 primeros numeros naturales con sus raíces cuadradas como valores
```python
dictionary = {i: i**0.5 for i in range(1, 1001) }
print(dictionary)
```
###### test:
1. En un dictionary comprehesions la condición es:
opcional

2. En un list comprehesions la condición es 
Obligatoria

# 3. Listas y anidados
## Importante
aprender a usar el *.gitignore*
para ignorar la carpeta, dentro del archivo git ignore, solo tenemos que escribir el nombre de las cosas que queremos ignorar.
>las listas son una manera de organizar objetos y los dicionaros también pero con un formato llave y valor

* las listas pueden guardar diccionarios porque son objetos en python y los diccionarios pueden almacenar listas.
    * se pueden tener listas que almacenen diccionarios  y diccionarios que almacenen listas

```python
def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname":"Carlos", "lastname":"Lara"} 

    super_list = [
        #lista de diccionario
        {"firstname":"Carlos", "lastname":"Lara"},
        {"firstname":"JOse", "lastname":"Jose"},
        {"firstname":"Benito", "lastname":"Maradona"},
    ]

    super_dict = {
        #diccionario de listas
        "natural_nums": [1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[1.1, 4.5, 6.43],
    }

    for key, value in super_dict.items():
        print(key,"-",value)

if __name__ == '__main__':
    run()

```

