# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""Dispositivos genéricos de entrada/salida."""

from __future__ import annotations

from typing import Dict, Tuple, Optional, overload, TYPE_CHECKING

from . import _common
from .parameters import Port as _Port

if TYPE_CHECKING:
    from ._common import MaybeAwaitable, MaybeAwaitableTuple
    from .parameters import Number


class PUPDevice:
    """Motor o sensor Powered Up."""

    def __init__(self, port: _Port):
        """PUPDevice(port)

        Arguments:
            port (Port): Puerto al que está conectado el dispositivo.
        """

    def info(self) -> Dict[str, str]:
        """info() -> Dict

        Obtiene información sobre el dispositivo.

        Returns:
            Diccionario con información, como el ``id`` del dispositivo.
        """

    def read(self, mode: int) -> MaybeAwaitableTuple:
        """read(mode) -> Tuple

        Lee valores de un modo dado.

        Arguments:
            mode (int): Modo del dispositivo.

        Returns:
            Valores leídos del sensor.
        """

    def write(self, mode: int, data: Tuple) -> MaybeAwaitable:
        """write(mode, data)

        Escribe valores al sensor. Solo sensores y modos seleccionados admiten
        esto.

        Arguments:
            mode (int): Modo del dispositivo.
            data (tuple): Valores a escribir.
        """


class LUMPDevice:
    """Dispositivos que usan el LEGO UART Messaging Protocol."""

    def __init__(self, port: _Port):
        """LUMPDevice(port)

        Arguments:
            port (Port): Puerto al que está conectado el dispositivo.
        """

    def read(self, mode: int) -> MaybeAwaitableTuple:
        """read(mode) -> Tuple

        Lee valores de un modo dado.

        Arguments:
            mode (int): Modo del dispositivo.

        Returns:
            Valores leídos del sensor.
        """


class DCMotor(_common.DCMotor):
    """Motor DC para LEGO® MINDSTORMS EV3."""


class Ev3devSensor:
    """Lee valores de un sensor compatible con ev3dev."""

    sensor_index: int
    """Índice de la clase `lego-sensor`_ del sysfs de ev3dev."""

    port_index: int
    """Índice de la clase `lego-port`_ del sysfs de ev3dev."""

    def __init__(self, port: _Port):
        """Ev3devSensor(port)

        Arguments:
            port (Port): Puerto al que está conectado el dispositivo.
        """

    def read(self, mode: str) -> MaybeAwaitableTuple:
        """read(mode) -> Tuple

        Lee valores en un modo dado.

        Arguments:
            mode (str): `Nombre del modo`_.

        Returns:
            valores leídos del sensor.
        """


class AnalogSensor:
    """Sensor analógico genérico o personalizado."""

    def __init__(self, port: _Port):
        """AnalogSensor(port)

        Arguments:
            port (Port): Puerto al que está conectado el sensor.
        """

    def voltage(self) -> int:
        """voltage() -> int: mV

        Mide el voltaje analógico.

        Returns:
            Voltaje analógico.
        """

    def resistance(self) -> int:
        """resistance() -> int: Ω

        Mide la resistencia.

        Este valor solo es significativo si el dispositivo analógico es una carga pasiva
        como una resistencia o termistor.

        Returns:
            Resistencia del dispositivo analógico.
        """

    def active(self) -> None:
        """active()

        Establece el sensor en modo activo. Esto establece el pin 5 del puerto del sensor
        en `alto`.

        Esto se usa en algunos sensores analógicos
        para controlar un interruptor. Por ejemplo, si usas el Sensor de Luz NXT
        como un sensor analógico personalizado, este método encenderá la luz.
        De ahí en adelante, ``voltage()`` devuelve el valor de luz reflejada sin procesar.
        """

    def passive(self) -> None:
        """passive()

        Establece el sensor en modo pasivo. Esto establece el pin 5 del puerto del sensor
        en `bajo`.

        Esto se usa en algunos sensores analógicos
        para controlar un interruptor. Por ejemplo, si usas el Sensor de Luz NXT
        como un sensor analógico personalizado, este método apagará la luz.
        De ahí en adelante, ``voltage()`` devuelve el valor de luz ambiente sin procesar.
        """


