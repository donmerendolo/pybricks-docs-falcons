# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""LEGO® Programmable Hubs."""

from typing import Sequence

from . import _common
from .parameters import Button as _Button, Axis


class TechnicHub:
    """LEGO® Technic Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _common.Battery()
    light = _common.ColorLight()
    imu = _common.IMU()
    system = _common.System()
    buttons = _common.Keypad([_Button.CENTER])
    ble = _common.BLE()

    def __init__(
        self,
        top_side: Axis = Axis.Z,
        front_side: Axis = Axis.X,
        broadcast_channel: int = None,
        observe_channels: Sequence[int] = [],
    ):
        """TechnicHub(top_side=Axis.Z, front_side=Axis.X, broadcast_channel=None, observe_channels=[])
        
        Inicializa el hub. Puedes especificar cómo el hub se
        :ref:`coloca en tu diseño <robotframe>` indicando en qué
        dirección apuntan el lado superior (con el botón)
        y el lado frontal (con la luz).

        Arguments:
            top_side (Axis): El eje que pasa por el *lado superior* del hub.
            front_side (Axis): El eje que pasa por el *lado frontal* del hub.
            broadcast_channel:
                Número de canal (0 a 255) usado para transmitir datos.
                Elige ``None`` si no usas transmisión.
            observe_channels:
                Una lista de canales para escuchar cuando se llama a ``hub.ble.observe()``.
                Escuchar más canales requiere más memoria.
                Por defecto es una lista vacía (sin canales).
        """


class PrimeHub:
    """LEGO® SPIKE Prime Hub."""

    # These class attributes are here for auto-documentation only.
    # In reality, they are instance attributes created by __init__.
    battery = _common.Battery()
    buttons = _common.Keypad(
        [
            _Button.LEFT,
            _Button.RIGHT,
            _Button.CENTER,
            _Button.BLUETOOTH,
        ]
    )
    charger = _common.Charger()
    light = _common.ColorLight()
    display = _common.LightMatrix(5, 5)
    speaker = _common.Speaker()
    imu = _common.IMU()
    system = _common.System()
    ble = _common.BLE()

    def __init__(
        self,
        top_side: Axis = Axis.Z,
        front_side: Axis = Axis.X,
        broadcast_channel: int = None,
        observe_channels: Sequence[int] = [],
    ):
        """PrimeHub(top_side=Axis.Z, front_side=Axis.X, broadcast_channel=None, observe_channels=[])

        Inicializa el hub. Puedes especificar cómo el hub se
        :ref:`coloca en tu diseño <robotframe>` indicando en qué
        dirección apuntan el lado superior (con el botón)
        y el lado frontal (con la luz).

        Arguments:
            top_side (Axis): El eje que pasa por el *lado superior* del hub.
            front_side (Axis): El eje que pasa por el *lado frontal* del hub.
            broadcast_channel:
                Número de canal (0 a 255) usado para transmitir datos.
                Elige ``None`` si no usas transmisión.
            observe_channels:
                Una lista de canales para escuchar cuando se llama a ``hub.ble.observe()``.
                Escuchar más canales requiere más memoria.
                Por defecto es una lista vacía (sin canales).
        """


# HACK: hide from jedi
del Axis
