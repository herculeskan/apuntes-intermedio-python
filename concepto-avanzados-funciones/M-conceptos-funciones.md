# Conceptos avanzados de funciones
Una función es simplemente código que escribimos una vez y aplicamos después en diferentes lugares donde estemos trabajando.

## funciones anónimas: Lambda

Lambda son las funciones anónimas que contienen una sola expresión, es decir: funciones sin identificación, sin nombre:

```python
lambda argumento:expresión
```
* tenemos la palabra clave *lambda*
* un argumento seguido de una expresión donde se colocan los argumentos

En vez de usar *def* usamos *lambda*. Estas últimas pueden tener el argumento que nosotros necesitemos, pero una sola línea de expresión.

```python
palindrome = lambda string: string === string[::-1]
print(palindrome("ana"))
#output
True
```
![lambda](../M-a-ciclos_comp/images/lambda.png)
1. argumento o parametro que recibe la función para poder  acompañado de la palabra clave lambda
2. expresión con linea de código
3. variable con identificador, *ojo* no es de la función, sino de la variable que va a contener un objeto de tipo función que retorna toda la función de python

![lamda2](../M-a-ciclos_comp/images/lambda2.png)

* retorna un objeto tipo función. además de ser anónima, para llamarlo, pero el nombre que va a tener esta función con el que se le va a llamar después es la variable de tipo función.
con funciones normales se vería:

```python
def palindrome(string):
    return string == strig[::-1]
print(palindrome("ana"))
#output
True
```
>pongo el código otra vez para comparar

```python
palindrome = lambda string: string === string[::-1]
print(palindrome("ana"))
#output
True
```

| lamda    | def   |
| ---------| ------|
|parametro sin paréntesis | parametro con parentesis|
| usar lambda   | usar def  |
| sin parentesis    | entre parentesis |
| identificador como nombre de la variable | identificador como nombre de la funcion
| sin return | palabra return |