class I2CDevice:
    """Dispositivo I2C genérico o personalizado."""

    def __init__(self, port: _Port, address: int):
        """I2CDevice(port, address)

        Arguments:
            port (Port): Puerto al que está conectado el dispositivo.
            address(int): Dirección I2C del dispositivo cliente. Ver
                :ref:`Direcciones I2C <i2caddress>`.
        """

    def read(self, reg: Optional[int], length: Optional[int] = 1) -> bytes:
        """read(reg, length=1)

        Lee bytes, comenzando en un registro dado.

        Arguments:
            reg (int): Registro en el que comenzar
                a leer: 0--255 o 0x00--0xFF.
            length (int): Cuántos bytes leer.

        Returns:
            Bytes devueltos por el dispositivo.
        """

    def write(self, reg: Optional[int], data: Optional[bytes] = None) -> None:
        """write(reg, data=None)

        Escribe bytes, comenzando en un registro dado.

        Arguments:
            reg (int): Registro en el que comenzar
                a escribir: 0--255 o 0x00--0xFF.
            data (bytes): Bytes a escribir.
        """


class UARTDevice:
    """Dispositivo UART genérico."""

    def __init__(self, port: _Port, baudrate: int, timeout: Optional[int] = None):
        """UARTDevice(port, baudrate, timeout=None)

        Arguments:
            port (Port): Puerto al que está conectado el dispositivo.
            baudrate (int): Velocidad en baudios del dispositivo UART.
            timeout (Number, ms): Cuánto tiempo esperar
                durante ``read`` antes de rendirse. Si eliges ``None``,
                esperará para siempre.
        """

    def read(self, length: int = 1) -> bytes:
        """read(length=1) -> bytes

        Lee un número dado de bytes del búfer.

        Tu programa esperará hasta que se reciba el número solicitado de bytes.
        Si esto toma más tiempo que ``timeout``, se genera la excepción ``ETIMEDOUT``.

        Arguments:
            length (int): Cuántos bytes leer.

        Returns:
            Bytes devueltos por el dispositivo.
        """

    def read_all(self) -> bytes:
        """read_all() -> bytes

        Lee todos los bytes del búfer.

        Returns:
            Bytes devueltos por el dispositivo.
        """

    def write(self, data: bytes) -> None:
        """write(data)

        Escribe bytes.

        Arguments:
            data (bytes): Bytes a escribir.
        """

    def waiting(self) -> int:
        """waiting() -> int

        Obtiene cuántos bytes aún están esperando ser leídos.

        Returns:
            Número de bytes en el búfer.
        """

    def clear(self) -> None:
        """clear()

        Vacía el búfer."""


class LWP3Device:
    """
    Se conecta a un hub que ejecuta firmware oficial de LEGO usando el
    `LEGO Wireless Protocol v3`_.

    .. _`LEGO Wireless Protocol v3`:
        https://lego.github.io/lego-ble-wireless-protocol-docs/
    """

    def __init__(
        self,
        hub_kind: int,
        name: str = None,
        timeout: int = 10000,
        pair: bool = False,
        num_notifications: int = 8,
    ):
        """LWP3Device(hub_kind, name=None, timeout=10000, pair=False, num_notifications=8)

        Arguments:
            hub_kind (int):
                El `identificador de tipo de hub`_ del hub al que conectarse.
            name (str):
                El nombre del hub al que conectarse o ``None`` para conectarse a cualquier
                hub.
            timeout (int):
                El tiempo, en milisegundos, a esperar por una conexión antes
                de generar una excepción.
            pair (bool): Si intentar el emparejamiento para una conexión segura.
                Esto es requerido para algunos hubs más nuevos.
            num_notifications (int): Número de mensajes entrantes del hub
                remoto a almacenar antes de descartar mensajes más antiguos.

        .. versionchanged:: 3.6

            Añadido parámetro ``pair``.

        .. versionchanged:: 3.7

            Añadido parámetro ``num_notifications``.

        .. _`identificador de tipo de hub`:
            https://github.com/pybricks/technical-info/blob/master/assigned-numbers.md#hub-type-ids
        """

    @overload
    def name(self, name: str) -> MaybeAwaitable: ...

    @overload
    def name(self) -> str: ...

    def name(self, *args):
        """name(name)
        name() -> str

        Establece u obtiene el nombre Bluetooth del dispositivo.

        Arguments:
            name (str): Nuevo nombre Bluetooth del dispositivo. Si no se proporciona ningún nombre,
                este método devuelve el nombre actual.
        """

    def write(self, buf: bytes) -> MaybeAwaitable:
        """write(buf)

        Envía un mensaje al hub remoto.

        Arguments:
            buf (bytes): El mensaje binario sin procesar a enviar.
        """

    def read(self) -> bytes | None:
        """read() -> bytes | None

        Recupera el mensaje almacenado en búfer más antiguo recibido del hub remoto.

        Si todos los mensajes almacenados en búfer ya han sido leídos, esto devuelve ``None``.

        Returns:
            El mensaje binario sin procesar más antiguo o ``None`` si no hay más mensajes.

        .. versionchanged:: 3.7

            Ahora admite la lectura de múltiples mensajes almacenados en búfer en lugar de bloquearse
            hasta que se recibiera un nuevo mensaje.
        """

    def disconnect(self) -> MaybeAwaitable:
        """disconnect()

        Desconecta el LWP3Device remoto del hub.
        """


