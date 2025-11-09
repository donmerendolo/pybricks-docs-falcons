.. pybricks-requirements::

Parada
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. class:: Stop

    Acción después de que el motor se detenga.

    .. autoattribute:: pybricks.parameters.Stop.COAST
        :annotation:

    .. autoattribute:: pybricks.parameters.Stop.COAST_SMART
        :annotation:

    .. autoattribute:: pybricks.parameters.Stop.BRAKE
        :annotation:

    .. autoattribute:: pybricks.parameters.Stop.HOLD
        :annotation:

    .. autoattribute:: pybricks.parameters.Stop.NONE
        :annotation:

    La tabla siguiente muestra cómo cada uno de los tipos de parada básicos añade un
    nivel extra de resistencia al movimiento. En estos ejemplos, ``m`` es un
    :class:`Motor <pybricks.pupdevices.Motor>` y ``d`` es una
    :class:`DriveBase <pybricks.robotics.DriveBase>`. Los ejemplos
    también muestran cómo se compara la ejecución a velocidad cero con estos tipos de parada.

    +--------+------------+-----------+------------------+------------------------+-----------------------------------------+
    | | Tipo | | Fricción | | Bloqueo | | Velocidad      |  | Ángulo mantenido en | | Ejemplos                              |
    |        |            |           | | mantenida en 0 |  | el objetivo         |                                         |
    +========+============+===========+==================+========================+=========================================+
    | Coast  | +          |           |                  |                        | | ``m.stop()``                          |
    |        |            |           |                  |                        | | ``m.run_target(500, 90, Stop.COAST)`` |
    +--------+------------+-----------+------------------+------------------------+-----------------------------------------+
    | Brake  | +          | +         |                  |                        | | ``m.brake()``                         |
    |        |            |           |                  |                        | | ``m.run_target(500, 90, Stop.BRAKE)`` |
    +--------+------------+-----------+------------------+------------------------+-----------------------------------------+
    |        | +          | +         | +                |                        | | ``m.run(0)``                          |
    |        |            |           |                  |                        | | ``d.drive(0, 0)``                     |
    +--------+------------+-----------+------------------+------------------------+-----------------------------------------+
    | Hold   | +          | +         | +                | +                      | | ``m.hold()``                          |
    |        |            |           |                  |                        | | ``m.run_target(500, 90, Stop.HOLD)``  |
    |        |            |           |                  |                        | | ``d.straight(0)``                     |
    |        |            |           |                  |                        | | ``d.straight(100)``                   |
    +--------+------------+-----------+------------------+------------------------+-----------------------------------------+
