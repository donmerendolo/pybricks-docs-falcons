# SPDX-License-Identifier: MIT
# SPDX-License-Identifier: PSF-2.0
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/builtins.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors
#
# Portions of the documentation copied from:
# https://docs.python.org/3/library/builtins.html
# https://docs.python.org/3/library/constants.html
# https://docs.python.org/3/library/stdtypes.html
# https://docs.python.org/3/library/exceptions.html
# Copyright (c) 2001-2021 Python Software Foundation

"""
Las siguientes funciones y excepciones se pueden usar sin importar nada.

La mayoría de las funciones y clases en este módulo no aceptan argumentos de palabra clave.
"""

from typing import (
    Any,
    Callable,
    Dict,
    Hashable,
    Iterable,
    Iterator,
    List,
    Literal,
    Mapping,
    Sequence,
    SupportsComplex,
    SupportsFloat,
    SupportsInt,
    Tuple,
    TypeVar,
    Union,
    overload,
)

import uio
import usys


# These get overridden later on, but we still want to use the originals
# for the purpose of typing the doc strings.
_bool = bool
_bytearray = bytearray
_bytes = bytes
_callable = callable
_classmethod = classmethod
_complex = complex
_dict = dict
_float = float
_int = int
_str = str
_type = type

_Self = TypeVar("_Self")

# Functions and types


def abs(x: Any) -> Any:
    """abs(x) -> Any

    Devuelve el valor absoluto de un número.

    El argumento puede ser un entero, un
    número de punto flotante, o cualquier objeto que implemente ``__abs__()``.
    Si el argumento es un número complejo, se devuelve su magnitud.

    Arguments:
        x (Any): El valor.

    Returns:
        Valor absoluto de ``x``.
    """


def all(x: Iterable) -> _bool:
    """all(x) -> bool

    Comprueba si todos los elementos del iterable son verdaderos.

    Equivalente a::

        def all(x):
            for element in x:
                if not element:
                    return False
            return True

    Arguments:
        x (Iterable): El iterable a comprobar.

    Returns:
        ``True`` si el iterable ``x`` está vacío o si todos los elementos
        son verdaderos. De lo contrario ``False``.
    """


def any(x: Iterable) -> _bool:
    """any(x) -> bool

    Comprueba si al menos un elemento del iterable es verdadero.

    Equivalente a::

        def any(x):
            for element in x:
                if element:
                    return True
            return False

    Arguments:
        x (Iterable): El iterable a comprobar.

    Returns:
        ``True`` si al menos un elemento en ``x`` es verdadero. De lo contrario ``False``.
    """


def bin(x: Any) -> _str:
    """bin(x) -> str

    Convierte un entero a su representación binaria. El resultado es una
    cadena con prefijo ``0b``. El resultado es una expresión válida de Python.
    Por ejemplo, ``bin(5)`` da ``"0b101"``.

    Arguments:
        x (int): Valor a convertir.

    Returns:
        Una cadena que representa la forma binaria de la entrada.
    """