class XboxController:
    """Usa el controlador Microsoft® Xbox® como un sensor en tus proyectos para
    controlarlos remotamente.

    El hub escaneará el controlador y se conectará a él. Se desconectará
    cuando el programa termine.

    Para consejos sobre conectividad y emparejamiento, ver :ref:`abajo <xbox-controller-pairing>`.
    """

    buttons = _common.Keypad([])

    def __init__(self):
        """"""

    def joystick_left(self) -> Tuple[int, int]:
        """joystick_left() -> Tuple

        Obtiene la posición del joystick izquierdo como porcentajes entre -100%
        y 100%. La posición central es (0, 0).

        Returns:
            Tupla de posición X (horizontal) e Y (vertical).
        """

    def joystick_right(self) -> Tuple[int, int]:
        """joystick_right() -> Tuple

        Obtiene la posición del joystick derecho como porcentajes entre -100%
        y 100%. La posición central es (0, 0).

        Returns:
            Tupla de posición X (horizontal) e Y (vertical).
        """

    def triggers(self) -> Tuple[int, int]:
        """triggers() -> Tuple

        Obtiene las posiciones de los gatillos izquierdo y derecho como porcentajes entre 0%
        y 100%.

        Returns:
            Tupla de posiciones de gatillos izquierdo y derecho.
        """

    def dpad(self) -> int:
        """dpad() -> int

        Obtiene el valor del pad direccional. ``1`` es arriba, ``2`` es arriba-derecha, ``3``
        es derecha, ``4`` es abajo-derecha, ``5`` es abajo, ``6`` es abajo-izquierda,
        ``7`` es izquierda, ``8`` es arriba-izquierda, y ``0`` es no presionado.

        Esto es esencialmente lo mismo que leer el estado de los
        botones ``Button.UP``, ``Button.RIGHT``, ``Button.DOWN``, y ``Button.LEFT``,
        pero este método convenientemente devuelve un número que indica
        una dirección.

        Returns:
            Posición del pad direccional, indicando una dirección.
        """

    def profile(self) -> int:
        """profile() -> int

        Obtiene el perfil actual del controlador. Solo disponible en el
        Xbox Elite Controller Series 2.

        Returns:
            Número de perfil.
        """

    def rumble(
        self,
        power: Number | Tuple[Number, Number, Number, Number] = 100,
        duration: int = 200,
        count: int = 1,
        delay: int = 100,
    ) -> MaybeAwaitable:
        """rumble(power=100, duration=200, count=1, delay=100)

        Hace que los actuadores integrados vibren, creando retroalimentación de fuerza.

        Si proporcionas un solo valor de ``power``, los actuadores principales izquierdo y derecho
        vibrarán ambos con esa potencia. Para un control más preciso, establece
        ``power`` como una tupla de cuatro valores, que controlan el actuador principal
        izquierdo, actuador principal derecho, actuador del gatillo izquierdo, y el actuador
        del gatillo derecho, respectivamente. Por ejemplo, ``power=(0, 0, 100, 0)``
        hace que el gatillo izquierdo vibre a máxima potencia.

        La vibración se ejecuta en segundo plano mientras tu programa continúa. Para
        hacer que tu programa espere, simplemente pausa el programa por una duración equivalente.
        Para una vibración, esto equivale a ``duration``. Para múltiples vibraciones, esto
        equivale a ``count * (duration + delay)``.

        Arguments:
            power (Number, % or tuple): Potencia de vibración.
            duration (Number, ms): Duración de vibración.
            count (int): Cantidad de vibraciones.
            delay (Number, ms): Retraso antes de cada vibración. Solo si ``count > 1``.
        """


# hide from jedi
if TYPE_CHECKING:
    del MaybeAwaitable
    del MaybeAwaitableTuple
    del Number