Importar módulos
================

En Python, el código está organizado en *módulos*. Un módulo
es un archivo que contiene código Python que hace algo
específico, y hay módulos para hacer básicamente cualquier cosa,
desde procesar los datos de un PDF hasta interactuar con alguna
página de internet.

Un módulo se importa con la palabra ``import`` seguida del
nombre del módulo:

.. code-block:: python

    import umath

Ahora podríamos usar funciones del módulo ``umath``, como
``umath.sqrt()`` para calcular la raíz cuadrada de un número.

Se pueden importar partes concretas de un módulo usando
``from ... import ...``:

.. code-block:: python

    from umath import sqrt

Ahora podemos usar ``sqrt()`` directamente sin tener que poner
``umath.``.

Pybricks, al ejecutarse en hubs de LEGO, está limitado en
comparación al Python que podríamos ejecutar en un ordenador.
Por eso Pybricks solo incluye los módulos necesarios para
programar los hubs y no incluye módulos para otras cosas como
procesar imágenes o conectarse a internet.

Para usar una clase o función de Pybricks hay que importarla
primero. Es normal que la parte de los imports de un programa
(que se pone al principio) sea algo así:

.. code-block:: python

    from pybricks.hubs import PrimeHub
    from pybricks.pupdevices import Motor, ColorSensor
    from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
    from pybricks.robotics import DriveBase
    from pybricks.tools import wait, StopWatch, Matrix

Lo normal es importar solo las clases y funciones que se
vayan a usar, pero no hay problema en importar más de las
necesarias.
