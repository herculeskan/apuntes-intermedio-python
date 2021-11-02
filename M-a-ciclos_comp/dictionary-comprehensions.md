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

