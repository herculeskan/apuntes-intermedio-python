#Módulo entorno virtual

## 1. Creación de entorno virtual
En la terminal escribimos esto para crear un entorno en python:
```
python -m venv venv

```
1. -m en python signifia modulo, módulo del lenguaje.
2. Llamamos a venv el cual significa (virtual enviroment)
3. Luego el nombre que le vamos a poner en el entorno virtua. *Por lo general se le pone venv o env*
4. Luego se crea una carpeta en la que vive un python específico.

>Luego activamos el python

Lo primero que tenemos qeu hacer es entrar a la carpeta *venv* desde la terminal. En windows se ubica en la carpeta *Scrips*, en linux en la carpeta *bin*

***Para activarlo se usa el siguiente comando***
```
source venv/bin/activate

para desactivarlo:

deactivate
```

###### Crear un alias

Un alias es un acortamiento de comandos para que sea más fácil escribirlo.
```
alias nombreAlias="El comando personalizado aquí
```

# 2. PIP
## Instalación de pip

Dentro de python existe un montón de códigos escritos por otras personas, pero tenemos que instalarlas de manera externa

* Esto se llama instalación de dependencias, el más popular es PIP (Package Installer for Python)
* módulos populares
  * request(web scraping)
  * BeautifulSoup4(web scraping)
  * Pandas (base de datos)
  * Numpy (base de datos)
  * Pytest (testing)

### Pip3
Es una herramienta que deberíamos usar en nuestro entorno virtual y nunca fuera del mismo

```
pip3 freeze > ver que módulos tenemos instalados en el momento

instalar pandas:

pip3 install pandas
```
Una vez instalado, lo podemos utilizar en todos los archivos python que queramos en esta carpeta

>PD: pandas instala  muchos módulos para funcionar

### compartir el proyecto desarrollado con un compañero

Para comprar el archivo de dependencia con otra persona en otro lutagr para instalar nuestras dependencias

```
pipe3 freeze > requeriment.txt
```
Esto guarda ls dependencia con sus mismos valores para repetirlos con otras personas..
Para instalar lo escrito en el archivo de texto,se usa el commando en la terminal:
```
pip3 install -r requeriment.txt
```
# 3. Una alternativa, Anaconda
Es una distribución especial de python, es un software completo para los científicos de datos.

* Nos permite crear un entorno virtual y dependencias de manera gráfica( pero solo nos sirve para ciencia de datos)
* Para backend lo mejor es pip

### Pasos para instalarla y ejecutarla
1. entrar a https://www.anaconda.com/products/individual
2. Dentro, bajamos para ver la versión que sea compatible con nuestro sistema operativo
3. Luego doble click en el instalador
4. *next* > *I agree* > *just me* > *next* > *elegir carpeta* > *next*
5. desmarcar los dos checks por defecto
6. Install 
 ![apu](https://i.pinimg.com/originals/58/a9/89/58a989a3ad3eb1884b687f31cc022657.jpg)
7. menú de inicio > anaconda navigator

* creamos un entorno, seleccionamos el lenguaje y la versión del mismo
* A diferencia de pip ya no se instalan dependencias de base 
* install > all > update index