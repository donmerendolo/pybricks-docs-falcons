# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2022 The Pybricks Authors

"""Parámetros/argumentos constantes para la API de Pybricks."""

from __future__ import annotations

from enum import Enum
from typing import Union, TYPE_CHECKING
import os

from .tools import Matrix as _Matrix, vector as _vector

if TYPE_CHECKING or os.environ.get("SPHINX_BUILD") == "True":
    Number = Union[int, float]
    """
    Los números pueden representarse como enteros o valores de punto flotante:

        * Los enteros (:class:`int <ubuiltins.int>`) son números enteros
          como ``15`` o ``-123``.
        * Los valores de punto flotante (:class:`float <ubuiltins.float>`) son números decimales
          como ``3.14`` o ``-123.45``.

    Si ves :class:`Number` como el tipo de argumento, se pueden usar tanto
    :class:`int <ubuiltins.int>` como :class:`float <ubuiltins.float>`.

    Por ejemplo, :func:`wait(15) <pybricks.tools.wait>` y
    :func:`wait(15.75) <pybricks.tools.wait>` están ambos permitidos. Sin embargo, en la mayoría de las funciones,
    tu valor de entrada se truncará a un número entero de todos modos. En este
    ejemplo, cualquiera de los dos comandos hace que el programa se pause durante solo 15 milisegundos.
    """


class _PybricksEnumMeta(type(Enum)):
    @classmethod
    def __dir__(cls):
        yield "__class__"
        yield "__name__"
        for member in cls:
            yield member.name


class _PybricksEnum(Enum, metaclass=_PybricksEnumMeta):
    def __dir__(self):
        yield "__class__"
        for member in type(self):
            yield member.name

    def __str__(self):
        return "{}.{}".format(type(self).__name__, self.name)

    def __repr__(self):
        return str(self)


class Axis:
    """Unidades de un sistema de coordenadas.

    .. data:: X = vector(1, 0, 0)
    .. data:: Y = vector(0, 1, 0)
    .. data:: Z = vector(0, 0, 1)

    """

    X: _Matrix = _vector(1, 0, 0)
    Y: _Matrix = _vector(0, 1, 0)
    Z: _Matrix = _vector(0, 0, 1)


class Color:
    """Color de luz o superficie."""

    NONE: Color = ...
    BLACK: Color = ...
    GRAY: Color = ...
    WHITE: Color = ...
    RED: Color = ...
    ORANGE: Color = ...
    BROWN: Color = ...
    YELLOW: Color = ...
    GREEN: Color = ...
    CYAN: Color = ...
    BLUE: Color = ...
    VIOLET: Color = ...
    MAGENTA: Color = ...

    def __init__(self, h: Number, s: Number = 100, v: Number = 100):
        """Color(h, s=100, v=100)

        Arguments:
            h (Number, deg): Tono.
            s (Number, %): Saturación.
            v (Number, %): Valor de brillo.
        """

        self.h = int(h) % 360
        """
        El tono.
        """

        self.s = max(0, min(int(s), 100))
        """
        La saturación.
        """

        self.v = max(0, min(int(v), 100))
        """
        El valor de brillo.
        """

    def __iter__(self):
        """Permite el desempaquetado de la instancia Color en h, s y v."""
        return iter((self.h, self.s, self.v))

    def __repr__(self):
        return "Color(h={}, s={}, v={})".format(self.h, self.s, self.v)

    def __eq__(self, other: Color) -> bool: ...

    def __mul__(self, scale: float) -> Color:
        v = max(0, min(self.v * scale, 100))
        return Color(self.h, self.s, int(v), self.name)

    def __rmul__(self, scale: float) -> Color:
        return self.__mul__(scale)

    def __truediv__(self, scale: float) -> Color:
        return self.__mul__(1 / scale)

    def __floordiv__(self, scale: int) -> Color:
        return self.__mul__(1 / scale)


Color.NONE = Color(0, 0, 0)
Color.BLACK = Color(0, 0, 10)
Color.GRAY = Color(0, 0, 50)
Color.WHITE = Color(0, 0, 100)
Color.RED = Color(0, 100, 100)
Color.ORANGE = Color(30, 100, 100)
Color.BROWN = Color(30, 100, 50)
Color.YELLOW = Color(60, 100, 100)
Color.GREEN = Color(120, 100, 100)
Color.CYAN = Color(180, 100, 100)
Color.BLUE = Color(240, 100, 100)
Color.VIOLET = Color(270, 100, 100)
Color.MAGENTA = Color(300, 100, 100)