class bool:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, x: Any) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        bool(​)
        bool(x)

        Crea un valor booleano, que es ``True`` o ``False``.

        El valor de entrada se convierte usando el procedimiento estándar de 
        prueba de verdad. Si no se proporciona entrada, se asume que es ``False``.

        Arguments:
            x: Valor a convertir.

        Returns:
            Resultado de la prueba de verdad.
        """


class bytes:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, source: _int) -> None:
        ...

    @overload
    def __init__(self, source: Union[_bytes, _bytearray, Iterable[_int]]) -> None:
        ...

    @overload
    def __init__(self, source: _str, encoding: _str) -> None:
        ...

    def __init__(self, *args):
        r"""
        bytes(​)
        bytes(integer)
        bytes(iterable)
        bytes(string, encoding)

        Crea un nuevo objeto ``bytes``, que es una secuencia de enteros
        en el rango :math:`0 \leq x \leq 255`. Este objeto es *inmutable*,
        lo que significa que *no puedes* cambiar su contenido después de crearlo.

        Si no se proporciona ningún argumento, esto crea un objeto ``bytes`` vacío.

        Arguments:
            integer (int): Si el argumento es un solo entero, esto crea
              un objeto ``bytes`` de ceros. El argumento especifica cuántos.
            iterable (iter): Si el argumento es un ``bytearray``, objeto ``bytes``
              u otro iterable de enteros, esto crea un objeto ``bytes``
              con la misma secuencia de bytes que el argumento.
            string (str): Si el argumento es una cadena, esto crea un objeto ``bytes``
              que contiene la cadena codificada.
            encoding (str): Especifica qué codificación usar para el argumento ``string``.
              Solo se admite ``"utf-8"``.
        """


class bytearray:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, source: _int) -> None:
        ...

    @overload
    def __init__(self, source: Union[_bytes, _bytearray, _str, Iterable[_int]]) -> None:
        ...

    def __init__(self, *args):
        r"""
        bytearray(​)
        bytearray(integer)
        bytearray(iterable)
        bytearray(string)

        Crea un nuevo objeto ``bytearray``, que es una secuencia de enteros
        en el rango :math:`0 \leq x \leq 255`. Este objeto es *mutable*, lo que
        significa que *puedes* cambiar su contenido después de crearlo.

        Si no se proporciona ningún argumento, esto crea un objeto ``bytearray`` vacío.

        Arguments:
            integer (int): Si el argumento es un solo entero, esto crea
              un objeto ``bytearray`` de ceros. El argumento especifica cuántos.
            iterable (iter): Si el argumento es un ``bytearray``, objeto ``bytes``
              u otro iterable de enteros, esto crea un objeto ``bytearray``
              con la misma secuencia de bytes que el argumento.
            string (str): Si el argumento es una cadena, esto crea
              un objeto ``bytearray`` que contiene la cadena codificada.
        """


def callable(object: Any) -> _bool:
    """
    callable(object) -> bool

    Comprueba si un objeto es invocable.

    Arguments:
        object: Objeto a comprobar.

    Returns:
        ``True`` si el argumento objeto parece invocable, ``False`` si no.
    """


def chr(x: _int) -> _str:
    """chr(x) -> str

    Devuelve la cadena que representa un carácter cuyo código Unicode es el
    entero ``x``. Esta es la inversa de :meth:`ord`. Por
    ejemplo, ``chr(97)`` da ``"a"``.

    Arguments:
        x (int): Valor a convertir (0-255).

    Returns:
        Una cadena con un carácter, correspondiente al valor Unicode dado.
    """


def classmethod(method: _callable) -> _callable:
    """
    Transforma un método en un método de clase.
    """


class complex:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(
        self, real: Union[_float, SupportsFloat, _complex, SupportsComplex]
    ) -> None:
        ...

    @overload
    def __init__(
        self,
        real: Union[_float, SupportsFloat, _complex, SupportsComplex],
        imag: Union[_float, SupportsFloat, _complex, SupportsComplex],
    ) -> None:
        ...

    @overload
    def __init__(self, value: _str) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        complex(string)
        complex(a=0, b=0)

        Crea un número complejo a partir de una cadena o de un par de números.

        Si se proporciona una cadena, debe ser de la forma ``'1+2j'``.
        Si se proporciona un par de números, el resultado se calcula
        como: ``a + b * j``.

        Arguments:
            string (str): Una cadena de la forma ``'1+2j'``.
            a (float or complex): Un número de valor real o complejo.
            b (float or complex): Un número de valor real o complejo.

        Returns:
            El número complejo resultante.
        """


class dict:
    @overload
    def __init(self) -> None:
        ...

    @overload
    def __init(self, **kwargs) -> None:
        ...

    def __init__(self, *args, **kwargs) -> None:
        """
        dict(**kwargs)
        dict(mapping, **kwargs)
        dict(iterable, **kwargs)

        Crea un objeto diccionario.

        Consulta la
        `documentación estándar de Python
        <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_
        para una referencia completa con ejemplos.
        """


@overload
def dir() -> List[_str]:
    ...


@overload
def dir(object: Any) -> List[_str]:
    ...


def dir(*args) -> List[_str]:
    """
    dir() -> List[str]
    dir(object) -> List[str]

    Obtiene una lista de los atributos de un objeto.

    Si no se proporciona un argumento de objeto, esta función obtiene la lista de nombres
    en el ámbito local actual.

    Arguments:
        object: Objeto del cual comprobar atributos válidos.

    Returns:
        Lista de atributos del objeto o lista de nombres en el ámbito local actual.
    """


@overload
def divmod(a: _int, b: _int) -> Tuple[_int, _int]:
    ...


@overload
def divmod(a: _float, b: _float) -> Tuple[_float, _float]:
    ...


def divmod(a, b):
    """
    divmod(a, b) -> Tuple[int, int]

    Obtiene el cociente y el resto al dividir dos enteros.

    Consulta la `documentación estándar de divmod de Python
    <https://docs.python.org/3/library/functions.html#divmod>`_ para
    el comportamiento esperado cuando ``a`` o ``b`` son números de punto flotante
    en su lugar.

    Arguments:
        a (int): Numerador.
        b (int): Denominador.

    Returns:
        Una tupla con el cociente ``a // b`` y el resto ``a % b``.
    """


