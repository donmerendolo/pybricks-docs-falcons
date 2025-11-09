Señales y unidades
=================


Muchos comandos permiten especificar argumentos en términos de magnitudes
físicas. Esta página ofrece una visión general de cada cantidad y su unidad.

Números
~~~~~~~

.. autodata:: pybricks.parameters.Number
  :noindex:

Tiempo
~~~~~~

.. _time:

tiempo: ms
---------
Todas las cantidades de tiempo se miden en milisegundos (ms).

Por ejemplo, la duración del movimiento con ``run_time``, y la duración
de :func:`wait <.tools.wait>` se especifican en milisegundos (ms).

Ángulos y movimiento angular
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _angle:

ángulo: °
-----------

Todos los ángulos se miden en grados (°).
Una vuelta completa corresponde a 360 grados.

Por ejemplo, los valores de ángulo de un ``Motor`` o del
``GyroSensor`` (giroscopio) se expresan en grados.

.. _speed:

velocidad angular: °/s
-----------------------

La velocidad angular describe cómo de rapido gira algo, expresada como
el número de grados por segundo (°/s).

Por ejemplo, la velocidad angular de un ``Motor`` o del
``GyroSensor`` (giroscopio) se expresa en grados por segundo.

Si bien recomendamos trabajar con grados por segundo en tus programas,
puedes usar la siguiente tabla para convertir entre unidades comúnmente usadas.

+-----------+-------+-----------+
|           | °/s   | rpm       |
+-----------+-------+-----------+
| 1 °/s =   | 1     | 1/6=0.167 |
+-----------+-------+-----------+
| 1 rpm =   | 6     | 1         |
+-----------+-------+-----------+

.. _acceleration:

aceleración angular: deg/s²
--------------------------------

La aceleración angular describe cómo de rápido cambia la velocidad angular.
Esto se expresa como el cambio del número de grados por segundo, durante
un segundo (°/s²). Esto también se escribe comúnmente como :math:`deg/s^2`.

Por ejemplo, puedes ajustar la aceleración angular de un ``Motor``
para cambiar cómo de suave o rápido alcanza la velocidad constante establecida.

Distancia y movimiento lineal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _distance:

distancia: mm
-------------
Las distancias se expresan en milímetros (mm) siempre que sea posible.

Por ejemplo, el valor de distancia del ``UltrasonicSensor``
se expresa en milímetros.


Si bien recomendamos trabajar con milímetros en tus programas,
puedes usar la siguiente tabla para convertir entre unidades comúnmente usadas.

+-------------+------+------+----------+
|             | mm   | cm   | pulgadas |
+-------------+------+------+----------+
| 1 mm =      | 1    | 0.1  | 0.0394   |
+-------------+------+------+----------+
| 1 cm =      | 10   | 1    | 0.394    |
+-------------+------+------+----------+
| 1 pulgada = | 25.4 | 2.54 | 1        |
+-------------+------+------+----------+

.. _dimension:

dimensión: mm
-------------

Las dimensiones se expresan en milímetros (mm), al igual que
las distancias.

Por ejemplo, las dimensiones de los sensores y motores
se especifican en milímetros (mm).

.. _linspeed:

velocidad: mm/s
------------
Las velocidades lineales se expresan en milímetros por segundo (mm/s).

Por ejemplo, la velocidad de un robot se expresa en mm/s.

.. _linacceleration:

aceleración lineal: mm/s²
--------------------------------

La aceleración lineal describe cómo de rápido cambia la velocidad lineal.
Esto se expresa como el cambio de los milímetros por segundo, durante
un segundo (mm/s²). Esto también se escribe comúnmente como :math:`mm/s^2`.

Por ejemplo, puedes ajustar la configuración de aceleración de una
:class:`DriveBase <.robotics.DriveBase>` para cambiar cómo
de suave o cómo de rápido alcanza el punto de ajuste de velocidad constante.

Unidades aproximadas y relativas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _percentage:

porcentaje: %
--------------

Algunas señales no tienen unidades específicas. Van desde un mínimo (0%) hasta un
máximo (100%). Los tipos específicos de porcentajes son :ref:`relative distances
<relativedistance>` o :ref:`brightness <brightness>`.

Otro ejemplo es el volumen del sonido,
que va desde 0% (silencio) hasta 100% (máximo volumen).

.. _relativedistance:

