# Creación de entorno virtual

terminal para crear un entorno python
```
python -m venv venv
```
1. -m en python significa modulo, módulo del lenguaje.
2.  llamamos al venv el cuál significa (virtual enviroment)
3. luego el nombre que le vamos a poner en el entorno virtual. Por lo general se le pone venv o env
4. Luego se crea una carpeta en la que vive un python específico.
###### Luego activamos el python 

Lo primero que tenemos que hacer es entrar en nuestra carpeta *venv* desde la terminal. Ubicamos la carpeta scripts(en mi caso linux sería *bin*).
En ***bin*** se encuentra el comando para activar el entorno virtual. 

Para activarlo se usa el siguiente comando
```
source venv/bin/activate
```
>tuve que descargar este comando: sudo apt-get install python3-venv 
en la terminal nos dirigimos a venv y escribimos:
```
source bin/activate
```

###### Creaar un alias
Es un acortamiento de comandos para que sea más fácil escribirlo.
Primero, para salirnos del entorno virtual usamos el comando
```
deactivate
```
Para crear un alias usamos
```
alias nombreAlias="tu comando personalizado aquí"
```
en nuestro caso vendría siendo algo como:
 ```
 alias venv="source venv/bin/activate" 
 ```