class enumerate:
    @overload
    def __init__(self, iterable: Iterable) -> None:
        ...

    @overload
    def __init__(self, iterable: Iterable, start: _int) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        enumerate(iterable, start=0)

        Enumera un iterador existente agregando un índice numérico.

        Esta función es equivalente a::

            def enumerate(sequence, start=0):
                n = start
                for elem in sequence:
                    yield n, elem
                    n += 1
        """


@overload
def eval(expression: _str) -> Any:
    ...


@overload
def eval(expression: _str, globals: _dict) -> Any:
    ...


@overload
def eval(expression: _str, globals: _dict, locals: Mapping) -> Any:
    ...


def eval(*args):
    """
    eval(expression) -> Any
    eval(expression, globals) -> Any
    eval(expression, globals, locals) -> Any

    Evalúa el resultado de una expresión.

    Los errores de sintaxis se reportan como excepciones.

    Arguments:
        expression (str): Expresión de la cual evaluar el resultado.
        globals (dict): Si se proporciona, esto controla qué funciones están disponibles
            para usar en la expresión. Por defecto, el ámbito global es accesible.
        locals (dict): Si se proporciona, esto controla qué funciones están disponibles
            para usar en la expresión. Por defecto es el mismo que ``globals``.

    Returns:
        El valor obtenido al ejecutar la expresión.
    """


@overload
def exec(object: Any) -> None:
    ...


@overload
def exec(object: Any, globals: _dict) -> None:
    ...


@overload
def exec(object: Any, globals: _dict, locals: Mapping) -> None:
    ...


def exec(*args):
    """
    exec(expression)
    exec(expression, globals)
    exec(expression, globals, locals)

    Ejecuta código de MicroPython.

    Los errores de sintaxis se reportan como excepciones.

    Arguments:
        expression (str): Código a ejecutar.
        globals (dict): Si se proporciona, esto controla qué funciones están disponibles
            para usar en la expresión. Por defecto, el ámbito global es accesible.
        locals (dict): Si se proporciona, esto controla qué funciones están disponibles
            para usar en la expresión. Por defecto es el mismo que ``globals``.
    """


class float:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, x: _int) -> None:
        ...

    @overload
    def __init__(self, x: SupportsFloat) -> None:
        ...

    @overload
    def __init__(self, x: _str) -> None:
        ...

    def __init__(self, *args) -> None:
        """float(x=0.0)

        Crea un número de punto flotante a partir de un objeto dado.

        Arguments:
            x (int or float or str): Número o cadena a convertir.
        """


@overload
def getattr(object: Any, name: _str) -> Any:
    ...


@overload
def getattr(object: Any, name: _str, default: Any) -> Any:
    ...


def getattr(*args):
    """
    getattr(object, name) -> Any
    getattr(object, name, default) -> Any

    Busca el atributo llamado ``name`` en el ``object`` dado.

    Arguments:
        object: Objeto en el cual buscar el atributo.
        name (str): Nombre del atributo.
        default: Objeto a devolver si el atributo no se encuentra.

    Returns:
        Devuelve el valor del atributo nombrado.
    """


def globals() -> Dict[_str, Any]:
    """
    globals() -> dict

    Obtiene un diccionario que representa la tabla de símbolos global actual.

    Returns:
        El diccionario de globales.
    """


def hasattr(object: Any, name: _str) -> _bool:
    """
    hasattr(object, name) -> bool

    Comprueba si un atributo existe en un objeto.

    Arguments:
        object: Objeto en el cual buscar el atributo.
        name (str): Nombre del atributo.

    Returns:
        ``True`` si existe un atributo con ese nombre, ``False`` si no.
    """


def hash(object: Any) -> _int:
    """
    hash(object) -> int

    Obtiene el valor hash de un objeto, si el objeto lo admite.

    Arguments:
        object: Objeto del cual obtener un valor hash.

    Returns:
        El valor hash.
    """


@overload
def help() -> None:
    ...


@overload
def help(object: Any) -> None:
    ...


def help(*args) -> None:
    """
    help()
    help(object)

    Obtiene información sobre un objeto.

    Si no se proporcionan argumentos, esta función imprime instrucciones para operar el
    REPL. Si el argumento es ``"modules"``, imprime los módulos disponibles.

    Arguments:
        object: Objeto del cual imprimir información de ayuda.
    """


def hex(x: int) -> _str:
    """hex(x) -> str

    Convierte un entero a su representación hexadecimal. El resultado es una
    cadena en minúsculas con prefijo ``0x``. El resultado es una expresión válida
    de Python. Por ejemplo, ``hex(25)`` da ``"0x19"``.

    Arguments:
        x (int): Valor a convertir.

    Returns:
        Una cadena que representa la forma hexadecimal de la entrada.
    """


def id(object: Any) -> _int:
    """
    id(object) -> int

    Obtiene la *identidad* de un objeto. Este es un entero que se garantiza
    que es único y constante para este objeto durante su vida útil.

    Arguments:
        object: Objeto del cual obtener el identificador.

    Returns:
        El identificador.
    """


@overload
def input() -> _str:
    ...


@overload
def input(prompt: _str) -> _str:
    ...


def input(*args) -> _str:
    """input() -> str
    input(prompt) -> str

    Obtiene entrada del usuario en la ventana del terminal. Espera hasta
    que el usuario presione :kbd:`Enter`.

    Arguments:
        prompt (str): Si se proporciona, esto se imprime primero en la ventana del terminal.
            Esto se puede usar para hacer una pregunta para que el usuario sepa qué escribir.

    Returns:
        Todo lo que el usuario escribió antes de presionar :kbd:`Enter`.
    """


class int:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, x: _str) -> None:
        ...

    @overload
    def __init__(self, x: _str, base: _int) -> None:
        ...

    @overload
    def __init__(self, x: Union[_int, SupportsInt]) -> None:
        ...

    def __init__(self, *args) -> None:
        """int(x=0)

        Crea un entero.

        Arguments:
            x (int or float or str): Objeto a convertir.
        """

    def to_bytes(self, length: _int, byteorder: Literal["little", "big"]) -> _bytes:
        """
        to_bytes(length, byteorder) -> bytes

        Obtiene una representación en :class:`bytes` del entero.

        Arguments:
            length (int): Cuántos bytes usar.
            byteorder (str): Elige ``"big"`` para poner el byte más significativo
                primero. Elige ``"little"`` para poner el byte menos significativo
                primero.

        Returns:
            Secuencia de bytes que representa el entero.
        """

    @_classmethod
    def from_bytes(cls, _bytes: _bytes, byteorder: Literal["little", "big"]) -> _int:
        """from_bytes(bytes, byteorder) -> int

        Convierte una secuencia de bytes al número que representa.

        Arguments:
            bytes (bytes): Los bytes a convertir.
            byteorder (str): Elige ``"big"`` si el byte más significativo es
                el primer elemento. Elige ``"little"`` si el byte menos significativo
                es el primer elemento.

        Returns:
            El número representado por los bytes.
        """


def isinstance(object: Any, classinfo: Union[_type, Tuple[_type]]) -> _bool:
    """
    isinstance(object, classinfo) -> bool

    Comprueba si un objeto es una instancia de una cierta clase.

    Arguments:
        object: Objeto del cual comprobar el tipo.
        classinfo (type or tuple): Información de clase.

    Returns:
        ``True`` si el argumento ``object`` es una instancia del argumento ``classinfo``,
        o de una subclase del mismo.
    """


def issubclass(cls: _type, classinfo: Union[_type, Tuple[_type]]) -> _bool:
    """
    issubclass(cls, classinfo) -> bool

    Comprueba si una clase es una subclase de otra clase.

    Arguments:
        cls: Tipo de clase.
        classinfo (type or tuple): Información de clase.

    Returns:
        ``True`` si ``cls`` es una subclase de ``classinfo``.
    """


def iter(object: Union[Iterable, Sequence]) -> Iterator:
    """
    iter(object) -> Iterator

    Obtiene el iterador del objeto si está disponible.

    Arguments:
        object: Objeto del cual obtener el iterador.

    Returns:
        El iterador.
    """


def len(s: Sequence) -> _int:
    """
    len(s) -> int

    Obtiene la longitud (el número de elementos) de un objeto.

    Arguments:
        s (Sequence): La secuencia de la cual obtener la longitud.

    Returns:
        La longitud.
    """


class list:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, iterable: Iterable) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        list(​)
        list(iterable)

        Crea una nueva lista. Si no se proporciona ningún argumento, esto crea un
        objeto ``list`` vacío.

        Una lista es *mutable*, lo que significa que *puedes* cambiar su contenido
        después de crearla.

        Arguments:
            iterable (iter): Iterable a partir del cual construir la lista.
        """


