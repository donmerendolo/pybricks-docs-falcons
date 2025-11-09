Sensor de color
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/diagrams/sensor_color_lights.png
   :width: 70 %

.. autoclass:: pybricks.pupdevices.ColorSensor
    :no-members:

    .. automethod:: pybricks.pupdevices.ColorSensor.color

    .. automethod:: pybricks.pupdevices.ColorSensor.reflection

    .. automethod:: pybricks.pupdevices.ColorSensor.ambient

    .. rubric:: Detección del color avanzada

    .. automethod:: pybricks.pupdevices.ColorSensor.hsv

    .. automethod:: pybricks.pupdevices.ColorSensor.detectable_colors

    .. rubric:: Luces integradas

    Este sensor tiene 3 luces integradas. Puedes ajustar el brillo de cada
    luz. Si usas el sensor para medir algo, las luces se encenderán o
    apagarán según sea necesario para la medición.

    .. automethod:: pybricks.pupdevices::ColorSensor.lights.on

    .. automethod:: pybricks.pupdevices::ColorSensor.lights.off


Examples
-------------------

.. dropdown:: Measuring color and reflection

    .. literalinclude::
        ../../../examples/pup/sensor_color/color_print.py


.. dropdown:: Waiting for a color

    .. literalinclude::
        ../../../examples/pup/sensor_color/wait_for_color.py


.. dropdown:: Reading *reflected* hue, saturation, and value

    .. literalinclude::
        ../../../examples/pup/sensor_color/hsv.py


.. dropdown:: Changing the detectable colors

    By default, the sensor is configured to detect red, yellow, green,
    blue, white, or no color, which suits many applications.

    For better results in your application, you can measure your desired
    colors in advance, and tell the sensor to look only for those colors.
    Be sure to measure them at the **same distance and light conditions**
    as in your final application. Then you'll get very accurate results
    even for colors that are otherwise hard to detect.
    
    .. literalinclude::
        ../../../examples/pup/sensor_color/detectable_colors.py

.. dropdown:: Reading *ambient* hue, saturation, value, and color

    .. literalinclude::
        ../../../examples/pup/sensor_color/color_ambient.py

.. dropdown:: Blinking the built-in lights

    .. literalinclude::
        ../../../examples/pup/sensor_color/lights_blink.py

.. dropdown:: Turning off the lights when the program ends

    .. literalinclude::
        ../../../examples/pup/sensor_color/cleanup.py
