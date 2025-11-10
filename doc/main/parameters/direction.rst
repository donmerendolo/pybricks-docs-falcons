Dirección
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. class:: Direction

    Rotación direccional para valores positivos de velocidad o ángulo.

    .. autoattribute:: pybricks.parameters.Direction.CLOCKWISE
        :annotation:

    .. autoattribute:: pybricks.parameters.Direction.COUNTERCLOCKWISE
        :annotation:

    +--------------------------------+----------------------------------+----------------------------------+
    | ``direccion_positiva =``       | Velocidad positiva:              | Velocidad negativa:              |
    +================================+==================================+==================================+
    | ``Direction.CLOCKWISE``        | sentido de las agujas del reloj  | contrario a las agujas del reloj |
    +--------------------------------+----------------------------------+----------------------------------+
    | ``Direction.COUNTERCLOCKWISE`` | contrario a las agujas del reloj | sentido de las agujas del reloj  |
    +--------------------------------+----------------------------------+----------------------------------+

    En general, el sentido de las agujas del reloj se define **mirando el eje del motor,
    como si miraras un reloj**. Algunos motores tienen dos ejes. Si tienes dudas,
    consulta el diagrama en la documentación de la clase ``Motor``.
    