def locals() -> _dict:
    """
    locals() -> dict

    Obtiene un diccionario que representa la tabla de símbolos local actual.

    Returns:
        El diccionario de locales.
    """


def map(function: Callable, iterable: Iterable, *args: Any) -> Iterator:
    """
    map(function, iterable) -> Iterator
    map(function, iterable1, iterable2...) -> Iterator

    Crea un nuevo iterador que aplica la función dada a cada elemento del
    iterable dado y devuelve los resultados.

    Arguments:
        function (callable): Función que calcula un resultado para un elemento del
            iterable(s). El número de argumentos de esta función debe coincidir
            con el número de iterables dados.
        iterable (iter): Uno o más iterables fuente de los cuales extraer datos.
            Con múltiples iterables, el iterador se detiene cuando el iterable
            más corto se agota.

    Returns:
        El nuevo iterador mapeado.
    """


@overload
def max(iterable: Iterable) -> Any:
    ...


@overload
def max(arg1: Any, arg2: Any, *args: Any) -> Any:
    ...


def max(*args):
    """
    max(iterable) -> Any
    max(arg1, arg2, ....) -> Any

    Obtiene el objeto con el mayor valor.

    El argumento puede ser un solo iterable, o cualquier número de objetos.

    Returns:
        El objeto con el mayor valor.
    """


