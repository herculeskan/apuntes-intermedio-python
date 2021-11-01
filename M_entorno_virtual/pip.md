# Instalación de dependencias pip
Dentro de python existe un montón de códigos escrito por otras personas para instalarlas de manera externa.

* esto se llama instalador de dependencias, el más popular  es pip (Package Installer for Python)
* Módulos populares
  * Request (web scraping)
  * BeautifulSoup4(web scraping)
  * pandas (base de datos)
  * Numpy(base de datos)
  * Pytest (testing)

### Pip3
Es una herramienta que deberíamos usar en nuestro entorno virtual y nunca fuera del mismo:

```
pip3 freeze -> ver que módulos tenemos instalados en el momento
```
instalar pandas:

```
pip3 install pandas
```
una vez ya instalado, lo podemos utilizar en todos los archivos python que queramos en esta carpeta
*PD: pandas instala muchos módulos para funcionar*

#### ¿Cómo compartir el proyecto desarrollado con un compañero?

Para compartir el archivo de dependencias con otra persona en otro lugar para instalar nuestras dependencias
```
pip3 freeze > requirement.txt
```
>guardar la dependencia con sus mismos valores para repetirlos con otras personas xD
A la hora de compartir el proyecto con la otra persona va a poner

```
pip3 install -r requeriment.txt
```
Esto hará que se instale todo lo escrito en el requeriment.txt