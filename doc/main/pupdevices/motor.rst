Motors with rotation sensors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig_pupmotors:

.. figure:: ../../main/diagrams/pupmotors.png
   :width: 100 %
   :alt: pupmotors

   Motores de Powered Up con sensores de rotación. Las flechas indican la
   dirección positiva predeterminada. Consulta el módulo :mod:`hubs <pybricks.hubs>`
   para las direcciones predeterminadas de los motores integrados.

.. autoclass:: pybricks.pupdevices.Motor
    :no-members:

    .. rubric:: Medición

    .. automethod:: pybricks.pupdevices.Motor.angle

    .. automethod:: pybricks.pupdevices.Motor.reset_angle

    .. automethod:: pybricks.pupdevices.Motor.speed

    .. automethod:: pybricks.pupdevices.Motor.load

    .. automethod:: pybricks.pupdevices.Motor.stalled

    .. rubric:: Parada

    .. automethod:: pybricks.pupdevices.Motor.stop

    .. automethod:: pybricks.pupdevices.Motor.brake

    .. automethod:: pybricks.pupdevices.Motor.hold

    .. rubric:: Ejecutar indefinidamente

    .. automethod:: pybricks.pupdevices.Motor.run

    .. automethod:: pybricks.pupdevices.Motor.dc

    .. rubric:: Ejecutar según una cantidad fija

    .. automethod:: pybricks.pupdevices.Motor.run_time

    .. automethod:: pybricks.pupdevices.Motor.run_angle

    .. automethod:: pybricks.pupdevices.Motor.run_target

    .. automethod:: pybricks.pupdevices.Motor.run_until_stalled

    .. automethod:: pybricks.pupdevices.Motor.track_target

    .. automethod:: pybricks.pupdevices.Motor.done

    .. _settings:

    .. rubric:: Configuración del motor

    .. automethod:: pybricks.pupdevices.Motor.settings

    .. automethod:: pybricks.pupdevices.Motor.close

    .. rubric:: Configuración del control

    .. automethod:: pybricks.pupdevices.Motor.control.limits

    .. automethod:: pybricks.pupdevices.Motor.control.pid

        .. warning::
            Ojo con poner valores demasiado altos o demasiado bajos. El motor puede romperse. Mejor no tocarlo.

    .. automethod:: pybricks.pupdevices.Motor.control.target_tolerances

    .. automethod:: pybricks.pupdevices.Motor.control.stall_tolerances

    .. attribute:: control.scale

        Número de grados que gira el motor para completar un grado
        en la salida del tren de engranajes. Esta es la relación de engranajes
        determinada a partir del argumento ``gears`` al inicializar el motor.

    .. automethod:: pybricks.pupdevices.Motor.model.state

    .. automethod:: pybricks.pupdevices.Motor.model.settings

Initialization examples
-----------------------

.. dropdown:: Making the motor move back and forth

    .. literalinclude::
        ../../../examples/pup/motor/motor_init_basic.py

.. dropdown:: Initializing multiple motors

    .. literalinclude::
        ../../../examples/pup/motor/motor_init_multiple.py

.. dropdown:: Setting the positive direction as counterclockwise

    .. literalinclude::
        ../../../examples/pup/motor/motor_init_direction.py

.. dropdown:: Using gears

    .. literalinclude::
        ../../../examples/pup/motor/motor_init_gears.py

Measurement examples
-----------------------

.. dropdown:: Measuring the angle and speed

    .. literalinclude::
        ../../../examples/pup/motor/motor_measure.py

.. dropdown:: Resetting the measured angle

    .. literalinclude::
        ../../../examples/pup/motor/motor_reset_angle.py

.. dropdown:: Getting the absolute angle

    .. literalinclude::
        ../../../examples/pup/motor/motor_absolute.py


Movement examples
-----------------------

.. dropdown:: Basic usage of all run methods

    .. literalinclude::
        ../../../examples/pup/motor/motor_action_basic.py

.. dropdown:: Stopping ongoing movements in different ways

    .. literalinclude::
        ../../../examples/pup/motor/motor_stop.py

.. dropdown:: Using the ``then`` argument to change how a run command stops

    .. literalinclude::
        ../../../examples/pup/motor/motor_action_then.py

Stall examples
-----------------------

.. dropdown:: Running a motor until a mechanical endpoint

    .. literalinclude::
        ../../../examples/pup/motor/motor_until_stalled.py

.. dropdown:: Centering a steering mechanism

    .. literalinclude::
        ../../../examples/pup/motor/motor_until_stalled_center.py


Parallel movement examples
--------------------------

.. dropdown:: Using the ``wait`` argument to run motors in parallel

    .. literalinclude::
        ../../../examples/pup/motor/motor_action_wait.py

.. dropdown:: Waiting for two parallel actions to complete

    .. literalinclude::
        ../../../examples/pup/motor/motor_action_wait_advanced.py