@overload
def min(iterable: Iterable) -> Any:
    ...


@overload
def min(arg1: Any, arg2: Any, *args: Any) -> Any:
    ...


def min(*args):
    """
    min(iterable) -> Any
    min(arg1, arg2, ....) -> Any

    Obtiene el objeto con el menor valor.

    El argumento puede ser un solo iterable, o cualquier número de objetos.

    Returns:
        El objeto con el menor valor.
    """


def next(iterator: Iterator) -> Any:
    """
    next(iterator) -> Any

    Recupera el siguiente elemento del iterador llamando a su método ``__next__()``.

    Arguments:
        iterator (iter): Objeto generador inicializado del cual extraer el siguiente
            valor.

    Returns:
        El siguiente valor del generador.
    """


class object:
    def __init__(self) -> None:
        """
        Crea un nuevo objeto sin características.
        """


def oct(x: _int) -> _str:
    """oct(x) -> str

    Convierte un entero a su representación octal. El resultado es una
    cadena con prefijo ``0o``. El resultado es una expresión válida
    de Python. Por ejemplo, ``oct(25)`` da ``"0o31"``.

    Arguments:
        x (int): Valor a convertir.

    Returns:
        Una cadena que representa la forma octal de la entrada.
    """


# .. function:: open()


def ord(c: _str) -> _int:
    """ord(c) -> int

    Convierte una cadena que consiste en un carácter Unicode al
    número correspondiente. Esta es la inversa de :meth:`chr`.

    Arguments:
        c (str): Carácter a convertir.

    Returns:
        Número que representa el carácter (0--255).
    """


def pow(base: Union[_int, _float], exp: Union[_int, _float]) -> Union[_int, _float]:
    """
    pow(base, exp) -> Number

    Eleva la base al exponente dado: :math:`\\text{base}^{\\mathrm{exp}}`.

    Esto es lo mismo que hacer ``base ** exp``.

    Arguments:
        base (Number): La base.
        exp (Number): El exponente.

    Returns:
        El resultado.
    """


@overload
def print(*objects):
    ...


@overload
def print(*objects, sep: _str = " ", end: _str = "\n", file: uio.FileIO = usys.stdin):
    ...


def print(*args):
    """print(*objects, sep=" ", end="\\n", file=usys.stdin)

    Imprime texto u otros objetos en la ventana del terminal.

    Arguments:
        objects: Cero o más objetos a imprimir.

    Keyword Arguments:
        sep (str): Esto se imprime entre objetos, si hay más de uno.
        end (str): Esto se imprime después del último objeto.
        file (FileIO): Por defecto, el resultado se imprime en la ventana del terminal. Este
              argumento te permite imprimirlo en un archivo en su lugar, si los archivos están
              soportados.
    """