distancia relativa: %
---------------------

Algunas mediciones de distancia no tienen un valor exacto con una unidad específica,
pero varían desde muy cerca (0%) hasta muy lejos (100%). Estas se denominan distancias relativas.

Por ejemplo, el valor de distancia del ``InfraredSensor`` es una distancia relativa.

.. _brightness:

brillo: %
--------------

El brillo percibido de una luz se expresa como un porcentaje. Es 0% cuando
la luz está apagada y 100% cuando la luz está completamente encendida.
Cuando eliges 50%, esto significa que la luz se percibe como aproximadamente
la mitad de brillante para el ojo humano.

Fuerza y par
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _force:

fuerza: N
------------
Los valores de fuerza se expresan en newtons (N).

Si bien recomendamos trabajar con newtons en tus programas, puedes usar la
siguiente tabla para convertir a y desde otras unidades.

+---------+------+-------+-----------------------------+
|         | mN   | N     | lbf                         |
+---------+------+-------+-----------------------------+
| 1 mN =  | 1    | 0.001 | :math:`2.248 \cdot 10^{-4}` |
+---------+------+-------+-----------------------------+
| 1 N =   | 1000 | 1     | 0.2248                      |
+---------+------+-------+-----------------------------+
| 1 lbf = | 4448 | 4.448 | 1                           |
+---------+------+-------+-----------------------------+

.. _torque:

par: mNm
------------
Los valores de par se expresan en milinewtonmetros (mNm) a menos que se indique lo contrario.

Electricidad
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _voltage:

voltaje: mV
--------------
Los voltajes se expresan en milivoltios (mV).

Por ejemplo, puedes verificar el voltaje de la batería.

.. _current:

corriente: mA
--------------

La corriente eléctrica se expresa en miliamperios (mA).

Por ejemplo, puedes verificar la corriente suministrada por la batería.

.. _energy:

energía: J
--------------

La energía almacenada o el consumo de energía se pueden expresar en Julios (J).

.. _power:

potencia: mW
--------------

La potencia es la tasa a la que se almacena o consume energía. Se expresa en
milivatios (mW).

Ambiente
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _frequency:

frecuencia: Hz
--------------
Las frecuencias de sonido se expresan en Hercios (Hz).

Por ejemplo, puedes elegir la frecuencia de un pitido para cambiar el tono.

.. _temperature:

temperatura: °C
---------------

La temperatura se mide en grados Celsius (°C). Para convertir a grados
Fahrenheit (°F) o Kelvin (K), puedes usar las siguientes fórmulas:

    :math:`^{\circ}\kern1pt\!F =\kern1pt^{\circ}\kern1pt\!C \cdot \frac{9}{5} + 32`.

    :math:`K =\kern1pt^{\circ}\kern1pt\!C + 273.15`.

.. _hue:

tono: °
--------------
Tono de un color (0-359 grados).

.. _robotframe:

Marcos de referencia
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

El módulo de Pybricks y esta documentación usan las siguientes convenciones:

- X: Positivo significa hacia adelante. Negativo significa hacia atrás.
- Y: Positivo significa hacia la izquierda. Negativo significa hacia la derecha.
- Z: Positivo significa hacia arriba. Negativo significa hacia abajo.

Para asegurarte de que todas las mediciones del hub (como la aceleración) tengan el
valor y el signo correctos, puedes especificar cómo está montado el hub en tu robot.
Esto ajusta las mediciones para que sea fácil ver cómo se mueve tu *robot*,
en lugar de cómo se mueve el *hub*.

Por ejemplo, el hub puede estar montado boca abajo en tu diseño. Si
configuras los ajustes como se muestra en :numref:`fig_imuexamples`, las
mediciones del hub se ajustarán en consecuencia. De esta manera, un valor
positivo de aceleración en la dirección X significa que tu *robot*
acelera hacia adelante, aunque el *hub* acelere hacia atrás.

.. _fig_imuexamples:

.. figure:: ../main/diagrams/imuexamples.png
   :width: 100 %

   Cómo configurar los ajustes de ``top_side`` y ``front_side`` para tres
   diseños de robots diferentes. La misma técnica se puede aplicar a otros hubs
   y robots, al observar hacia dónde apuntan la parte superior y el frente
   :class:`Side <Side>` del hub. La configuración del ejemplo de la izquierda
   es la predeterminada.
