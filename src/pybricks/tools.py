# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""Herramientas comunes para temporización, registro de datos y álgebra lineal."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Sequence, Tuple, overload, Coroutine

if TYPE_CHECKING:
    from ._common import MaybeAwaitable, MaybeAwaitableTuple
    from .parameters import Number


def wait(time: Number) -> MaybeAwaitable:
    """wait(time)

    Pausa el programa del usuario durante una cantidad de tiempo especificada.

    Arguments:
        time (Number, ms): Cuánto tiempo esperar.
    """


class StopWatch:
    """Un cronómetro para medir intervalos de tiempo. Similar a la función
    de cronómetro de tu teléfono."""

    def __init__(self): ...

    def time(self) -> int:
        """time() -> int: ms

        Obtiene el tiempo actual del cronómetro.

        Returns:
            Tiempo transcurrido.
        """

    def pause(self) -> None:
        """pause()

        Pausa el cronómetro."""

    def resume(self) -> None:
        """resume()

        Reanuda el cronómetro."""

    def reset(self) -> None:
        """reset()

        Reinicia el tiempo del cronómetro a 0.

        El estado de ejecución no se ve afectado:

        * Si estaba en pausa, permanece en pausa (pero ahora en 0).
        * Si estaba en ejecución, permanece en ejecución (pero comenzando nuevamente desde 0).
        """


class DataLog:
    """Crea un archivo y registra datos."""

    def __init__(
        self,
        *headers: str,
        name: str = "log",
        timestamp: bool = True,
        extension: str = "csv",
        append: bool = False,
    ):
        """DataLog(*headers, name='log', timestamp=True, extension='csv', append=False)

        Arguments:
            headers (str, str, ...): Encabezados de columna. Estos son los
                nombres de las columnas de datos. Por ejemplo, elige ``'time'`` y
                ``'angle'``.
            name (str): Nombre del archivo.
            timestamp (bool): Elige ``True`` para agregar la fecha y hora al
                nombre del archivo. De esta manera, tu archivo tiene un nombre único.
                Elige ``False`` para omitir la marca de tiempo.
            extension (str): Extensión del archivo.
            append (bool): Elige ``True`` para reabrir un archivo de registro de datos existente
                y agregar datos a él. Elige ``False`` para borrar los datos
                existentes. Si el archivo aún no existe, se creará un archivo vacío
                de cualquier manera.
        """

    def log(self, *values: Any) -> None:
        """log(value1, value2, ...)

        Guarda uno o más valores en una nueva línea del archivo.

        Arguments:
            values (object, object, ...): Uno o más objetos o valores.
        """


class Matrix:
    """Representación matemática de una matriz. Soporta
    suma (``A + B``), resta (``A - B``),
    y multiplicación de matrices (``A * B``) para matrices de tamaño compatible.

    También soporta multiplicación escalar (``c * A`` o ``A * c``)
    y división escalar (``A / c``).

    Un objeto :class:`.Matrix` es inmutable."""

    def __add__(self, other) -> Matrix: ...

    def __iadd__(self, other) -> Matrix: ...

    def __sub__(self, other) -> Matrix: ...

    def __isub__(self, other) -> Matrix: ...

    def __mul__(self, other) -> Matrix: ...

    def __rmul__(self, other) -> Matrix: ...

    def __imul__(self, other) -> Matrix: ...

    def __truediv__(self, other) -> Matrix: ...

    def __itruediv__(self, other) -> Matrix: ...

    def __floordiv__(self, other) -> Matrix: ...

    def __ifloordiv__(self, other) -> Matrix: ...

    def __init__(self, rows: Sequence[Sequence[float]]):
        """Matrix(rows)

        Arguments:
            rows (list): Lista de filas. Cada fila es en sí misma una lista de números.

        """

    @property
    def T(self) -> Matrix:  # noqa: N802
        """Devuelve una nueva :class:`.Matrix` que es la transpuesta de la
        original."""

    @property
    def shape(self) -> Tuple[int, int]:
        """Devuelve una tupla (``m``, ``n``),
        donde ``m`` es el número de filas y ``n`` es el número de columnas.
        """


@overload
def vector(x: float, y: float) -> Matrix:
    """
    Función de conveniencia para crear una :class:`.Matrix` con forma (``2``, ``1``).

    Arguments:
        x (float): coordenada x del vector.
        y (float): coordenada y del vector.

    Returns:
        Una matriz con la forma de un vector columna.
    """