class Port(_PybricksEnum):
    """Puerto en el brick programable o hub."""

    # Generic motor/sensor ports
    A: Port = ord("A")
    B: Port = ord("B")
    C: Port = ord("C")
    D: Port = ord("D")
    E: Port = ord("E")
    F: Port = ord("F")

    # NXT/EV3 sensor ports
    S1: Port = ord("1")
    S2: Port = ord("2")
    S3: Port = ord("3")
    S4: Port = ord("4")


class Stop(_PybricksEnum):
    """Acción después de que el motor se detenga o alcance su objetivo."""

    COAST: Stop = 0
    """Dejar que el motor se mueva libremente."""

    COAST_SMART: Stop = 4
    """
    Dejar que el motor se mueva libremente. Para la próxima maniobra de ángulo relativo,
    tomar el último ángulo objetivo (en lugar del ángulo actual) como el nuevo
    punto de partida. Esto reduce los errores acumulativos. Esto solo se aplicará si el
    ángulo actual es menor que el doble de la tolerancia de posición configurada.
    """

    BRAKE: Stop = 1
    """Resistir pasivamente pequeñas fuerzas externas."""

    HOLD: Stop = 2
    """Seguir controlando el motor para mantenerlo en el ángulo comandado."""

    NONE: Stop = 3
    """
    No desacelerar al acercarse a la posición objetivo. Esto se puede usar
    para concatenar múltiples maniobras de motor o base de conducción sin detenerse. Si
    no se dan más comandos, el motor procederá a funcionar indefinidamente
    a la velocidad dada.
    """


class Direction(_PybricksEnum):
    """Dirección de rotación para valores positivos de velocidad o ángulo."""

    CLOCKWISE: Direction = 0
    """Una velocidad positiva debe hacer que el motor gire en el sentido de las agujas del reloj."""

    COUNTERCLOCKWISE: Direction = 1
    """Una velocidad positiva debe hacer que el motor gire en sentido contrario a las agujas del reloj."""

class Button(_PybricksEnum):
    """Botones en un hub o control remoto."""

    LEFT_DOWN: Button = 1
    LEFT_MINUS: Button = 1
    DOWN: Button = 2
    RIGHT_DOWN: Button = 3
    RIGHT_MINUS: Button = 3
    LEFT: Button = 4
    CENTER: Button = 5
    RIGHT: Button = 6
    LEFT_UP: Button = 7
    LEFT_PLUS: Button = 7
    UP: Button = 8
    BEACON: Button = 8
    RIGHT_UP: Button = 9
    RIGHT_PLUS: Button = 9
    BLUETOOTH: Button = 9
    A: Button = 0
    B: Button = 0
    X: Button = 0
    Y: Button = 0
    LB: Button = 0
    RB: Button = 0
    LJ: Button = 0
    RJ: Button = 0
    P1: Button = 0
    P2: Button = 0
    P3: Button = 0
    P4: Button = 0
    GUIDE: Button = 0
    MENU: Button = 0
    UPLOAD: Button = 0
    VIEW: Button = 0


class Side(_PybricksEnum):
    """Lado de un hub o un sensor."""

    RIGHT: Side = 6
    FRONT: Side = 0
    TOP: Side = 8
    LEFT: Side = 4
    BACK: Side = 5
    BOTTOM: Side = 2


