Color
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: pybricks.parameters.Color
    :no-members:

    .. rubric:: Saturated colors

    Estos colores tienen saturación y valor de brillo máximos.
    Solo difieren en el tono.

    .. autoattribute:: RED

        .. pybricks-color:: RED

    .. autoattribute:: ORANGE

        .. pybricks-color:: ORANGE

    .. autoattribute:: YELLOW

        .. pybricks-color:: YELLOW

    .. autoattribute:: GREEN

        .. pybricks-color:: GREEN

    .. autoattribute:: CYAN

        .. pybricks-color:: CYAN

    .. autoattribute:: BLUE

        .. pybricks-color:: BLUE

    .. autoattribute:: VIOLET

        .. pybricks-color:: VIOLET

    .. autoattribute:: MAGENTA

        .. pybricks-color:: MAGENTA

    .. rubric:: Colores no saturados

    Estos colores tienen tono y saturación cero. Solo difieren en el valor de brillo.

    Cuando se detectan estos colores usando sensores, sus valores dependen mucho
    de la distancia al objeto. Si la distancia entre el sensor y el objeto no es
    constante en tu robot, es mejor usar solo uno de estos colores en tus programas.

    .. autoattribute:: WHITE

        .. pybricks-color:: WHITE

    .. autoattribute:: GRAY

        .. pybricks-color:: GRAY

    .. autoattribute:: BLACK

        Esto representa objetos oscuros que reflejan muy poca luz.

        .. pybricks-color:: BLACK

    .. autoattribute:: NONE

        Esto es oscuridad total, sin reflexión ni luz en absoluto.

        .. pybricks-color:: NONE

.. rubric:: Creando tus propios colores

Este ejemplo muestra los conceptos básicos de las propiedades de color y cómo definir nuevos colores.

.. literalinclude::
    ../../../examples/pup/parameters/color_basics.py

Este ejemplo muestra usos más avanzados de la clase ``Color``.

.. literalinclude::
    ../../../examples/pup/parameters/color_advanced.py