@overload
def vector(x: float, y: float, z: float) -> Matrix:
    """
    Función de conveniencia para crear una :class:`.Matrix` con forma (``3``, ``1``).

    Arguments:
        x (float): coordenada x del vector.
        y (float): coordenada y del vector.
        z (float): coordenada z del vector.

    Returns:
        Una matriz con la forma de un vector columna.
    """


def vector(*args):
    """
    vector(x, y) -> Matrix
    vector(x, y, z) -> Matrix

    Función de conveniencia para crear una :class:`.Matrix` con
    forma (``2``, ``1``) o (``3``, ``1``).

    Arguments:
        x (float): coordenada x del vector.
        y (float): coordenada y del vector.
        z (float): coordenada z del vector (opcional).

    Returns:
        Una matriz con la forma de un vector columna.
    """


def cross(a: Matrix, b: Matrix) -> Matrix:
    """
    cross(a, b) -> Matrix

    Obtiene el producto vectorial ``a`` × ``b`` de dos vectores.

    Arguments:
        a (Matrix): Un vector tridimensional.
        b (Matrix): Un vector tridimensional.

    Returns:
        El producto vectorial, también un vector tridimensional.
    """


def read_input_byte(last: bool = False, chr: bool = False) -> Optional[int | str]:
    """
    read_input_byte() -> int | str | None

    Lee un byte de la entrada estándar sin bloquear y lo elimina del
    búfer de entrada.

    Arguments:
        last (bool): Elige ``True`` para leer el último (más reciente) byte en el búfer y descartar el resto.
                     Elige ``False`` para leer solo el primer (más antiguo) byte.
        chr (bool): Elige ``True`` para convertir el resultado a una cadena de un solo carácter.

    Returns:
        El byte que se leyó, como un valor numérico (``0`` a ``255``) o
        cadena (ej. ``"B"``). Devuelve ``None`` si no hay datos disponibles. Si
        ``chr=True``, también devuelve ``None`` si el byte que se leyó no es
        imprimible como un carácter.
    """


def hub_menu(*symbols: int | str) -> int | str:
    """
    hub_menu(symbol1, symbol2, ...) -> int | str

    Muestra un menú en la pantalla del hub y espera a que el usuario seleccione un elemento
    usando los botones. Puede usarse en tu propio programa de menú que te permite
    elegir cuál de tus otros programas ejecutar.

    Ten en cuenta que esto es solo una función de conveniencia que combina la pantalla,
    los botones y las esperas para hacer un menú simple. Esto significa que puede usarse
    en cualquier lugar de un programa, no solo al inicio.

    Arguments:
        symbol1 (int or str): El primer símbolo a mostrar en el menú.
        symbol2 (int or str): El segundo símbolo, y así sucesivamente...

    Returns:
        El símbolo seleccionado.
    """


def multitask(*coroutines: Coroutine, race=False) -> MaybeAwaitableTuple:
    """
    multitask(coroutine1, coroutine2, ...) -> Tuple

    Ejecuta múltiples corrutinas concurrentemente. Esto crea una nueva corrutina que
    puede usarse como cualquier otra, incluso en otra declaración ``multitask``.

    Arguments:
        coroutines (coroutine, coroutine, ...): Una o más corrutinas para ejecutar
            en paralelo.
        race (bool): Elige ``False`` para esperar a que todas las corrutinas terminen.
            Elige ``True`` para esperar a que una corrutina termine y luego
            cancelar las demás, como si fuera una "carrera".

    Returns:
        Tupla de los valores de retorno de cada corrutina. Las corrutinas no terminadas
        tendrán ``None`` como su valor de retorno.
    """


def run_task(coroutine: Coroutine) -> Optional[bool]:
    """
    run_task(coroutine) -> bool | None

    Ejecuta una corrutina de principio a fin mientras bloquea el resto del
    programa. Se usa principalmente para ejecutar la corrutina principal de un programa.

    No se permiten llamadas anidadas a esta función.

    Arguments:
        coroutine (coroutine): La corrutina principal a ejecutar.

    Returns:
        Si no se proporciona ``coroutine``, esta función devuelve si el
        bucle de ejecución está actualmente activo (``True``) o no (``False``).
    """


# HACK: hide from jedi
if TYPE_CHECKING:
    del Number
    del MaybeAwaitable
    del MaybeAwaitableTuple