class range:
    @overload
    def __init__(self, stop: _int) -> None:
        ...

    @overload
    def __init__(self, start: _int, stop: _int) -> None:
        ...

    @overload
    def __init__(self, start: _int, stop: _int, step: _int) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        range(stop)
        range(start, stop)
        range(start, stop, step)

        Crea un generador que produce valores desde ``start`` hasta
        ``stop``, con incrementos de ``step``.

        Arguments:
            start (int): Valor inicial. Por defecto es ``0`` si solo se proporciona un argumento.
            stop (int): Punto final. Este valor *no* está incluido.
            step (int): Incremento entre valores. Por defecto es ``1`` si solo se proporcionan
                uno o dos argumentos.
        """


def repr(x: Any) -> _str:
    """repr(object) -> str

    Obtiene la cadena que representa un objeto.

    Arguments:
        x (object): Objeto a convertir.

    Returns:
        Representación en cadena implementada por el método ``__repr__`` del objeto.
    """


def reversed(seq: Sequence) -> Iterator:
    """
    reversed(seq) -> Iterator

    Obtiene un iterador que produce los valores de la secuencia en reversa, si
    está soportado.

    Arguments:
        seq: Secuencia de la cual extraer muestras.

    Returns:
        Iterador que produce valores en orden inverso, comenzando con el último valor.
    """


@overload
def round(number: _float) -> _int:
    ...


@overload
def round(number: _float, ndigits: _int) -> _float:
    ...


def round(*args):
    """
    round(number) -> int
    round(number, ndigits) -> float

    Redondea un número a un número dado de dígitos después del punto decimal.

    Si se omite ``ndigits`` o es ``None``, devuelve el entero más cercano.

    El redondeo con uno o más dígitos después del punto decimal no siempre
    truncará los ceros finales. Para imprimir números bien, formatea cadenas en su lugar::

        # imprimir dos decimales
        print('my number: %.2f' % number)
        print('my number: {:.2f}'.format(number))
        print(f'my number: {number:.2f}')

    Arguments:
        number (float): El número a redondear.
        ndigits (int): El número de dígitos restantes después del punto decimal.
    """


class set:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, iterable: Iterable[Hashable]) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        set()
        set(iterable)

        Crea un nuevo conjunto.

        Sin argumentos, crea un nuevo conjunto vacío, de lo contrario crea un conjunto
        que contiene elementos únicos de *iterable*.

        Los conjuntos también se pueden crear usando un literal de conjunto::

            my_set = {1, 2, 3}

        Los elementos de un conjunto deben ser hashables. Solo hay unos pocos tipos, como
        :class:`list` que no son hashables.

        Args:
            iterable: Un iterable de objetos hashables.
        """

    def copy(self: _Self) -> _Self:
        """
        copy() -> set

        Devuelve una copia superficial del conjunto.

        Returns:
            Un nuevo conjunto.
        """

    def difference(self: _Self, *others: set) -> _Self:
        """
        difference(other1, other2, ...) -> set

        Devuelve un nuevo conjunto con elementos que no están en ninguno de los otros conjuntos.

        La diferencia también se puede calcular usando el operador ``-``::

            diff = s - other

        Args:
            others: 1 o más otros conjuntos.

        Returns:
            Un nuevo conjunto.
        """

    def intersection(self: _Self, *others: set) -> _Self:
        """
        intersection(other1, other2, ...) -> set

        Devuelve un nuevo conjunto con elementos que son comunes entre este conjunto y
        todos los otros conjuntos.

        La intersección también se puede calcular usando el operador ``&``::

            intersect = s & other

        Args:
            others: 1 o más otros conjuntos.

        Returns:
            Un nuevo conjunto.
        """

    def isdisjoint(self, other: set) -> bool:
        """
        isdisjoint(other) -> bool

        Prueba si un conjunto y *other* no tienen elementos en común.

        Args:
            other: Otro conjunto.

        Returns:
            ``True`` si este conjunto no tiene elementos en común con *other*,
            de lo contrario ``False``.
        """

    def issubset(self, other: set) -> bool:
        """
        issubset(other) -> bool

        Prueba si un conjunto es un subconjunto de *other*.

        La prueba también se puede realizar usando el operador ``<=``::

            if s <= other:
                # s es subconjunto de other
                ...

        Args:
            other: Otro conjunto.

        Returns:
            ``True`` si este conjunto es un subconjunto de *other*, de lo contrario ``False``.
        """

    def issuperset(self, other: set) -> bool:
        """
        issuperset(other) -> bool

        Prueba si un conjunto es un superconjunto de *other*.

        La prueba también se puede realizar usando el operador ``>=``::

            if s >= other:
                # s es superconjunto de other
                ...

        Args:
            other: Otro conjunto.

        Returns:
            ``True`` si este conjunto es un superconjunto de *other*, de lo contrario ``False``.
        """

    def symmetric_difference(self: _Self, other: set) -> _Self:
        """
        symmetric_difference(other) -> bool

        Devuelve un nuevo conjunto con elementos en un conjunto o en el otro pero no en ambos.

        La diferencia simétrica también se puede calcular usando el operador ``^``::

            diff = s ^ other

        Args:
            other: Otro conjunto.

        Returns:
            Un nuevo conjunto.
        """

    def union(self: _Self, *others: set) -> _Self:
        """
        union(other1, other2, ...) -> set

        Devuelve un nuevo conjunto con elementos de este conjunto y de todos los otros conjuntos.

        La unión también se puede calcular usando el operador ``|``::

            u = s | other

        Args:
            others: 1 o más otros conjuntos.

        Returns:
            Un nuevo conjunto.
        """

    def __contains__(self, item: Hashable) -> bool:
        ...

    def __len__(self) -> int:
        ...

    def __bool__(self) -> bool:
        ...

    def __gt__(self, other: set) -> bool:
        ...

    def __lt__(self, other: set) -> bool:
        ...

    def __ge__(self, other: set) -> bool:
        ...

    def __le__(self, other: set) -> bool:
        ...

    def __eq__(self, other: set) -> bool:
        ...

    def __ne__(self, other: set) -> bool:
        ...

    def __sub__(self: _Self, other: set) -> _Self:
        ...

    def __and__(self: _Self, other: set) -> _Self:
        ...

    def __or__(self: _Self, other: set) -> _Self:
        ...

    def __xor__(self: _Self, other: set) -> _Self:
        ...


