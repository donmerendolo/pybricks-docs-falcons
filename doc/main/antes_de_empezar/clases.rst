Clases
======

A lo largo de la documentación de Pybricks se hablan (entre otras
cosas) de clases. Por ejemplo, la clase ``TechnicHub``:

.. autoclass:: pybricks.hubs.TechnicHub
    :no-members:
    :noindex:

Las clases son las que tienen un rectángulo azul en la parte.
Las que tiene un rectángulo gris, son funciones o métodos.

La documentación nos da una descripción de la clase (el párrafo
que hay justo debajo del rectángulo azul) y podemos ver los
parámetros que acepta (a la derecha de "Parameters:"), junto
con una descripción de lo que hace cada uno. En este caso, los parámetros son
``top_side``, ``front_side``, ``broadcast_channel`` y ``observe_channels``.

Para la clase ``TechnicHub``, los parámetros tienen valores por
defecto, por lo que no es necesario especificarlos al crear un
objeto de esta clase, pero podemos cambiarlos por otros si queremos
igual que haríamos al especificar cualquier parámetro.

Con las clases podemos crear *objetos*. Ejemplo:

.. code-block:: python

    mi_hub = TechnicHub(top_side=Axis.Z, front_side=Axis.X)

Aquí hemos creado un objeto llamado ``mi_hub``, que es una
instancia de la clase ``TechnicHub`` y representa el hub de
Technic sobre el que se esta ejecutando nuestro código.

Este objeto tiene *métodos* (funciones) que podemos usar para
controlar el hub y *atributos*, que son otros objetos o propiedades 
dentro del hub.
Por ejemplo, el método ``light.on()`` para encender la luz del hub.
De esta forma, si queremos encender la luz del hub que hemos
creado, podemos usar:

.. code-block:: python

    mi_hub.light.on()

Para ver los métodos disponibles para una clase tenemos que ver la página de la documentación
de esa clase, que en este caso es :doc:`../hubs/technichub`.

Hay objetos que tienen como parámetros otros objetos creados
previamente por nosotros. Por ejemplo, para crear una DriveBase
hay que pasarle los objetos de los motores que queremos que use
(habiéndolos creado antes).

.. autoclass:: pybricks.robotics.DriveBase
    :no-members:

En este caso, los parámetros ``left_motor`` y ``right_motor`` son 
objetos de la clase ``Motor``, ``wheel_diameter`` y ``axle_track`` 
son números (*float* o *int*) que representan medidas en 
milímetros. Estos parámetros no tienen valores por defecto, por lo que es obligatorio especificarlos al crear la DriveBase:

.. code-block:: python

    # Primero crear los motores
    motor_izq = Motor(Port.A)
    motor_der = Motor(Port.B)

    # Luego crear la DriveBase usando esos motores
    mi_robot = DriveBase(motor_izq, motor_der, wheel_diameter=56,   axle_track=114)

Como un apunte final, en Python *todo es un objeto* (excepto las
estructuras de control como ``if`` o ``while``), incluso los
números, las funciones o los módulos que importamos. Una cadena
de texto que definamos con ``texto = "hola"`` es un objeto de tipo
``str`` (string) y tiene métodos como ``texto.upper()`` que
devuelve la cadena en mayúsculas.
