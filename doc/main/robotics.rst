:mod:`robotics <pybricks.robotics>` -- Robótica y DriveBases
===============================================================

.. automodule:: pybricks.robotics
    :no-members:

.. autoclass:: pybricks.robotics.DriveBase
    :no-members:

    .. rubric:: Moverse según una distancia o ángulo dado

    Usa los siguientes comandos para recorrer una distancia dada o girar en un
    ángulo dado.

    Esto se mide utilizando los sensores de rotación internos. Debido a que las
    ruedas pueden deslizarse mientras se mueven, la distancia y el ángulo
    recorridos son solo estimaciones.

    .. automethod:: pybricks.robotics.DriveBase.straight

    .. automethod:: pybricks.robotics.DriveBase.turn

    .. automethod:: pybricks.robotics.DriveBase.arc

    .. automethod:: pybricks.robotics.DriveBase.settings

    .. automethod:: pybricks.robotics.DriveBase.done

    .. rubric:: Moverse indefinidamente

    Usa :meth:`.drive` para empezar a moverse a una velocidad y dirección deseadas.

    Sigue moviéndose hasta que uses :meth:`.stop` o cambies de rumbo
    usando :meth:`.drive` de nuevo. Por ejemplo, puedes moverlo hasta que se
    active un sensor y luego parar o dar la vuelta.

    .. automethod:: pybricks.robotics.DriveBase.drive

    .. automethod:: pybricks.robotics.DriveBase.stop

    .. automethod:: pybricks.robotics.DriveBase.brake

    .. rubric:: Medición

    .. automethod:: pybricks.robotics.DriveBase.distance

    .. automethod:: pybricks.robotics.DriveBase.angle

    .. automethod:: pybricks.robotics.DriveBase.state

    .. automethod:: pybricks.robotics.DriveBase.reset

    .. automethod:: pybricks.robotics.DriveBase.stalled

    .. rubric:: Moviéndose con el giroscopio

    .. automethod:: pybricks.robotics.DriveBase.use_gyro

    Si tu hub no está montado plano en tu robot, asegúrate de especificar
    los parámetros ``top_side`` y ``front_side`` cuando inicialices el
    :class:`PrimeHub() <pybricks.hubs.PrimeHub>` o
    :class:`TechnicHub() <pybricks.hubs.TechnicHub>`.
    De esta forma, el robot sabe en qué ángulo fijarse al girar.

    El giroscopio en cada hub es un poco diferente, lo que puede hacer que esté
    desviado unos pocos grados en giros grandes o en muchos giros pequeños.
    Por ejemplo, es posible que tengas que usar
    :meth:`turn(357) <pybricks.robotics.DriveBase.turn>` o
    :meth:`turn(362) <pybricks.robotics.DriveBase.turn>`
    en tu robot para hacer un giro completo.


    Por defecto, esta clase intenta mantener la posición del robot después
    de que se complete un movimiento. Esto significa que las ruedas girarán
    si levantas el robot, en un esfuerzo por mantener su ángulo de dirección.
    Para evitar esto, puedes elegir
    ``then=Stop.COAST`` en el último
    :meth:`straight <pybricks.robotics.DriveBase.straight>`,
    :meth:`turn <pybricks.robotics.DriveBase.turn>`, o
    :meth:`curve <pybricks.robotics.DriveBase.arc>` comando.

    .. _measuring:

    .. rubric:: Midiendo y validando de las dimensiones del robot

    Como primera estimación, puedes medir el ``wheel_diameter`` y el
    ``axle_track`` con una regla. Debido a que es difícil ver dónde tocan
    exactamente las ruedas el suelo, puedes estimar el ``axle_track`` como
    la distancia entre el punto medio de las ruedas.

    Si no tienes una regla, puedes usar una viga LEGO para medir. La distancia
    centro a centro de los agujeros es de 8 mm. Para algunos neumáticos, el
    diámetro está impreso en el lateral. Por ejemplo, 62.4 x 20 significa que el
    diámetro es de 62.4 mm y que el ancho es de 20 mm.

    En la práctica, la mayoría de las ruedas se comprimen ligeramente bajo el
    peso de tu robot. Para verificarlo, haz que tu robot se mueva 1000 mm
    usando ``my_robot.straight(1000)`` y mide cómo de lejos ha llegado realmente.
    Compensa de la siguiente manera:

        - Si el robot **no recorre la distancia suficiente**, **disminuye**
          ligeramente el valor de ``wheel_diameter``.
        - Si el robot **recorre más distancia de la esperada**, **aumenta** ligeramente el
          valor de ``wheel_diameter``.

    Los ejes y los ejes de los motores se doblan ligeramente bajo la carga del
    robot, haciendo que el punto de contacto con el suelo de las ruedas esté
    más cerca del punto medio de tu robot. Para verificarlo, haz que tu robot
    gire 360 grados usando ``my_robot.turn(360)`` y comprueba si termina en el
    mismo sitio:

        - Si el robot gira **demasiado poco**, **aumenta** ligeramente el valor de
          ``axle_track``.
        - Si el robot gira **demasiado**, **disminuye** ligeramente el valor de
          ``axle_track``.

    Cuando hagas ajustes, ajusta siempre primero el
    ``wheel_diameter``, como se ha hecho arriba. Asegúrate de probar tanto
    el giro como avance en línea recta después de terminar.

    .. rubric:: Uso individual de los motores de la DriveBase

    Después de crear un objeto :class:`.DriveBase`, aún puedes usar sus dos
    motores individualmente. Si inicias un motor, el otro motor se
    detendrá automáticamente. Del mismo modo, si un motor ya está en marcha y
    haces que la DriveBase se mueva, la maniobra original se cancela.

    .. rubric:: Ajustes avanzados

    El método :meth:`.settings` se usa para ajustar los ajustes usados por defecto
    de la velocidad y aceleración predeterminadas para avances y giros.
    Usa los siguientes atributos para ajustar ajustes de control más avanzados.

    .. autoattribute:: pybricks.robotics.DriveBase.distance_control
        :annotation:

    .. autoattribute:: pybricks.robotics.DriveBase.heading_control
        :annotation:


Ejemplos
-------------------

.. dropdown:: Avance y giro sobre sí mismo con una DriveBase

    Este programa muestra los conceptos básicos de avance y giro.

    .. literalinclude::
        ../../examples/pup/robotics/drivebase_basics.py
