# Class Notes

# El Zen De Python

- Bello es mejor que Feo
- Explicito es mejor que Implicito
- Simple es mejor que Complejo
- Complejo es mejor que Complicado
- Plano es mejor que anidado
- Espaciado es mejor que denso
- La Legibilidad es Importante
- Los casos especiales no son lo suficientemente especiales como para romper las reglas
- Sin embargo la practicidad le gana a la pureza
- Los errores nunca deberian pasar silenciosamente 
- A menos que se silencien explicitamente
- Frente a la ambiguedad, evitar la tentación de adivinar.
- Deberia haber una y preferiblemente solo una, manera obvia de hacerlo
- A pesar de que esa manera no sea obvia a menos que seas holandés
- Ahora es mejor que nunca
- A pesar de que nunca es muchas veces que ahora mismo
- Si la implementacion es dificil de explicar, es una mala idea
- Si la implementacion es facil de explicar, es una buena idea
- Los name spaces son una gran idea, tengamos más de estos!

## Documentación

La Documentación es el manual de Python. En donde las personas colaboradoras del lenguaje han creado una extensa lista de funciones y 
aplicaciones del lenguaje. Se puede leer en la documentación una descripción muy extensa y tecnica sobre todo lo que se puede hacer 
con el lenguaje base. 

Librerias externas a Python deberian tener su propia documentación la cual cumple el mismo objetivo que la documentación de python.

Una de las partes de la documentación de Python son los PEP. O las formas en las que se debería realizar el código de Python. Hay PEPs de 
otros lenguajes cómo C.

## Entorno Virtual

Los entornos virtuales son entornos unicos para cada proyecto, en el cual debe estar totalmente enfocado a desarrollar ese proyecto. 
La mayor diferencia entre un entorno virtual y trabajar normalmente en python en nuestro computador. Es que si instalamos algo de manera 
global, una libreria, esta va a estar disponible en todos los proyectos de python de nuestro computador. Mientras que eso no va a afectar 
nuestros entornos virtuales.

El no afectar a nuestros entornos es importante para no tener problemas de compatibilidad al actualizar modulos o librerias.

Para hacer un Virtual Enviroment:

Primero vamos a ejercutar el comando Python con la flag module, llamando a venv o VirtualENViroment, y el nombre de nuestro enviroment, generalmente
venv.

python3 -m venv nombre-env

Para usar el Virtual Enviroment vamos a tener que activarlo, en windows es de la siguiente forma:
.\nombre-env\Scripts\activate
En sistemas tipo unix es así:
source nombre-env/bin/activate

Listo, para desactivar el venv. Vamos a simplemente escribir 

deactivate

## Packgage Installer for Python

Pip es una herramienta que nos va a permitir descargar código, modulos o dependencias para usar, cómo

- Pandas
- NumPy
- tkinter

usando 

pip install modulo-a-descargar

Se puede ver que dependencias, modulos o librerias se han descargado se puede usar:

pip freeze

Una forma de compartir las dependencias de los proyectos es modificar un poco el comando para que la salida de esté salga a un archivo 
llamado "requirements.txt" que van a ser las dependencias de nuestro proyecto. 

Pero esto ademas de ser una lista de las dependencias, se puden usar para descargar modificando un poco el comando de installar.

pip install -r requirements.txt

## Listas y Diccionarios Anidados

Lo de siempre, listas y diccionarios aninados con otras listas y diccionarios.

## List y Dict comprehentions

Las List y Dicts comprehetions son una forma de hacer una lista con un loop y si se necesita una condicional. Ahorrandonos espacio en nuestro 
código. Las comprehetions tienen la siguiente estructura:

variable = [valorAGuardar for valorAGuardar in range if valorAGuardar == condicional]

para dicts, solo vamos a agregarle una key a valor a guardar. 
El for loop puede ser para unos items de un dict o un array. No solo necesariamente un range().

## Funciones Anonimas: Lambda

Las funciones anonimas o Lambda. Son funciones que se pueden escribir en una sola linea en Python. Son bastante utiles para 
recortar parte del código de una forma sencillas. Sin embargo no las debemos usar cuando no se pueda reducir una funcion a sola una linea.
Su estructura es la siguiente:

variableQueTendraLaFunction = lambda tipoDato: function

El resultado que salga de function va a ser retornado al llamar la variableQueTendra... cómo una function. Esta tambien no solo puede ser usada
cómo una function a llamar sencilla. Tambien se puede usar cómo parametro al llamar otra function que necesite otra function.

## High Order Functions 

Las High order functions son functions que nos permiten obtener de una lista determinados elementos, dependiendo de su función nos pueden dar 
varios elementos. Las lambda functions son muy buenas para usarlas junto a estas functions

### filter
filter pide una function y una variable iterable, list o dict. En la function vamos a realizar una condicional que va a pasar por todos los 
elementos de la variable iterable. Al pasar true por esta condición, se van a agregar a la salida. 

### Map
map pide una function y una variable iterable. En la function vamos a realizar un cambio que va a pasar por todos los elementos. Todos los elementoscon los cambios dados por la function van a ser agregados a la Salida.

### Reduce

Reduce es parte del módulo functools de Python, es necesario llamarlo con: from functools import reduce

Reduce va a tomar una function y una variable iterable. Reduce va a ir por todos los elementos de la variable en pares y les va a aplicar la function. Devolviendo un unico valor reducido de la lista.