def setattr(object: Any, name: _str, value: Any) -> None:
    """
    setattr(object, name, value)

    Asigna un valor a un atributo, siempre que el objeto lo permita.

    Esta es la contraparte de :meth:`getattr`.

    Arguments:
        object: Objeto en el cual almacenar el atributo.
        name (str): Nombre del atributo.
        value: Valor a almacenar.
    """


class slice:
    @overload
    def __init__(self, stop: _int) -> None:
        ...

    @overload
    def __init__(self, start: _int, stop: _int) -> None:
        ...

    @overload
    def __init__(self, start: _int, stop: _int, step: _int) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        slice(​)

        No se admite la creación de instancias de esta clase.

        Usa la sintaxis de indexación en su lugar. Por
        ejemplo: ``a[start:stop:step]`` o ``a[start:stop, i]``.
        """


def sorted(iterable: Iterable, key=None, reverse=False) -> List:
    """
    Ordena objetos.

    Arguments:
        iterable (iter): Objetos a ordenar. Esto también puede ser un generador que
            produce un número finito de objetos.
        key (callable): Función ``def(item) -> int`` que mapea un objeto a un
            valor numérico. Esto se usa para determinar el orden de los elementos
            ordenados.
        reverse (bool): Si ordenar en reversa, poniendo el valor más alto
            primero.


    Returns:
        Una nueva lista con los elementos ordenados.
    """


def staticmethod(method: _callable) -> _callable:
    """
    Transforma un método en un método estático.
    """


class str:
    @overload
    def __init__(self, object: Any = "") -> None:
        ...

    @overload
    def __init__(
        self, object: _bytes = b"", encoding: _str = "utf-8", errors: _str = "strict"
    ) -> None:
        ...

    def __init__(self) -> None:
        """
        str(​)
        str(object)
        str(object, encoding)

        Obtiene la representación en cadena de un objeto.

        Si no se proporciona ningún argumento, esto crea un objeto ``str`` vacío.

        Arguments:
            object: Si solo se proporciona este argumento, esto devuelve la representación
              en cadena del objeto.
            encoding (str): Si el primer argumento es un objeto ``bytearray`` o ``bytes``
              y el argumento de codificación es ``"utf-8"``, esto decodificará
              los datos de bytes para obtener una representación en cadena.
        """


@overload
def sum(iterable: Iterable) -> _int:
    ...


@overload
def sum(iterable: Iterable, start: _int) -> _int:
    ...


def sum(*args):
    """
    sum(iterable) -> Number
    sum(iterable, start) -> Number

    Suma los elementos del iterable y el valor inicial.

    Arguments:
        iterable (iter): Valores a sumar, comenzando con el primer valor.
        start (Number): Valor agregado al total.

    Returns:
        La suma total.
    """


@overload
def super() -> _type:
    ...


@overload
def super(type: _type) -> _type:
    ...


@overload
def super(type: _type, object_or_type: Any) -> _type:
    ...


def super(*args):
    """
    super() -> type
    super(type) -> type
    super(type, object_or_type) -> type

    Obtiene un objeto que delega llamadas de método a un padre, o a una clase hermana
    del tipo dado.

    Returns:
        El objeto `super()` correspondiente.
    """


class tuple:
    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, iterable: Iterable):
        ...

    def __init__(self, *args) -> None:
        """
        tuple(​)
        tuple(iterable)

        Crea una nueva tupla. Si no se proporciona ningún argumento, esto crea un
        objeto ``tuple`` vacío.

        Una tupla es *inmutable*, lo que significa que *no puedes* cambiar su
        contenido después de crearla.

        Arguments:
            iterable (iter): Iterable a partir del cual construir la tupla.
        """


class type:
    def __init__(self, object: Any) -> None:
        """type(object)

        Obtiene el tipo de un objeto. Esto se puede usar para verificar si un objeto
        es una instancia de una clase particular.

        Arguments:
            object: Objeto del cual comprobar el tipo.
        """


def zip(*iterables: Iterable) -> Iterable[Tuple]:
    """
    zip(iter_a, iter_b, ...) -> Iterable[Tuple]

    Devuelve un iterador de tuplas, donde la *i*-ésima tupla contiene el *i*-ésimo
    elemento de cada una de las secuencias o iterables del argumento. El iterador
    se detiene cuando el iterable de entrada más corto se agota.

    Con un solo argumento iterable, devuelve un iterador de tuplas de 1 elemento.
    Sin argumentos, devuelve un iterador vacío.

    Esta funcionalidad es equivalente a::

        def zip(*iterables):
            sentinel = object()
            iterators = [iter(it) for it in iterables]
            while iterators:
                result = []
                for it in iterators:
                    elem = next(it, sentinel)
                    if elem is sentinel:
                        return
                    result.append(elem)
                yield tuple(result)

    Arguments:
        iter_a (iter): El primer iterable. Este proporciona el primer valor para
            cada una de las tuplas producidas.
        iter_b (iter): El segundo iterable. Este proporciona el segundo valor en
            cada una de las tuplas producidas. Y así sucesivamente.

    Returns:
        Un nuevo iterador que produce tuplas que contienen los valores de los
        iterables individuales.
    """


# base exceptions


class BaseException:
    """
    La clase base para todas las excepciones integradas.

    No está destinada a ser heredada directamente por clases definidas por el usuario (para eso,
    usa :class:`Exception`).
    """

    args: Tuple
    """
    La tupla de argumentos dados al constructor de la excepción.
    """


class Exception(BaseException):
    """
    Todas las excepciones integradas se derivan de esta clase.

    Todas las excepciones definidas por el usuario también deben derivarse de esta clase.
    """


class ArithmeticError(Exception):
    """
    La clase base para aquellas excepciones integradas que se lanzan para varios
    errores aritméticos.
    """


class LookupError(Exception):
    """
    La clase base para las excepciones que se lanzan cuando una clave o índice usado
    en un mapeo o secuencia es inválido.
    """


# concrete exceptions


class AssertionError(Exception):
    """
    Se lanza cuando falla una declaración assert.
    """


class AttributeError(Exception):
    """
    Se lanza cuando falla una referencia o asignación de atributo.
    """


class EOFError(Exception):
    """
    Se lanza cuando la función :meth:`input` encuentra una condición de fin de archivo (EOF)
    sin leer ningún dato.
    """


class GeneratorExit(BaseException):
    """
    Se lanza cuando un generador o corrutina se cierra.
    """


class ImportError(Exception):
    """
    Se lanza cuando la declaración ``import`` no puede cargar un módulo.
    """


class IndentationError(SyntaxError):
    """
    Clase base para errores de sintaxis relacionados con indentación incorrecta.
    """


class IndexError(LookupError):
    """
    Se lanza cuando un subíndice de secuencia está fuera de rango.
    """


class KeyError(LookupError):
    """
    Se lanza cuando una clave de mapeo (diccionario) no se encuentra en el conjunto de claves existentes.
    """


class KeyboardInterrupt(BaseException):
    """
    Se lanza cuando el usuario presiona la tecla de interrupción (normalmente :kbd:`Ctrl` :kbd:`C`).
    """


class MemoryError(Exception):
    """
    Se lanza cuando una operación se queda sin memoria.
    """


class NameError(Exception):
    """
    Se lanza cuando no se encuentra un nombre local o global.
    """


class NotImplementedError(RuntimeError):
    """
    En clases base definidas por el usuario, los métodos abstractos deben lanzar esta excepción
    cuando requieren que las clases derivadas sobrescriban el método, o mientras la
    clase está siendo desarrollada para indicar que la implementación real aún
    necesita ser agregada.
    """


class OSError(Exception):
    """
    Esta excepción es lanzada por el firmware, que es
    el Sistema Operativo que se ejecuta en el hub.
    Por :ref:`ejemplo <device_detection>`, lanza
    un ``OSError`` si llamas a ``Motor(Port.A)`` cuando no hay un
    motor en el puerto A.
    """

    errno: _int
    """
    Especifica qué tipo de ``OSError`` ocurrió, como se lista en el
    módulo :mod:`uerrno`.
    """


class OverflowError(ArithmeticError):
    """
    Se lanza cuando el resultado de una operación aritmética es demasiado grande para ser representado.
    """


class RuntimeError(Exception):
    """
    Se lanza cuando se detecta un error que no cae en ninguna de las otras categorías.

    El valor asociado es una cadena que indica qué salió mal exactamente.
    """


class StopIteration(Exception):
    """
    Lanzada por la función integrada :meth:`next` y el método ``__next__()`` de un iterador
    para señalar que no hay más elementos producidos por el iterador.

    Las funciones generadoras deben retornar en lugar de lanzar esto directamente.
    """


class SyntaxError(Exception):
    """
    Se lanza cuando el analizador encuentra un error de sintaxis.
    """


class SystemExit(BaseException):
    """
    Se lanza cuando presionas el botón de parar en el hub o en la aplicación Pybricks Code.
    """


class TypeError(Exception):
    """
    Se lanza cuando se aplica una operación o función a un objeto de tipo inapropiado.
    """


class ValueError(Exception):
    """
    Se lanza cuando una operación o función recibe un argumento que tiene el tipo
    correcto pero un valor inapropiado. Esto se usa cuando la situación
    no está descrita por una excepción más precisa como :class:`IndexError`.
    """


class ZeroDivisionError(ArithmeticError):
    """
    Se lanza cuando el segundo argumento de una división o operación de módulo es cero.
    """