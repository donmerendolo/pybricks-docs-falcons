# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""Módulo de robótica para la API de Pybricks."""

from __future__ import annotations

from typing import Tuple, Optional, overload, TYPE_CHECKING

from . import _common
from .parameters import Stop

if TYPE_CHECKING:
    from ._common import Motor, MaybeAwaitable
    from .parameters import Number


class DriveBase:
    """Un vehículo robótico con dos ruedas motorizadas y una rueda de apoyo
    opcional o rueda loca.

    Al especificar las dimensiones de tu robot, esta clase
    facilita conducir una distancia determinada en milímetros o girar un
    número determinado de grados.

    Las distancias, radios o velocidades de conducción **positivas** significan
    conducir **hacia adelante**. **Negativas** significa **hacia atrás**.

    Los ángulos y tasas de giro **positivos** significan girar a la **derecha**.
    **Negativos** significa a la **izquierda**. Entonces, cuando se ve desde arriba,
    positivo significa en el sentido de las agujas del reloj y negativo significa
    en sentido contrario a las agujas del reloj.

    Consulta la sección `measuring`_ para consejos sobre cómo medir y ajustar los
    valores del diámetro de la rueda y la distancia entre ejes.
    """

    distance_control = _common.Control()
    """La distancia recorrida y la velocidad de conducción están controladas por un
    controlador PID. Puedes usar este atributo para cambiar su configuración.
    Consulta el atributo de :ref:`control del motor <settings>` para obtener una
    descripción general de los métodos disponibles. El atributo ``distance_control``
    tiene la misma funcionalidad, pero la configuración se aplica a cada milímetro
    recorrido por la base de conducción, en lugar de grados girados por un motor."""

    heading_control = _common.Control()
    """El ángulo de giro del robot y la tasa de giro están controlados por un
    controlador PID. Puedes usar este atributo para cambiar su configuración.
    Consulta el atributo de :ref:`control del motor <settings>` para obtener una
    descripción general de los métodos disponibles. El atributo ``heading_control``
    tiene la misma funcionalidad, pero la configuración se aplica a cada grado de
    rotación de toda la base de conducción (vista desde arriba) en lugar de grados
    girados por un motor."""

    def __init__(
        self,
        left_motor: Motor,
        right_motor: Motor,
        wheel_diameter: Number,
        axle_track: Number,
    ):
        """DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

        Arguments:
            left_motor (Motor):
                El motor que impulsa la rueda izquierda.
            right_motor (Motor):
                El motor que impulsa la rueda derecha.
            wheel_diameter (Number, mm):
                Diámetro de las ruedas.
            axle_track (Number, mm):
                Distancia entre los puntos donde ambas ruedas tocan el suelo.
        """

    def drive(self, speed: Number, turn_rate: Number) -> None:
        """drive(speed, turn_rate)

        Comienza a conducir a la velocidad y tasa de giro especificadas. Ambos
        valores se miden en el punto central entre las ruedas del robot.

        Arguments:
            speed (Number, mm/s): Velocidad del robot.
            turn_rate (Number, deg/s): Tasa de giro del robot.
        """

    def stop(self) -> None:
        """stop()

        Detiene el robot dejando que los motores giren libremente."""

    def brake(self) -> None:
        """brake()

        Detiene el robot frenando pasivamente los motores.
        """

    def distance(self) -> int:
        """distance() -> int: mm

        Obtiene la distancia recorrida estimada.

        Returns:
            Distancia recorrida desde el último reinicio.
        """

    def angle(self) -> float:
        """angle() -> float: deg

        Obtiene el ángulo de rotación estimado de la base de conducción.

        Returns:
            Ángulo acumulado desde el último reinicio.
        """

    def state(self) -> Tuple[int, int, int, int]:
        """state() -> Tuple[int, int, int, int]

        Obtiene el estado del robot.

        Returns:
            Tupla de distancia, velocidad de conducción, ángulo y tasa de giro del robot.
        """

    def reset(self, distance: Number = 0, angle: Number = 0) -> None:
        """reset(distance=0, angle=0)

        Reinicia la distancia recorrida estimada y el ángulo de rumbo.

        Esto también llama a :meth:`.stop` para detener los movimientos en curso.
        Si tu robot está controlado con :meth:`.use_gyro` establecido en ``True``,
        llamar a este método `también` establecerá el giroscopio en el ángulo dado.

        Arguments:
            distance (Number, mm): Velocidad del robot.
            angle (Number, deg): Ángulo de rumbo del robot.
        """

    @overload
    def settings(
        self,
        straight_speed: Optional[Number] = None,
        straight_acceleration: Optional[Number] = None,
        turn_rate: Optional[Number] = None,
        turn_acceleration: Optional[Number] = None,
    ) -> None: ...

    @overload
    def settings(self) -> Tuple[int, int, int, int]: ...

    def settings(self, *args):
        """
        settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
        settings() -> Tuple[int, int, int, int]

        Configura la velocidad y aceleración de la base de conducción.

        Si no proporcionas argumentos, esto devuelve los valores actuales como una tupla.

        Los valores iniciales se configuran automáticamente en función del diámetro de
        la rueda y la distancia entre ejes. Se seleccionan de manera que tu robot
        conduzca aproximadamente al 40% de su velocidad máxima.

        Los valores de velocidad dados aquí no se aplican al método :meth:`.drive`,
        ya que proporcionas tus propios valores de velocidad como argumentos en ese método.

        Arguments:
            straight_speed (Number, mm/s): Velocidad en línea recta del robot.
            straight_acceleration (Number, mm/s²): Aceleración y desaceleración
                en línea recta del robot. Proporciona una tupla con dos valores para
                establecer la aceleración y desaceleración por separado.
            turn_rate (Number, deg/s): Tasa de giro del robot.
            turn_acceleration (Number, deg/s²): Aceleración y desaceleración
                angular del robot. Proporciona una tupla con dos valores para
                establecer la aceleración y desaceleración por separado.
        """

    def straight(
        self, distance: Number, then: Stop = Stop.HOLD, wait: bool = True
    ) -> MaybeAwaitable:
        """straight(distance, then=Stop.HOLD, wait=True)

        Conduce en línea recta durante una distancia determinada y luego se detiene.

        Arguments:
            distance (Number, mm): Distancia a recorrer
            then (Stop): Qué hacer después de detenerse por completo.
            wait (bool): Esperar a que se complete la maniobra antes de continuar
                         con el resto del programa.
        """

    def turn(
        self, angle: Number, then: Stop = Stop.HOLD, wait: bool = True
    ) -> MaybeAwaitable:
        """turn(angle, then=Stop.HOLD, wait=True)

        Gira en el lugar un ángulo determinado y luego se detiene.

        Arguments:
            angle (Number, deg): Ángulo del giro.
            then (Stop): Qué hacer después de detenerse por completo.
            wait (bool): Esperar a que se complete la maniobra antes de continuar
                         con el resto del programa.
        """

    def arc(
        self,
        radius: Number,
        angle: Number = None,
        distance: Number = None,
        then: Stop = Stop.HOLD,
        wait: bool = True,
    ) -> MaybeAwaitable:
        """arc(radius, angle=None, distance=None, then=Stop.HOLD, wait=True)

        Conduce un arco (un círculo parcial) con un radio determinado. Puedes especificar
        qué tan lejos conducir usando un ángulo o una distancia.

        Con un radio positivo, el robot conduce a lo largo de un círculo hacia su derecha.
        Con un radio negativo, el robot conduce a lo largo de un círculo hacia su izquierda.

        Puedes especificar qué tan lejos viajar a lo largo de ese círculo como un ángulo
        (grados) o distancia (mm). Un valor positivo significa conducir hacia adelante
        a lo largo del círculo. Negativo significa conducir en reversa.

        Arguments:
            radius (Number, mm): Radio del círculo.
            angle (Number, deg): Ángulo para conducir a lo largo del círculo.
            distance (Number, mm): Distancia para conducir a lo largo del círculo,
                                   medida en el centro del robot.
            then (Stop): Qué hacer después de detenerse por completo.
            wait (bool): Esperar a que se complete la maniobra antes de continuar
                         con el resto del programa.
        Excepciones:
            ValueError:
                Debes especificar ``angle`` o ``distance``, pero no ambos. El
                radio no puede ser cero. Usa :meth:`.turn` para giros en el lugar.
        """

    def curve(
        self, radius: Number, angle: Number, then: Stop = Stop.HOLD, wait: bool = True
    ) -> MaybeAwaitable:
        """curve(radius, angle, then=Stop.HOLD, wait=True)

        Conduce un arco a lo largo de un círculo de un radio determinado, por un ángulo determinado.

        Arguments:
            radius (Number, mm): Radio del círculo.
            angle (Number, deg): Ángulo a lo largo del círculo.
            then (Stop): Qué hacer después de detenerse por completo.
            wait (bool): Esperar a que se complete la maniobra antes de continuar
                         con el resto del programa.
        """

    def done(self) -> bool:
        """done() -> bool

        Verifica si un comando o maniobra en curso está completo.

        Returns:
            ``True`` si el comando está completo, ``False`` si no.
        """

    def stalled(self) -> bool:
        """stalled() -> bool

        Verifica si la base de conducción está actualmente estancada.

        Está estancada cuando no puede alcanzar la velocidad o posición objetivo, incluso
        con la señal de actuación máxima.

        Returns:
            ``True`` si la base de conducción está estancada, ``False`` si no.
        """

    def use_gyro(self, use_gyro: bool) -> None:
        """use_gyro(use_gyro)

        Elige ``True`` para usar el sensor giroscópico para girar y conducir
        en línea recta. Elige ``False`` para confiar solo en los sensores de
        rotación integrados del motor.

        Este método llamará automáticamente a :meth:`.stop` para detener los
        movimientos en curso.

        Arguments:
            use_gyro (bool): ``True`` para habilitar, ``False`` para deshabilitar.
        """


