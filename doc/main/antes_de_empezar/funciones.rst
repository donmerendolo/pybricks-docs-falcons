Funciones
=========

Una función es como un mini programa dentro de un programa.
Python proporciona varias funciones integradas, como las funciones
``print()``, ``input()`` y ``len()``, pero también puedes escribir
las tuyas propias.

Para definir una función, se usa la palabra ``def``, seguida del
nombre de la función, los parámetros dentro de paréntesis, dos puntos
y el código de la función en las líneas siguientes:

.. code-block:: python

    def funcion(parametro1, parametro2):
        print(parametro1)
        print(parametro2)

        if parametro1 > parametro2:
            print('parametro1 es mayor que parametro2')
        
        return parametro1 + parametro2

Un propósito principal de las funciones es agrupar código que se ejecuta
varias veces. Sin una función definida, tendrías que copiar y pegar ese
código cada vez que quisieras ejecutarlo.

Argumentos y Parámetros
-----------------------

Cuando llamas a la función ``print()`` o ``len()``, le pasas valores,
llamados *argumentos*, ingresándolos entre los paréntesis.

Una cosa especial a tener en cuenta sobre los parámetros es que solo
se pueden usar dentro de la función en la que se definen, y no fuera.
Por ejemplo, si después de definir la función ``funcion()`` de antes,
intentamos utilizar ``parametro1`` fuera de la función, obtendremos
un error:

.. code-block:: python

    funcion(5, 10)
    print(parametro1)  # ¡ERROR!

Los términos *definir*, *llamar*, *pasar*, *argumento* y *parámetro*
pueden ser confusos. Para revisar sus significados, considera un
ejemplo de código:

.. code-block:: python

    def say_hello_to(name):
        # Imprime tres saludos al nombre proporcionado
        print('Buenos días, ' + name)
        print('Buenas tardes, ' + name)
        print('Buenas noches, ' + name)

    say_hello_to('Alberto')

*Definir* una función es crearla, igual que una sentencia
como ``spam = 42`` crea la variable ``spam`` y le da como valor el número 42.
La sentencia ``def`` define
la función ``say_hello_to()``. La línea ``say_hello_to('Alberto')`` *llama* a la
función ahora creada, enviando la ejecución a la parte superior del código
de la función. Esta llamada a función está *pasando* la cadena ``'Alberto'`` a la
función. Un valor que se pasa en una llamada a función es un *argumento*. Los
argumentos se asignan a variables locales llamadas *parámetros*. El argumento
``'Alberto'`` se asigna al parámetro ``name``.

Valores de Retorno y Sentencias return
---------------------------------------

Cuando llamas a la función ``len()`` y le pasas un argumento como ``'Hello'``,
la llamada a función se evalúa al valor entero ``5``, que es la longitud de la
cadena que le pasaste. En general, el valor al que se evalúa una llamada a función
se llama el *valor de retorno* de la función.

Al crear una función usando la sentencia ``def``, puedes especificar el valor
de retorno con una sentencia ``return``, que consiste en lo siguiente:

* La palabra clave ``return``
* El valor o expresión que la función debe devolver (retornar)

En el caso de una expresión, el valor de retorno es lo que esta expresión evalúa.
Por ejemplo, el siguiente programa define una función que devuelve una cadena
diferente dependiendo del número que se le pase como argumento.

.. code-block:: python

    import random

    def obtener_respuesta(num_respuesta):
        # Devuelve una respuesta de fortuna basada en qué int es num_respuesta, del 1 al 9
        if num_respuesta == 1:
            return 'Es seguro'
        elif num_respuesta == 2:
            return 'Definitivamente es así'
        elif num_respuesta == 3:
            return 'Sí'
        elif num_respuesta == 4:
            return 'Respuesta confusa, inténtalo de nuevo'
        elif num_respuesta == 5:
            return 'Pregunta de nuevo más tarde'
        elif num_respuesta == 6:
            return 'Concéntrate y pregunta de nuevo'
        elif num_respuesta == 7:
            return 'Mi respuesta es no'
        elif num_respuesta == 8:
            return 'El panorama no es tan bueno'
        elif num_respuesta == 9:
            return 'Muy dudoso'

    print('Haz una pregunta de sí o no:')
    input('>')
    r = random.randint(1, 9)
    fortuna = obtener_respuesta(r)
    print(fortuna)

Cuando el programa comienza, Python primero importa el módulo
``random``. Luego viene la definición de la función ``obtener_respuesta()``.
Debido a que la función no se está llamando, el código dentro de ella
no se ejecuta. Luego, el programa llama a la función ``random.randint()``
con dos argumentos: ``1`` y ``9``. Esta función evalúa un entero
aleatorio entre ``1`` y ``9`` (incluyendo ``1`` y ``9``), luego lo
almacena en una variable llamada ``r``.

Ahora el programa llama a la función ``obtener_respuesta()`` con ``r`` como
argumento. La ejecución del programa se mueve a la parte superior de esa
función, almacenando el valor ``r`` en un parámetro llamado
``num_respuesta``. Luego, dependiendo del valor en ``num_respuesta``, la
función retorna uno de muchos valores de cadena posibles. La ejecución regresa
a la línea en la parte inferior del programa que originalmente llamó a ``obtener_respuesta()``
y asigna la cadena retornada a una variable llamada ``fortuna``, que luego se
pasa a una llamada ``print()`` y se imprime en la pantalla.

Ten en cuenta que debido a que puedes pasar valores de retorno como
argumentos a otras llamadas de función, podrías acortar estas tres líneas:

.. code-block:: python

    r = random.randint(1, 9)
    fortuna = obtener_respuesta(r)
    print(fortuna)

a esta única línea equivalente:

.. code-block:: python

    print(obtener_respuesta(random.randint(1, 9)))

Recuerda que las expresiones consisten en valores y operadores; puedes usar una llamada a función en una expresión porque la llamada se evalúa a su valor de retorno.

.. admonition:: Funciones como "Cajas Negras"

   A menudo, todo lo que necesitas saber sobre una función son sus entradas (los parámetros) y su valor de salida; no siempre tienes que cargarte con cómo funciona realmente el código de la función. Cuando piensas en las funciones de esta manera de alto nivel, es común decir que estás tratando una función como una "caja negra".
