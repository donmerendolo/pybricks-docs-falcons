.. pybricks-requirements:: primehub

Prime Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/hub-prime.png
    :width: 40%

.. autoclass:: pybricks.hubs.PrimeHub
    :no-members:

    .. rubric:: Uso de la luz de estado del hub

    .. figure:: ../../main/diagrams/primehub_light.png
        :width: 22 em

    .. automethod:: pybricks.hubs::PrimeHub.light.on

    .. automethod:: pybricks.hubs::PrimeHub.light.off

    .. automethod:: pybricks.hubs::PrimeHub.light.blink

    .. automethod:: pybricks.hubs::PrimeHub.light.animate

    .. rubric:: Uso de la matriz de luces

    .. figure:: ../../main/diagrams/primehub_display.png
        :width: 22 em

    .. automethod:: pybricks.hubs::PrimeHub.display.orientation

    .. automethod:: pybricks.hubs::PrimeHub.display.off

    .. automethod:: pybricks.hubs::PrimeHub.display.pixel

    .. automethod:: pybricks.hubs::PrimeHub.display.icon

    .. automethod:: pybricks.hubs::PrimeHub.display.animate

    .. automethod:: pybricks.hubs::PrimeHub.display.number

    .. automethod:: pybricks.hubs::PrimeHub.display.char

    .. automethod:: pybricks.hubs::PrimeHub.display.text

    .. rubric:: Uso de los botones

    .. figure:: ../../main/diagrams/primehub_buttons.png
        :width: 22 em

    .. automethod:: pybricks.hubs::PrimeHub.buttons.pressed

    .. automethod:: pybricks.hubs::PrimeHub.system.set_stop_button

    .. rubric:: Uso de la IMU (básicamente el giroscopio y acelerómetro)

    .. automethod:: pybricks.hubs::PrimeHub.imu.ready

    .. automethod:: pybricks.hubs::PrimeHub.imu.stationary

    .. automethod:: pybricks.hubs::PrimeHub.imu.up

    .. automethod:: pybricks.hubs::PrimeHub.imu.tilt

    .. automethod:: pybricks.hubs::PrimeHub.imu.acceleration

    .. automethod:: pybricks.hubs::PrimeHub.imu.angular_velocity

    .. automethod:: pybricks.hubs::PrimeHub.imu.heading

    .. automethod:: pybricks.hubs::PrimeHub.imu.reset_heading

    .. automethod:: pybricks.hubs::PrimeHub.imu.rotation

    .. automethod:: pybricks.hubs::PrimeHub.imu.orientation

    .. automethod:: pybricks.hubs::PrimeHub.imu.settings

    .. rubric:: Uso del altavoz

    .. automethod:: pybricks.hubs::PrimeHub.speaker.volume

    .. automethod:: pybricks.hubs::PrimeHub.speaker.beep

    .. automethod:: pybricks.hubs::PrimeHub.speaker.play_notes

    .. rubric:: Uso de la mensajería Bluetooth sin conexión directa

    .. automethod:: pybricks.hubs::PrimeHub.ble.broadcast

    .. automethod:: pybricks.hubs::PrimeHub.ble.observe

    .. automethod:: pybricks.hubs::PrimeHub.ble.signal_strength

    .. automethod:: pybricks.hubs::PrimeHub.ble.version

    .. rubric:: Uso de la batería

    .. automethod:: pybricks.hubs::PrimeHub.battery.voltage

    .. automethod:: pybricks.hubs::PrimeHub.battery.current

    .. rubric:: Estado del cargador

    .. automethod:: pybricks.hubs::PrimeHub.charger.connected

    .. automethod:: pybricks.hubs::PrimeHub.charger.current

    .. automethod:: pybricks.hubs::PrimeHub.charger.status

    .. rubric:: Control del sistema

    .. automethod:: pybricks.hubs::PrimeHub.system.info

    .. automethod:: pybricks.hubs::PrimeHub.system.storage

        Puedes guardar hasta 512 bytes de datos en este hub. Los datos se borran
        si actualizas el firmware de Pybricks.

    .. automethod:: pybricks.hubs::PrimeHub.system.reset_storage

    .. automethod:: pybricks.hubs::PrimeHub.system.shutdown

Status light examples
---------------------

.. dropdown:: Turning the light on and off

    .. literalinclude::
        ../../../examples/pup/hub_common/build/light_off_primehub.py

.. dropdown:: Changing brightness and using custom colors

    .. literalinclude::
        ../../../examples/pup/hub_common/build/light_hsv_primehub.py

.. dropdown:: Making the light blink

    .. literalinclude::
        ../../../examples/pup/hub_common/build/light_blink_primehub.py

.. dropdown:: Creating light animations

    .. literalinclude::
        ../../../examples/pup/hub_common/build/light_animate_primehub.py

Matrix display examples
-----------------------

.. dropdown:: Displaying images

    .. literalinclude::
        ../../../examples/pup/hub_primehub/display_image.py

.. dropdown:: Displaying numbers

    .. literalinclude::
        ../../../examples/pup/hub_primehub/display_number.py

.. dropdown:: Displaying text

    .. literalinclude::
        ../../../examples/pup/hub_primehub/display_text.py

.. dropdown:: Displaying individual pixels

    .. literalinclude::
        ../../../examples/pup/hub_primehub/display_pixel.py

.. dropdown:: Changing the display orientation

    .. literalinclude::
        ../../../examples/pup/hub_primehub/display_orientation.py

.. dropdown:: Displaying orientation using the IMU

    .. literalinclude::
        ../../../examples/pup/hub_primehub/display_orientation_imu.py

.. dropdown:: Making your own images
    :name: make_your_own_images

    .. literalinclude::
        ../../../examples/pup/hub_primehub/display_matrix.py

.. dropdown:: Combining icons to make expressions

    .. literalinclude::
        ../../../examples/pup/hub_primehub/display_expression.py

.. dropdown:: Displaying animations

    .. literalinclude::
        ../../../examples/pup/hub_primehub/display_animate.py

Button examples
---------------

.. dropdown:: Detecting button presses

    .. literalinclude::
        ../../../examples/pup/hub_primehub/button_main.py

IMU examples
---------------

.. dropdown:: Testing which way is up

    .. literalinclude::
        ../../../examples/pup/hub_common/build/imu_up_primehub.py


.. dropdown:: Reading the tilt value

    .. literalinclude::
        ../../../examples/pup/hub_common/build/imu_tilt_primehub.py

.. dropdown:: Using a custom hub orientation

    .. literalinclude::
        ../../../examples/pup/hub_common/build/imu_tilt_blast_primehub.py

.. dropdown:: Reading acceleration and angular velocity vectors

    .. literalinclude::
        ../../../examples/pup/hub_common/build/imu_read_vector_primehub.py

.. dropdown:: Reading acceleration and angular velocity on one axis

    .. literalinclude::
        ../../../examples/pup/hub_common/build/imu_read_scalar_primehub.py


Bluetooth examples
------------------

.. dropdown:: Broadcasting data to other hubs

    .. literalinclude::
        ../../../examples/pup/hub_common/build/ble_broadcast_primehub.py

.. dropdown:: Observing data from other hubs

    .. literalinclude::
        ../../../examples/pup/hub_common/build/ble_observe_primehub.py


System examples
----------------------------------

.. dropdown:: Changing the stop button combination

    .. literalinclude::
        ../../../examples/pup/hub_primehub/button_stop.py

.. dropdown:: Turning the hub off

    .. literalinclude::
        ../../../examples/pup/hub_common/build/system_shutdown_primehub.py