class Icon:
    """Iconos para mostrar en una matriz de luz.

    Cada uno de los siguientes atributos son matrices. Esto significa que puedes escalar
    iconos para ajustar el brillo o agregar iconos para hacer composiciones.
    """

    UP: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    """
    DOWN: _Matrix = ...
    """
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    LEFT: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨🟨
    | ⬜⬜🟨⬜⬜
    """
    RIGHT: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | 🟨🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    ARROW_RIGHT_UP: _Matrix = ...
    """
    | ⬜⬜🟨🟨🟨
    | ⬜⬜⬜🟨🟨
    | ⬜⬜🟨⬜🟨
    | ⬜🟨⬜⬜⬜
    | 🟨⬜⬜⬜⬜
    """
    ARROW_RIGHT_DOWN: _Matrix = ...
    """
    | 🟨⬜⬜⬜⬜
    | ⬜🟨⬜⬜⬜
    | ⬜⬜🟨⬜🟨
    | ⬜⬜⬜🟨🟨
    | ⬜⬜🟨🟨🟨
    """
    ARROW_LEFT_UP: _Matrix = ...
    """
    | 🟨🟨🟨⬜⬜
    | 🟨🟨⬜⬜⬜
    | 🟨⬜🟨⬜⬜
    | ⬜⬜⬜🟨⬜
    | ⬜⬜⬜⬜🟨
    """
    ARROW_LEFT_DOWN: _Matrix = ...
    """
    | ⬜⬜⬜⬜🟨
    | ⬜⬜⬜🟨⬜
    | 🟨⬜🟨⬜⬜
    | 🟨🟨⬜⬜⬜
    | 🟨🟨🟨⬜⬜
    """
    ARROW_UP: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜🟨🟨🟨⬜
    | 🟨⬜🟨⬜🟨
    | ⬜⬜🟨⬜⬜
    | ⬜⬜🟨⬜⬜
    """
    ARROW_DOWN: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜⬜🟨⬜⬜
    | 🟨⬜🟨⬜🟨
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    ARROW_LEFT: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜🟨⬜⬜⬜
    | 🟨🟨🟨🟨🟨
    | ⬜🟨⬜⬜⬜
    | ⬜⬜🟨⬜⬜
    """
    ARROW_RIGHT: _Matrix = ...
    """
    | ⬜⬜🟨⬜⬜
    | ⬜⬜⬜🟨⬜
    | 🟨🟨🟨🟨🟨
    | ⬜⬜⬜🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    HAPPY: _Matrix = ...
    """
    | 🟨🟨⬜🟨🟨
    | 🟨🟨⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    | 🟨⬜⬜⬜🟨
    | ⬜🟨🟨🟨⬜
    """
    SAD: _Matrix = ...
    """
    | 🟨🟨⬜🟨🟨
    | 🟨🟨⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    | ⬜🟨🟨🟨⬜
    | 🟨⬜⬜⬜🟨
    """
    EYE_LEFT: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | 🟨🟨⬜⬜⬜
    | 🟨🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_RIGHT: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    """
    EYE_LEFT_BLINK: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | 🟨🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_RIGHT_BLINK: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    """
    EYE_RIGHT_BROW: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_LEFT_BROW: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | 🟨🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_LEFT_BROW_UP: _Matrix = ...
    """
    | 🟨🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    EYE_RIGHT_BROW_UP: _Matrix = ...
    """
    | ⬜⬜⬜🟨🟨
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    HEART: _Matrix = ...
    """
    | ⬜🟨⬜🟨⬜
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    """
    PAUSE: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜🟨⬜🟨⬜
    | ⬜🟨⬜🟨⬜
    | ⬜🟨⬜🟨⬜
    | ⬜⬜⬜⬜⬜
    """
    EMPTY: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    FULL: _Matrix = ...
    """
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    """
    SQUARE: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    | ⬜⬜⬜⬜⬜
    """
    TRIANGLE_RIGHT: _Matrix = ...
    """
    | ⬜🟨⬜⬜⬜
    | ⬜🟨🟨⬜⬜
    | ⬜🟨🟨🟨⬜
    | ⬜🟨🟨⬜⬜
    | ⬜🟨⬜⬜⬜
    """
    TRIANGLE_LEFT: _Matrix = ...
    """
    | ⬜⬜⬜🟨⬜
    | ⬜⬜🟨🟨⬜
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨🟨⬜
    | ⬜⬜⬜🟨⬜
    """
    TRIANGLE_UP: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | ⬜⬜🟨⬜⬜
    | ⬜🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | ⬜⬜⬜⬜⬜
    """
    TRIANGLE_DOWN: _Matrix = ...
    """
    | ⬜⬜⬜⬜⬜
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    | ⬜⬜🟨⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    CIRCLE: _Matrix = ...
    """
    | ⬜🟨🟨🟨⬜
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | 🟨🟨🟨🟨🟨
    | ⬜🟨🟨🟨⬜
    """
    CLOCKWISE: _Matrix = ...
    """
    | 🟨🟨🟨🟨⬜
    | 🟨⬜⬜🟨⬜
    | 🟨⬜⬜🟨⬜
    | 🟨⬜🟨🟨🟨
    | ⬜⬜⬜🟨⬜
    """
    COUNTERCLOCKWISE: _Matrix = ...
    """
    | ⬜🟨🟨🟨🟨
    | ⬜🟨⬜⬜🟨
    | ⬜🟨⬜⬜🟨
    | 🟨🟨🟨⬜🟨
    | ⬜🟨⬜⬜⬜
    """
    TRUE: _Matrix = ...
    """
    | ⬜⬜⬜⬜🟨
    | ⬜⬜⬜🟨⬜
    | 🟨⬜🟨⬜⬜
    | ⬜🟨⬜⬜⬜
    | ⬜⬜⬜⬜⬜
    """
    FALSE: _Matrix = ...
    """
    | 🟨⬜⬜⬜🟨
    | ⬜🟨⬜🟨⬜
    | ⬜⬜🟨⬜⬜
    | ⬜🟨⬜🟨⬜
    | 🟨⬜⬜⬜🟨
    """