class Car:
    """Un vehículo con un motor de dirección y uno o más motores para conducir.

    Cuando uses esta clase, el motor de dirección encontrará automáticamente la
    posición central. Esto también determina qué ángulo corresponde al 100%
    de dirección.
    """

    def __init__(
        self,
        steer_motor: Motor,
        drive_motors: Motor | Tuple[Motor, ...],
        torque_limit: Number = 100,
    ):
        """Car(steer_motor, drive_motors, torque_limit=100)

        Arguments:
            steer_motor (Motor):
                El motor que dirige las ruedas delanteras.
            drive_motors (Motor): El motor que impulsa las ruedas. Usa una tupla
                para múltiples motores.
            torque_limit (Number, %): El límite máximo de torque utilizado para encontrar
                los puntos finales del mecanismo de dirección, como porcentaje del
                torque máximo del motor de dirección.
        """

    def steer(self, percentage: Number) -> None:
        """steer(percentage)

        Dirige las ruedas delanteras en una cantidad determinada. Para una dirección del 100%,
        gira a la derecha por el ángulo que se determinó en la inicialización.
        Para una dirección del -100%, gira a la izquierda y 0% significa recto.

        Arguments:
            steering (Number, %): Cantidad para dirigir las ruedas delanteras.
        """

    def drive_power(self, power: Number) -> None:
        """drive_power(power)

        Conduce el automóvil a un nivel de potencia determinado. Los valores positivos conducen
        hacia adelante, los valores negativos conducen hacia atrás.

        El valor de ``power`` se usa para establecer el voltaje del motor como un porcentaje del
        voltaje de la batería. Por debajo del 10%, el automóvil dejará rodar las ruedas libremente
        para desplazarse suavemente en lugar de frenar bruscamente.

        Este comando es útil para aplicaciones de control remoto donde deseas una respuesta
        instantánea a pulsaciones de botones o movimientos de joystick.

        Arguments:
            speed (Number, %): Velocidad del automóvil.
        """

    def drive_speed(self, speed: Number) -> None:
        """drive_speed(speed)

        Conduce el automóvil a una velocidad de motor determinada. Los valores positivos conducen
        hacia adelante, los valores negativos conducen hacia atrás.

        Este comando es útil para una conducción más precisa con aceleración y desaceleración
        suaves. Esto aumenta automáticamente la potencia para mantener la velocidad a medida
        que conduces a través de obstáculos.

        Arguments:
            speed (Number, deg/s): Velocidad angular de los motores de conducción.
        """


# HACK: hide from jedi
if TYPE_CHECKING:
    del Motor
    del Number
    del MaybeAwaitable
    del Stop