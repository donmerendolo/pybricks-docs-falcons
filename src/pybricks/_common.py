# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""Módulo genérico multiplataforma para dispositivos típicos como luces, pantallas,
altavoces y baterías."""

from __future__ import annotations

from typing import (
    Union,
    Iterable,
    overload,
    Optional,
    Tuple,
    Collection,
    Set,
    TYPE_CHECKING,
)

from .tools import Matrix
from .parameters import Axis, Direction, Stop, Button, Port, Color, Side

if TYPE_CHECKING:
    from typing import Any, Awaitable, TypeVar

    from .parameters import Number

    _T_co = TypeVar("_T_co", covariant=True)

    class MaybeAwaitable(None, Awaitable[None]): ...

    # HACK: Cannot subclass bool, so using Any instead.
    class MaybeAwaitableBool(Any, Awaitable[bool]): ...

    class MaybeAwaitableFloat(float, Awaitable[float]): ...

    class MaybeAwaitableInt(int, Awaitable[int]): ...

    class MaybeAwaitableTuple(Tuple[_T_co], Awaitable[Tuple[_T_co]]): ...

    class MaybeAwaitableColor(Color, Awaitable[Color]): ...


class System:
    """Acciones de control del sistema para un hub."""

    def set_stop_button(
        self, button: Optional[Union[Button, Iterable[Button]]]
    ) -> None:
        """
        set_stop_button(button)

        Configura el botón o combinación de botones que detiene un script en ejecución.

        Normalmente, el botón central se usa para detener un script en ejecución. Puedes
        cambiar o deshabilitar este comportamiento para usar el botón con otros
        propósitos.

        Arguments:
            button (Button): Un botón como
                :attr:`Button.CENTER <pybricks.parameters.Button.CENTER>`,
                o una tupla de múltiples botones. Elige ``None`` para deshabilitar
                completamente el botón de detención. Si lo haces, aún puedes apagar el hub
                manteniendo presionado el botón central durante tres segundos.
        """

    def shutdown(self) -> None:
        """shutdown()

        Detiene el programa y apaga el hub."""

    @overload
    def storage(self, offset: int, *, read: int) -> bytes: ...

    @overload
    def storage(self, offset: int, *, write: bytes) -> None: ...

    def storage(self, offset, read=None, write=None):
        """
        storage(offset, write=)
        storage(offset, read=) -> bytes

        Lee o escribe datos binarios en almacenamiento persistente.

        Esto te permite almacenar datos que pueden usarse la próxima vez que ejecutes el
        programa.

        Los datos se guardarán en la memoria flash cuando apagues el hub
        normalmente. No se guardarán si retiras las baterías *mientras* el
        hub todavía está en encendido.

        Una vez guardados, los datos permanecerán disponibles incluso después de retirar las
        baterías.

        Arguments:
            offset (int): El desplazamiento desde el inicio de la memoria de almacenamiento del usuario, en bytes.
            read (int): El número de bytes a leer. Omite este argumento al escribir.
            write (bytes): Los bytes a escribir. Omite este argumento al leer.

        Returns:
            Los bytes leídos si se está leyendo, de lo contrario ``None``.

        Raises:
            ValueError:
                Si intentas leer o escribir datos fuera del rango permitido.
        """

    def reset_storage(self) -> None:
        """reset_storage()

        Restablece todas las configuraciones de usuario a los valores predeterminados y borra los programas de usuario.
        """

    def info(self) -> dict:
        """info() -> dict

        Obtiene información sobre el hub como un diccionario con las siguientes claves:

         - ``"name"``: El nombre del hub. Este es el nombre que ves al conectarte
           vía Bluetooth.
         - ``"reset_reason"``: Por qué el hub (re)inició. Es ``0`` si el hub
           se apagó previamente de forma normal. Es ``1`` si el hub se reinició
           automáticamente, como después de una actualización de firmware. Es ``2`` si el hub
           previamente falló debido a un timeout del watchdog, lo que indica un
           problema de firmware.
         - ``"host_connected_ble"``: ``True`` si el hub está conectado a un
           ordenador, tableta o teléfono vía Bluetooth, y ``False`` de lo contrario.
         - ``"program_start_type"``: Es ``1`` si el programa se inició
           automáticamente cuando el hub se encendió. Es ``2`` si el programa
           se inició con los botones del hub. Es ``3`` si el programa se
           inició desde tu computadora conectada.

        Returns:
            Un diccionario con información del sistema.
        """


class DCMotor:
    """Clase genérica para controlar motores simples sin sensores de rotación, como
    motores de tren."""

    def __init__(self, port: Port, positive_direction: Direction = Direction.CLOCKWISE):
        """__init__(port, positive_direction=Direction.CLOCKWISE)

        Arguments:
            port (Port): Puerto al que está conectado el motor.
            positive_direction (Direction): En qué dirección debe
                girar el motor cuando das un valor de ciclo de trabajo positivo.
        """

    def dc(self, duty: Number) -> None:
        """dc(duty)

        Hace girar el motor a un ciclo de trabajo dado (también conocido como "potencia").

        Arguments:
            duty (Number, %): El ciclo de trabajo (-100.0 a 100).
        """

    def stop(self) -> None:
        """stop()

        Detiene el motor y lo deja girar libremente.

        El motor se detiene gradualmente debido a la fricción."""

    def brake(self) -> None:
        """brake()

        Frena el motor pasivamente.

        El motor se detiene debido a la fricción, más el voltaje que
        se genera mientras el motor todavía está en movimiento."""

    @overload
    def settings(self, max_voltage: Number) -> None: ...

    @overload
    def settings(self) -> Tuple[int]: ...

    def settings(self, *args):
        """
        settings(max_voltage)
        settings() -> Tuple[int]

        Configura los ajustes del motor. Si no se dan argumentos,
        devuelve los valores actuales.

        Arguments:
            max_voltage (Number, mV):
                Voltaje máximo aplicado al motor durante todos los comandos del motor.
        """


class Control:
    """Clase para interactuar con el controlador PID y configuraciones."""

    scale: int

    """
    Factor de escala entre la variable entera controlada
    y la salida física. Por ejemplo, para un solo
    motor este es el número de pulsos del codificador por grado de rotación.
    """

    @overload
    def limits(
        self,
        speed: Optional[Number] = None,
        acceleration: Optional[Number] = None,
        torque: Optional[Number] = None,
    ) -> None: ...

    @overload
    def limits(self) -> Tuple[int, int, int]: ...

    def limits(self, *args):
        """
        limits(speed, acceleration, torque)
        limits() -> Tuple[int, int, int]

        Configura la velocidad, aceleración y par máximos.

        Si no se dan argumentos, devolverá los valores actuales.

        Los nuevos límites de ``acceleration`` y ``speed`` entrarán en efecto
        cuando des un nuevo comando al motor. Las maniobras en curso no se ven afectadas.

        Arguments:
            speed (Number, deg/s o Number, mm/s):
                Velocidad máxima. Todos los comandos de velocidad se limitarán a este valor.
            acceleration (Number, deg/s² o Number, mm/s²):
                Pendiente de la curva de velocidad al acelerar o desacelerar.
                Usa una tupla para configurar aceleración y desaceleración por separado.
                Si se da un valor, se usa para ambos.
            torque (:ref:`torque`):
                Par de retroalimentación máximo durante el control.
        """

    @overload
    def pid(
        self,
        kp: Optional[Number] = None,
        ki: Optional[Number] = None,
        kd: Optional[Number] = None,
        integral_deadzone: Optional[Number] = None,
        integral_rate: Optional[Number] = None,
    ) -> None: ...

    @overload
    def pid(self) -> Tuple[int, int, int, int, int]: ...

    def pid(self, *args):
        """pid(kp, ki, kd, integral_deadzone, integral_rate)
        pid() -> Tuple[int, int, int, int, int]

        Obtiene o configura los valores PID para el control de posición y velocidad.

        Si no se dan argumentos, esto retornará los valores actuales.

        Arguments:
            kp (int): Constante de control de posición proporcional. Es el par de
                retroalimentación por grado de
                error: µNm/deg.
            ki (int): Constante de control de posición integral. Es el par de
                retroalimentación por grado acumulado de error: µNm/(deg s).
            kd (int): Constante de control de posición derivativo (o velocidad proporcional).
                Es el par de retroalimentación por
                unidad de velocidad: µNm/(deg/s).
            integral_deadzone (Number, deg o Number, mm): Zona alrededor del
                objetivo donde la integral del error no acumula errores.
            integral_rate (Number, deg/s o Number, mm/s): Tasa máxima a la
                que se permite crecer la integral del error.
        """

    @overload
    def target_tolerances(
        self, speed: Optional[Number] = None, position: Optional[Number] = None
    ) -> None: ...

    @overload
    def target_tolerances(self) -> Tuple[int, int]: ...

    def target_tolerances(self, *args):
        """target_tolerances(speed, position)
        target_tolerances() -> Tuple[int, int]

        Obtiene o configura las tolerancias que indican cuándo una maniobra está completa.

        Si no se dan argumentos, esto retornará los valores actuales.

        Arguments:
            speed (Number, deg/s o Number, mm/s): Desviación permitida
                de velocidad cero antes de que el movimiento se considere completo.
            position (Number, deg o :ref:`distance`): Desviación
                permitida del objetivo antes de que el movimiento se considere
                completo.
        """

    @overload
    def stall_tolerances(
        self, speed: Optional[Number] = None, time: Optional[Number] = None
    ) -> None: ...

    @overload
    def stall_tolerances(self) -> Tuple[int, int]: ...

    def stall_tolerances(self, speed, time):
        """stall_tolerances(speed, time)
        stall_tolerances() -> Tuple[int, int]

        Obtiene o configura las tolerancias de bloqueo.

        Si no se dan argumentos, esto retornará los valores actuales.

        Arguments:
            speed (Number, deg/s o Number, mm/s): Si el controlador
                no puede alcanzar esta velocidad durante algún ``time`` incluso con la
                actuación máxima, está bloqueado.
            time (Number, ms): Cuánto tiempo el controlador tiene que estar por debajo de esta
                ``speed`` mínima antes de que digamos que está bloqueado.
        """


class Model:
    """Clase para interactuar con el observador de estado del motor y configuraciones."""

    def state(self) -> Tuple[float, float, float, bool]:
        """state() -> Tuple[float, float, float, bool]

        Obtiene el ángulo, velocidad, corriente y estado de bloqueo estimados del motor,
        usando un modelo de simulación que imita el motor real.
        Estas estimaciones se actualizan más rápido que las mediciones reales,
        lo que puede ser útil al construir tus propios controladores PID.

        Para la mayoría de las aplicaciones es mejor usar el *medido*
        :meth:`angle <pybricks.pupdevices.Motor.angle>`,
        :meth:`speed <pybricks.pupdevices.Motor.speed>`,
        :meth:`load <pybricks.pupdevices.Motor.load>`, y
        estado :meth:`stall <pybricks.pupdevices.Motor.stalled>` en su lugar.

        Returns:
            Tupla con el ángulo estimado (deg), velocidad (deg/s), corriente (mA),
            y estado de bloqueo (``True`` o ``False``).
        """

    @overload
    def settings(self, values: tuple) -> None: ...

    @overload
    def settings(self) -> tuple: ...

    def settings(self, speed, time):
        """settings(values)
        settings() -> Tuple

        Obtiene o configura los ajustes del modelo como una tupla de enteros. Si no se dan argumentos,
        esto retornará los valores actuales. Este método se usa principalmente
        para depurar la clase del modelo del motor. Cambiar estos ajustes no debería ser
        necesario en programas de usuario.

        .. _model settings: https://docs.pybricks.com/projects/pbio/en/latest/struct__pbio__observer__settings__t.html

        Arguments:
            values (Tuple): Tupla con los `model settings`_.
        """


class Motor(DCMotor):
    """Clase genérica para controlar motores con sensores de rotación incorporados."""

    control = Control()
    """Los motores usan control PID para seguir con precisión los objetivos de velocidad y
    ángulo que especificas. Puedes cambiar su comportamiento a través del
    atributo ``control`` del motor. Ver :ref:`control` para una descripción de los
    métodos disponibles."""

    model = Model()
    """Modelo que representa el observador que estima el estado del motor."""

    def __init__(
        self,
        port: Port,
        positive_direction: Direction = Direction.CLOCKWISE,
        gears: Optional[Union[Collection[int], Collection[Collection[int]]]] = None,
        reset_angle: bool = True,
        profile: Number = None,
    ):
        """__init__(port, positive_direction=Direction.CLOCKWISE, gears=None, reset_angle=True, profile=None)

        Arguments:
            port (Port): Puerto al que está conectado el motor.
            positive_direction (Direction): En qué dirección debe
                girar el motor cuando das un valor de velocidad o
                ángulo positivo.
            gears (list):
                Lista de engranajes vinculados al motor. El engranaje conectado
                al motor va primero y el engranaje conectado a la salida
                va al final.

                Por ejemplo: ``[12, 36]`` representa un tren de engranajes con un
                engranaje de 12 dientes conectado al motor y un engranaje de 36 dientes
                conectado a la salida. Usa una lista de listas para múltiples
                trenes de engranajes, como ``[[12, 36], [20, 16, 40]]``.

                Cuando especificas un tren de engranajes, todos los comandos y configuraciones del motor
                se ajustan automáticamente para tener en cuenta la relación de engranajes resultante.
                La dirección del motor permanece sin cambios por esto.
            reset_angle (bool):
                Elige ``True`` para restablecer el valor del sensor de rotación al
                ángulo del marcador absoluto (entre -180 y 179).
                Elige ``False`` para mantener el
                valor actual, para que tu programa sepa dónde lo dejó la última
                vez.
            profile (Number, deg): Perfil de precisión. Esta es la tolerancia de
                posición aproximada en grados que es aceptable en tu
                aplicación. Un valor menor da un movimiento más preciso pero más errático;
                un valor mayor da un movimiento menos preciso pero más suave. Si no se da ningún valor,
                se seleccionará automáticamente un perfil adecuado para este
                tipo de motor (aproximadamente 11 grados).
        """

    def angle(self) -> int:
        """angle() -> int: deg

        Obtiene el ángulo de rotación del motor.

        Returns:
            Ángulo del motor.
        """

    def speed(self, window: Number = 100) -> int:
        """speed(window=100) -> int: deg/s

        Obtiene la velocidad del motor.

        La velocidad se mide como el cambio en el ángulo del motor durante la
        ventana de tiempo dada. Una ventana corta hace que el valor de velocidad sea más
        sensible al movimiento del motor, pero menos estable. Una ventana larga hace que el
        valor de velocidad sea menos sensible, pero más estable.

        Arguments:
            window (Number, ms): La ventana de tiempo usada para determinar la velocidad.

        Returns:
            Velocidad del motor.

        """

    def stalled(self) -> bool:
        """stalled() -> bool

        Verifica si el motor está actualmente bloqueado.

        Está bloqueado cuando no puede alcanzar la velocidad o posición objetivo, incluso
        con la señal de actuación máxima.

        Returns:
            ``True`` si el motor está bloqueado, ``False`` si no lo está.
        """

    def load(self) -> int:
        """load() -> int: mNm

        Estima la carga que retiene al motor cuando intenta moverse.

        Returns:
            El par de carga.
        """

    def reset_angle(self, angle: Optional[Number]) -> None:
        """
        reset_angle(angle)

        Establece el ángulo de rotación acumulado del motor a un valor deseado.

        Si este motor también está siendo usado por una base de conducción, sus valores de distancia y
        ángulo también se verán afectados. Es posible que desees
        usar su método :meth:`reset <pybricks.robotics.DriveBase.reset>`
        en su lugar.

        Arguments:
            angle (Number, deg): Valor al que debe restablecerse el ángulo.
        """

    def hold(self) -> None:
        """hold()

        Detiene el motor y lo mantiene activamente en su ángulo actual."""

    def run(self, speed: Number) -> None:
        """run(speed)

        Hace funcionar el motor a una velocidad constante.

        El motor acelera a la velocidad dada y sigue funcionando a esta
        velocidad hasta que des un nuevo comando.

        Arguments:
            speed (Number, deg/s): Velocidad del motor.
        """

    def run_time(
        self, speed: Number, time: Number, then: Stop = Stop.HOLD, wait: bool = True
    ) -> MaybeAwaitable:
        """run_time(speed, time, then=Stop.HOLD, wait=True)

        Hace funcionar el motor a una velocidad constante durante un tiempo determinado.

        El motor acelera a la velocidad dada, sigue funcionando a esta velocidad,
        y luego desacelera. La maniobra completa dura exactamente el
        ``time`` dado.

        Arguments:
            speed (Number, deg/s): Velocidad del motor.
            time (Number, ms): Duración de la maniobra.
            then (Stop): Qué hacer después de detenerse.
            wait (bool): Esperar a que la maniobra se complete antes de continuar
                con el resto del programa.
        """

    def run_angle(
        self,
        speed: Number,
        rotation_angle: Number,
        then: Stop = Stop.HOLD,
        wait: bool = True,
    ) -> MaybeAwaitable:
        """run_angle(speed, rotation_angle, then=Stop.HOLD, wait=True)

        Hace funcionar el motor a una velocidad constante por un ángulo dado.

        Arguments:
            speed (Number, deg/s): Velocidad del motor.
            rotation_angle (Number, deg): Ángulo por el que el motor debe
                girar.
            then (Stop): Qué hacer después de detenerse.
            wait (bool): Esperar a que la maniobra se complete antes de continuar
                con el resto del programa.
        """

    def run_target(
        self,
        speed: Number,
        target_angle: Number,
        then: Stop = Stop.HOLD,
        wait: bool = True,
    ) -> MaybeAwaitable:
        """run_target(speed, target_angle, then=Stop.HOLD, wait=True)

        Hace funcionar el motor a una velocidad constante hacia un ángulo objetivo dado.

        La dirección de rotación se selecciona automáticamente según el ángulo
        objetivo. No importa si ``speed`` es positivo o negativo.

        Arguments:
            speed (Number, deg/s): Velocidad del motor.
            target_angle (Number, deg): Ángulo al que el motor debe girar.
            then (Stop): Qué hacer después de detenerse.
            wait (bool): Esperar a que el motor alcance el objetivo
                antes de continuar con el resto del programa.
        """

    def run_until_stalled(
        self,
        speed: Number,
        then: Stop = Stop.COAST,
        duty_limit: Optional[Number] = None,
    ) -> MaybeAwaitableInt:
        """
        run_until_stalled(speed, then=Stop.COAST, duty_limit=None) -> int: deg

        Hace funcionar el motor a una velocidad constante hasta que se bloquea.

        Arguments:
            speed (Number, deg/s): Velocidad del motor.
            then (Stop): Qué hacer después de detenerse.
            duty_limit (Number, %): Límite de ciclo de trabajo durante este
                comando. Esto es útil para evitar aplicar el par completo del motor
                a un mecanismo de engranajes o palanca. Si es ``None``, el
                límite de trabajo no se cambiará durante este comando.

        Returns:
            Ángulo en el que el motor se bloquea.
        """

    def done(self) -> bool:
        """done() -> bool

        Verifica si un comando o maniobra en curso está completo.

        Returns:
            ``True`` si el comando está completo, ``False`` si no lo está.
        """

    def track_target(self, target_angle: Number) -> None:
        """track_target(target_angle)

        Rastrea un ángulo objetivo. Esto es similar a :meth:`.run_target`, pero
        se omite la aceleración suave habitual: se moverá al ángulo
        objetivo lo más rápido posible. Este método es útil si quieres
        cambiar continuamente el ángulo objetivo.

        Arguments:
            target_angle (Number, deg): Ángulo objetivo al que el motor debe
                girar.
        """

    def close(self) -> None:
        """close()

        Cierra el objeto del motor para que puedas llamar a ``Motor`` nuevamente para inicializar
        un nuevo objeto.

        Esto permite a usuarios avanzados cambiar propiedades como los engranajes en el
        medio del programa, lo que puede ser útil para accesorios removibles.
        """


class Speaker:
    """Reproduce pitidos y sonidos usando un altavoz."""

    @overload
    def volume(self, volume: Number) -> None: ...

    @overload
    def volume(self) -> int: ...

    def volume(self, *args):
        """volume(volume)
        volume() -> int: %

        Obtiene o configura el volumen del altavoz.

        Si no se da volumen, este método retorna el volumen actual.

        Arguments:
            volume (Number, %): Volumen del altavoz en el rango 0-100.
        """

    def beep(self, frequency: Number = 500, duration: Number = 100) -> MaybeAwaitable:
        """beep(frequency=500, duration=100)

        Reproduce un pitido/tono.

        Arguments:
            frequency (Number, Hz):
                Frecuencia del pitido en el rango de 64-24000 Hz.
            duration (Number, ms):
                Duración del pitido. Si la duración es menor
                que 0, entonces el método retorna inmediatamente y la frecuencia
                continúa reproduciéndose indefinidamente.
        """

    def play_notes(self, notes: Iterable[str], tempo: Number = 120) -> MaybeAwaitable:
        """play_notes(notes, tempo=120)

        Reproduce una secuencia de notas musicales. Por ejemplo:
        ``["C4/4", "C4/4", "G4/4", "G4/4"]``.

        Cada nota es una cadena con el siguiente formato:

            - El primer carácter es el nombre de la nota, ``A`` a ``G``
              o ``R`` para un silencio.
            - Los nombres de las notas también pueden incluir un accidental ``#`` (sostenido) o
              ``b`` (bemol). ``B#``/``Cb`` y ``E#``/``Fb`` no están
              permitidos.
            - El nombre de la nota es seguido por el número de octava ``2``
              a ``8``. Por ejemplo ``C4`` es el do central. La octava cambia
              al siguiente número en la nota C, por ejemplo, ``B3`` es la
              nota debajo del do central (``C4``).
            - La octava es seguida por ``/`` y un número que indica
              el tamaño de la nota. Por ejemplo ``/4`` es una negra,
              ``/8`` es una corchea y así sucesivamente.
            - Esto puede ser seguido opcionalmente por un ``.`` para hacer una nota
              con puntillo. Las notas con puntillo duran 1-1/2 veces más que las notas sin
              punto.
            - La nota puede terminar opcionalmente con un ``_`` que es una ligadura o
              slur. Esto hace que no haya pausa entre esta nota y
              la siguiente nota.

        Arguments:
            notes (iter):
                Una secuencia de notas a reproducir.
            tempo (int):
                Beats por minuto. Una negra es un beat.
        """


class ColorLight:
    """Controla una luz multicolor."""

    def on(self, color: Color) -> None:
        """on(color)

        Enciende la luz con el color especificado.

        Arguments:
            color (Color): Color de la luz.
        """

    def off(self) -> None:
        """off()

        Apaga la luz."""

    def blink(self, color: Color, durations: Collection[Number]) -> None:
        """blink(color, durations)

        Hace parpadear la luz con el color dado, encendiéndola y apagándola
        durante las duraciones especificadas.

        La luz sigue parpadeando indefinidamente mientras el resto del
        programa continúa ejecutándose.

        Este método proporciona una forma simple de crear patrones básicos
        pero útiles. Para patrones más genéricos y con múltiples colores,
        usa ``animate()`` en su lugar.

        Arguments:
            color (Color): Color de la luz.
            durations (list): Secuencia de valores de tiempo de
                la forma ``[encendido_1, apagado_1, encendido_2, apagado_2, ...]``.
        """

    def animate(self, colors: Collection[Color], interval: Number) -> None:
        """animate(colors, interval)

        Anima la luz con una secuencia de colores, mostrándolos uno por
        uno durante el intervalo especificado.

        La animación se ejecuta en segundo plano mientras el resto del
        programa continúa ejecutándose. Cuando la animación se completa, se repite.

        Arguments:
            colors (list): Secuencia de valores :class:`Color <.parameters.Color>`.
            interval (Number, ms): Tiempo entre actualizaciones de color.
        """


class ExternalColorLight:
    """Controla una luz multicolor."""

    def on(self, color: Color) -> MaybeAwaitable:
        """on(color)

        Enciende la luz con el color especificado.

        Arguments:
            color (Color): Color de la luz.
        """

    def off(self) -> MaybeAwaitable:
        """off()

        Apaga la luz.
        """


class LightArray3:
    """Controla un arreglo de tres luces de un solo color."""

    def on(
        self, brightness: Union[Number, Tuple[Number, Number, Number]]
    ) -> MaybeAwaitable:
        """on(brightness)

        Enciende las luces con el brillo especificado.

        Arguments:
            brightness (Number o tuple, %):
                Usa un solo valor para establecer el brillo de todas las luces al
                mismo tiempo. Usa una tupla de tres valores para establecer el brillo
                de cada luz individualmente.
        """

    def off(self) -> MaybeAwaitable:
        """off()

        Apaga todas las luces.
        """


class LightArray4(LightArray3):
    """Controla un arreglo de cuatro luces de un solo color."""

    def on(
        self, brightness: Union[Number, Tuple[Number, Number, Number, Number]]
    ) -> MaybeAwaitable:
        """on(brightness)

        Enciende las luces con el brillo especificado.

        Arguments:
            brightness (Number o tuple, %):
                Usa un solo valor para establecer el brillo de todas las luces al
                mismo tiempo. Usa una tupla de cuatro valores para establecer el brillo
                de cada luz individualmente. El orden de las luces se muestra
                en la imagen anterior.
        """


class LightMatrix:
    """Controla una cuadrícula rectangular de luces de un solo color."""

    def __init__(self, rows: int, columns: int):
        """LightMatrix(rows, columns)

        Inicializa la pantalla de matriz de luces.

        Arguments:
            rows (int): Número de filas en la cuadrícula
            columns (int): Número de columnas en la cuadrícula
        """

    def orientation(self, up: Side) -> None:
        """orientation(up)

        Establece la orientación de la pantalla de matriz de luces.

        Solo las nuevas imágenes y píxeles mostrados se ven afectados. El contenido de pantalla
        existente permanece sin cambios.

        Arguments:
            top (Side): Qué lado de la pantalla de matriz de luces está "arriba" en tu
                diseño. Elige ``Side.TOP``, ``Side.LEFT``, ``Side.RIGHT``,
                o ``Side.BOTTOM``.
        """

    def icon(self, icon: Matrix) -> None:
        """icon(icon)

        Muestra un icono, representado por una matriz de valores de :ref:`brightness`.

        Arguments:
            icon (Matrix): Matriz de intensidades (:ref:`brightness`). También se
                acepta una lista 2D.
        """

    def animate(self, matrices: Collection[Matrix], interval: Number) -> None:
        """animate(matrices, interval)

        Muestra una animación hecha usando una lista de imágenes.

        Cada imagen tiene el mismo formato que arriba. Cada imagen se
        muestra durante el intervalo dado. La animación se repite
        para siempre mientras el resto de tu programa sigue ejecutándose.

        Arguments:
            matrices (iter): Secuencia de
                :class:`Matrix <pybricks.tools.Matrix>` de intensidades.
            interval (Number, ms): Tiempo para mostrar cada imagen en la lista.
        """

    def pixel(self, row: Number, column: Number, brightness: Number = 100) -> None:
        """pixel(row, column, brightness=100)

        Enciende un píxel con el brillo especificado.

        Arguments:
            row (Number): Índice vertical de la cuadrícula, comenzando en 0 desde arriba.
            column (Number): Índice horizontal de la cuadrícula, comenzando en 0 desde la izquierda.
            brightness (Number :ref:`brightness`): Brillo del píxel.
        """

    def off(self) -> None:
        """off()

        Apaga todos los píxeles."""

    def number(self, number: Number) -> None:
        """number(number)

        Muestra un número en el rango -99 a 99.

        Un signo menos (``-``) se muestra como un punto tenue
        en el centro de la pantalla. Los números mayores que 99 se
        muestran como ``>``. Los números menores que -99 se muestran como ``<``.

        Arguments:
            number (int): El número a mostrar.
        """

    def char(self, char: str) -> None:
        """char(char)

        Muestra un carácter o símbolo en la cuadrícula de luces. Puede
        ser cualquier letra (``a``--``z``), letra mayúscula (``A``--``Z``) o uno de
        los siguientes símbolos: ``!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}``.

        Arguments:
            character (str): El carácter o símbolo a mostrar.
        """

    def text(self, text: str, on: Number = 500, off: Number = 50) -> None:
        """text(text, on=500, off=50)

        Muestra una cadena de texto, un carácter a la vez, con una pausa
        entre cada carácter. Después de que se muestra el último carácter, todas las luces
        se apagan.

        Arguments:
            text (str): El texto a mostrar.
            on (Number, ms): Por cuánto tiempo se muestra un carácter.
            off (Number, ms): Por cuánto tiempo la pantalla está apagada entre
                caracteres.
        """


class Keypad:
    """Obtiene el estado de los botones en un diseño de teclado."""

    def __init__(self, active_buttons): ...

    def pressed(self) -> Set[Button]:
        """pressed() -> Set[Button]

        Verifica qué botones están actualmente presionados.

        Returns:
            Conjunto de botones presionados.
        """


class Battery:
    """Obtiene el estado de una batería."""

    def voltage(self) -> int:
        """voltage() -> int: mV

        Obtiene el voltaje de la batería.

        Returns:
            Voltaje de la batería.
        """

    def current(self) -> int:
        """current() -> int: mA

        Obtiene la corriente suministrada por la batería.

        Returns:
            Corriente de la batería.
        """


class Charger:
    """Obtiene el estado de un cargador de batería."""

    def connected(self) -> bool:
        """connected() -> bool

        Verifica si un cargador está conectado vía USB.

        Returns:
            ``True`` si un cargador está conectado, ``False`` si no lo está.
        """

    def status(self) -> int:
        """status() -> int

        Obtiene el estado del cargador de batería, representado por uno de los
        siguientes valores. Esto corresponde al indicador de luz de la batería
        justo al lado del puerto USB.

            0. No cargando (luz apagada).
            1. Cargando (luz roja).
            2. Carga completa (luz verde).
            3. Hay un problema con el cargador (luz amarilla).

        Returns:
            Valor de estado.
        """

    def current(self) -> int:
        """current() -> int: mA

        Obtiene la corriente de carga.

        Returns:
            Corriente de carga.
        """


class SimpleAccelerometer:
    """Obtiene mediciones de un acelerómetro."""

    def acceleration(self) -> Tuple[int, int, int]:
        """acceleration() -> Tuple[int, int, int]: mm/s²

        Obtiene la aceleración del dispositivo.

        Returns:
            Aceleración a lo largo de los tres ejes.
        """

    def up(self) -> Side:
        """up() -> Side

        Verifica qué lado del hub está mirando hacia arriba actualmente.

        Returns:
            ``Side.TOP``, ``Side.BOTTOM``, ``Side.LEFT``, ``Side.RIGHT``,
            ``Side.FRONT`` o ``Side.BACK``.
        """

    def tilt(self) -> Tuple[int, int]:
        """tilt() -> Tuple[int, int]

        Obtiene los ángulos de inclinación (pitch) y balanceo (roll). Esto es relativo a la
        :ref:`orientación neutral especificada por el usuario <robotframe>`.

        El orden de rotación es inclinación-luego-balanceo. Esto es equivalente a una
        rotación positiva a lo largo del eje y del robot y luego una rotación positiva
        a lo largo del eje x.

        Returns:
            Tupla de ángulos de inclinación y balanceo en grados.
        """


class IMU:

    def up(self, calibrated: bool = True) -> Side:
        """up(calibrated=True) -> Side

        Verifica qué lado del hub está mirando hacia arriba actualmente.

        Arguments:
            calibrated (bool): Elige ``True`` para usar datos calibrados del giroscopio y
                acelerómetro para determinar qué lado está arriba. Elige
                ``False`` para usar valores de aceleración crudos.

        Returns:
            ``Side.TOP``, ``Side.BOTTOM``, ``Side.LEFT``, ``Side.RIGHT``,
            ``Side.FRONT`` o ``Side.BACK``.
        """

    def tilt(self, calibrated: bool = True) -> Tuple[int, int]:
        """tilt(calibrated=True) -> Tuple[int, int]

        Obtiene los ángulos de inclinación (pitch) y balanceo (roll). Esto es relativo a la
        :ref:`orientación neutral especificada por el usuario <robotframe>`.

        El orden de rotación es inclinación-luego-balanceo. Esto es equivalente a una
        rotación positiva a lo largo del eje y del robot y luego una rotación positiva
        a lo largo del eje x.

        Arguments:
            calibrated (bool): Elige ``True`` para usar datos calibrados del giroscopio y
                acelerómetro para determinar la inclinación. Elige ``False``
                para usar valores de aceleración crudos.

        Returns:
            Tupla de ángulos de inclinación y balanceo en grados.
        """

    @overload
    def acceleration(self, axis: Axis = None, calibrated: bool = True) -> float: ...

    @overload
    def acceleration(self, calibrated: bool = True) -> Matrix: ...

    def acceleration(self, *args):
        """
        acceleration(axis, calibrated=True) -> float: mm/s²
        acceleration(calibrated=True) -> vector: mm/s²

        Obtiene la aceleración del dispositivo a lo largo de un eje dado en el
        :ref:`marco de referencia del robot <robotframe>`.

        Arguments:
            axis (Axis): Eje a lo largo del cual se debe medir la aceleración,
                o ``None`` para obtener un vector a lo largo de todos los ejes.
            calibrated (bool): Elige ``True`` para usar valores de aceleración
                calibrados. Elige ``False`` para usar valores de aceleración crudos.

        Returns:
            Aceleración a lo largo del eje especificado. Si no especificas ningún eje,
            esto retorna un vector de aceleraciones a lo largo de todos los ejes.
        """

    def ready(self) -> bool:
        """ready() -> bool

        Comprueba si el dispositivo está calibrado y listo para su uso.

        Esto se vuelve ``True`` cuando el robot ha estado estático durante
        unos segundos, lo que permite que el dispositivo se recalibre. Es ``False``
        si el hub acaba de iniciarse, o si no ha tenido la oportunidad de
        calibrarse durante más de 10 minutos.

        Returns:
            ``True`` si está listo para su uso, ``False`` si no lo está.
        """

    def stationary(self) -> bool:
        """stationary() -> bool

        Comprueba si el dispositivo está actualmente estacionario (sin moverse).

        Returns:
            ``True`` si está estacionario durante al menos un segundo,
            ``False`` si se está moviendo.
        """

    @overload
    def settings(
        self,
        *,
        angular_velocity_threshold: float = None,
        acceleration_threshold: float = None,
        heading_correction: float = None,
        angular_velocity_bias: Tuple[float, float, float] = None,
        angular_velocity_scale: Tuple[float, float, float] = None,
        acceleration_correction: Tuple[float, float, float, float, float, float] = None,
    ) -> None: ...

    @overload
    def settings(
        self,
    ) -> Tuple[
        float,
        float,
        float,
        Tuple[float, float, float],
        Tuple[float, float, float],
        Tuple[float, float, float, float, float, float],
    ]: ...

    def settings(self, *args):
        """
        settings(*, angular_velocity_threshold, acceleration_threshold, heading_correction, angular_velocity_bias, angular_velocity_scale, acceleration_correction)
        settings() -> Tuple

        Configura los ajustes del IMU. Si no se dan argumentos,
        esto retorna los valores actuales. Usa argumentos con nombre para cada valor
        para asegurar el comportamiento correcto porque los ajustes pueden agregarse o cambiarse en
        versiones futuras.

        Estos ajustes del IMU se guardan en el hub. Mantendrán sus valores
        hasta que los cambies nuevamente. Los valores se restablecerán a los valores predeterminados
        si actualizas el hub a una versión de firmware diferente o llamas al
        método ``hub.system.reset_storage``.

        Los ``angular_velocity_threshold`` y ``acceleration_threshold``
        definen cuándo el hub se considera estacionario. Si todas
        las mediciones permanecen por debajo de estos umbrales durante un segundo, el IMU
        se recalibrará a sí mismo. En una sala ruidosa con altas vibraciones ambientales (como un
        salón de competencia), puedes aumentar los umbrales
        ligeramente para darle a tu robot la oportunidad de calibrarse.
        Para verificar que tus ajustes funcionen como se espera, prueba que
        el método ``stationary()`` dé ``False`` si tu robot se está moviendo,
        y ``True`` si está quieto.

        El giroscopio mide qué tan rápido gira el hub para estimar el
        ángulo total. Debido a variaciones en el proceso de producción, cada
        hub reporta consistentemente un valor diferente para una rotación completa. Por
        ejemplo, tu hub podría reportar consistentemente `357` grados por cada
        vuelta de `360` grados. Puedes medir este valor
        con ``hub.imu.rotation(-Axis.Z, calibrated=False)`` e ingresarlo como
        el ajuste ``heading_correction``. Entonces, el método ``hub.imu.heading()``
        lo tendrá en cuenta en adelante, escalándolo correctamente
        a 360 grados para una rotación completa.

        Arguments:
            angular_velocity_threshold (Number, deg/s): El umbral para
                variaciones en la velocidad angular por debajo del cual el hub se
                considera suficientemente estacionario para calibrarse.
                Después de un reinicio el valor es 2 deg/s.
            acceleration_threshold (Number, mm/s²): El umbral para
                variaciones en la aceleración por debajo del cual el hub se considera
                suficientemente estacionario para calibrarse. Después de un reinicio el valor
                es 2500 mm/s².
            heading_correction (Number, deg): Número de grados
                reportados para una rotación completa de tu robot.
                Después de un reinicio el valor es 360 grados. Esto se aplica además
                de cualquier escalado que se haga con el ajuste ``angular_velocity_scale``.
            angular_velocity_bias (tuple, deg/s): Sesgo inicial para mediciones de
                velocidad angular a lo largo de x, y, y z inmediatamente después del arranque.
                Después de un reinicio el valor es (0, 0, 0) deg/s.
            angular_velocity_scale (tuple, deg): Ajuste de escala para rotación en x, y,
                y z para tener en cuenta diferencias de fabricación. Después de un
                reinicio el valor es (360, 360, 360) deg/s. Los valores correctos
                pueden obtenerse usando `hub.imu.rotation(Axis.X, calibrated=False)`
                y repitiéndolo para cada eje.
            acceleration_correction (tuple, mm/s²): Ajuste de escala para magnitud de gravedad en x, y,
                y z en ambas direcciones para tener en cuenta
                diferencias de fabricación. Después de un reinicio el
                valor es (9806.65, -9806.65, 9806.65, -9806.65, 9806.65, -9806.65) mm/s².
                Los valores correctos pueden
                obtenerse usando `hub.imu.acceleration(Axis.X, calibrated=False)`
                y repitiéndolo para todos los ejes en ambas direcciones.
        """

    def heading(self) -> float:
        """heading() -> float: deg

        Obtiene el ángulo de rumbo de tu robot. Un valor positivo significa un
        giro en sentido horario.

        El rumbo es 0 cuando tu programa inicia. El valor continúa creciendo
        incluso cuando el robot gira más de 180 grados. No se ajusta
        a -180 como lo hace en algunas aplicaciones.

        Returns:
            Ángulo de rumbo relativo a la orientación inicial.

        """

    def reset_heading(self, angle: Number) -> None:
        """reset_heading(angle)

        Restablece el ángulo de rumbo acumulado del robot.

        Esto no puede llamarse mientras una base de conducción está usando el giroscopio para conducir o
        mantener posición.
        Usa :meth:`DriveBase.reset() <pybricks.robotics.DriveBase.reset>`
        en su lugar, que detendrá el robot y luego establecerá el nuevo valor de rumbo.

        .. versionchanged:: 3.6 No está permitido restablecer el ángulo mientras se conduce. Detente primero.

        Arguments:
            angle (Number, deg): Valor al que debe restablecerse el rumbo.

        Raises:
            OSError:
                Hay una base de conducción que actualmente está usando el giroscopio.
        """

    @overload
    def angular_velocity(self, axis: Axis = None, calibrated: bool = True) -> float: ...

    @overload
    def angular_velocity(self, calibrated: bool = True) -> Matrix: ...

    def angular_velocity(self, *args):
        """
        angular_velocity(axis, calibrated=True) -> float: deg/s
        angular_velocity(calibrated=True) -> vector: deg/s

        Obtiene la velocidad angular del dispositivo a lo largo de un eje dado en
        el :ref:`marco de referencia del robot <robotframe>`.

        Arguments:
            axis (Axis): Eje a lo largo del cual se debe medir la velocidad angular,
                o ``None`` para obtener un vector a lo largo de todos los ejes.
            calibrated (bool): Elige ``True`` para compensar el
                sesgo estimado y la escala configurada del giroscopio. Elige ``False``
                para obtener valores de velocidad angular crudos.

        Returns:
            Velocidad angular a lo largo del eje especificado. Si no especificas ningún eje,
            esto retorna un vector de aceleraciones a lo largo de todos los ejes.
        """

    def rotation(self, axis: Axis, calibrated: bool = True) -> float:
        """
        rotation(axis, calibrated=True) -> float: deg

        Obtiene la rotación del dispositivo a lo largo de un eje dado en
        el :ref:`marco de referencia del robot <robotframe>`.

        Este valor es útil si tu robot *solo* rota a lo largo del eje solicitado.
        Para movimiento tridimensional general, usa el
        método ``orientation()`` en su lugar.

        Arguments:
            axis (Axis): Eje a lo largo del cual se debe medir la rotación.
            calibrated (bool): Elige ``True`` para compensar la escala
                configurada del giroscopio. Elige ``False`` para obtener valores sin escalar.

        Returns:
            El ángulo de rotación.
        """

    def orientation(self) -> Matrix:
        """
        orientation() -> Matrix

        Obtiene la orientación tridimensional del robot en
        el :ref:`marco de referencia del robot <robotframe>`.

        Retorna una matriz de rotación cuyas columnas representan los ejes ``X``, ``Y``,
        y ``Z`` del robot.

        Returns:
            La matriz de rotación 3x3.
        """


class CommonColorSensor:
    """Sensor de color genérico que soporta la calibración de color de Pybricks."""

    def __init__(self, port: Port):
        """__init__(port)

        Arguments:
            port (Port): Puerto al que está conectado el sensor.
        """

    def color(self) -> MaybeAwaitableColor:
        """color() -> Color

        Escanea el color de una superficie.

        Eliges qué colores se detectan usando el
        método ``detectable_colors()``. Por defecto, detecta
        ``Color.RED``, ``Color.YELLOW``, ``Color.GREEN``, ``Color.BLUE``,
        ``Color.WHITE``, o ``Color.NONE``.

        Returns:
            Color detectado.
        """

    def hsv(self) -> MaybeAwaitableColor:
        """hsv() -> Color

        Escanea el color de una superficie.

        Este método es similar a ``color()``, pero da el rango completo
        de valores de matiz, saturación y brillo, en lugar de redondearlo al
        color detectable más cercano.

        Returns:
            Color medido. El color es descrito por un matiz (0--359), una
            saturación (0--100), y un valor de brillo (0--100).
        """

    def ambient(self) -> MaybeAwaitableInt:
        """ambient() -> int: %

        Mide la intensidad de la luz ambiente.

        Returns:
            Intensidad de luz ambiente, variando de 0% (oscuro)
            a 100% (brillante).
        """

    def reflection(self) -> MaybeAwaitableInt:
        """reflection() -> int: %

        Mide cuánto refleja una superficie la luz emitida por el
        sensor.

        Returns:
            Reflejo medido, variando de 0% (sin reflejo) a
            100% (alto reflejo).
        """

    @overload
    def detectable_colors(self, colors: Collection[Color]) -> None: ...

    @overload
    def detectable_colors(self) -> Collection[Color]: ...

    def detectable_colors(self, *args):
        """
        detectable_colors(colors)
        detectable_colors() -> Collection[Color]

        Configura qué colores debe detectar el método ``color()``.

        Especifica solo los colores que deseas detectar en tu aplicación.
        De esta manera, las mediciones de color completo se redondean al color
        deseado más cercano, y otros colores se ignoran. Esto mejora la confiabilidad.

        Si no das argumentos, se retornarán los colores actualmente elegidos.

        Al programar con bloques, esto se configura en el bloque de configuración del sensor.

        Arguments:
            colors (list o tuple): Lista de objetos :class:`Color <.parameters.Color>`
                : los colores que quieres detectar. Puedes elegir
                colores estándar como ``Color.MAGENTA``, o proporcionar tus
                propios colores como ``Color(h=348, s=96, v=40)`` para resultados
                aún mejores. Mides tus propios colores con el
                método ``hsv()``.
        """


class AmbientColorSensor(CommonColorSensor):
    """Como CommonColorSensor, pero también detecta colores ambientales cuando la luz del sensor
    está apagada"""

    def color(self, surface: bool = True) -> MaybeAwaitableColor:
        """color(surface=True) -> Color

        Escanea el color de una superficie o una fuente de luz externa.

        Eliges qué colores se detectan usando el
        método ``detectable_colors()``. Por defecto, detecta
        ``Color.RED``, ``Color.YELLOW``, ``Color.GREEN``, ``Color.BLUE``,
        ``Color.WHITE``, o ``Color.NONE``.

        Arguments:
            surface (bool): Elige ``true`` para escanear el color de objetos
                y superficies. Elige ``false`` para escanear el color de
                pantallas y otras fuentes de luz externas.

        Returns:
            Color detectado.
        """

    def hsv(self, surface: bool = True) -> MaybeAwaitableColor:
        """hsv(surface=True) -> Color

        Escanea el color de una superficie o una fuente de luz externa.

        Este método es similar a ``color()``, pero da el rango completo
        de valores de matiz, saturación y brillo, en lugar de redondearlo al
        color detectable más cercano.

        Arguments:
            surface (bool): Elige ``true`` para escanear el color de objetos
                y superficies. Elige ``false`` para escanear el color de
                pantallas y otras fuentes de luz externas.

        Returns:
            Color medido. El color es descrito por un matiz (0--359), una
            saturación (0--100), y un valor de brillo (0--100).
        """


class BLE:
    """
    Bluetooth Low Energy.

    .. versionadded:: 3.3
    """

    def broadcast(self, data: Union[bool, int, float, str, bytes]) -> MaybeAwaitable:
        """broadcast(data)

        Comienza a transmitir los datos dados en
        el ``broadcast_channel`` que seleccionaste al inicializar el hub.

        Los datos pueden ser de tipo ``int``, ``float``, ``str``, ``bytes``,
        ``True``, o ``False``. También puede ser una lista o tupla de estos.

        Elige ``None`` para detener la transmisión. Esto ayuda a mejorar el rendimiento
        cuando no necesitas la función de transmisión, especialmente cuando observas
        al mismo tiempo.

        El tamaño total de datos es bastante limitado (26 bytes). ``True`` y
        ``False`` ocupan 1 byte cada uno. ``float`` ocupa 5 bytes. ``int`` ocupa de 2 a
        5 bytes dependiendo de qué tan grande sea el número. ``str`` y ``bytes`` ocupan
        el número de bytes en el objeto más un byte extra.

        Al hacer multitarea, solo una tarea puede transmitir a la vez. Para transmitir
        información de múltiples tareas (o pilas de bloques), podrías usar una
        tarea separada dedicada que transmita nuevos valores cuando una o más
        variables cambien.

        Arguments:
            data: El valor o valores a transmitir.

        .. versionadded:: 3.3
        """

    def observe(
        self, channel: int
    ) -> Optional[Tuple[Union[bool, int, float, str, bytes], ...]]:
        """observe(channel) -> bool | int | float | str | bytes | tuple | None

        Recupera los últimos datos observados para un canal dado.

        Recibir datos es más confiable cuando el hub no está conectado
        a una computadora u otros dispositivos al mismo tiempo.

        Arguments:
            channel (int): El canal a observar (0 a 255).

        Returns:
            Los datos recibidos en el mismo formato en que fueron enviados, o ``None``
            si no hay datos recientes disponibles.

        .. versionadded:: 3.3
        """

    def signal_strength(self, channel: int) -> int:
        """signal_strength(channel) -> int: dBm

        Obtiene la intensidad de señal promedio en dBm para el canal dado.

        Esto indica qué tan cerca está el dispositivo transmisor. Los dispositivos cercanos
        pueden tener una intensidad de señal alrededor de -40 dBm, mientras que los dispositivos lejanos
        podrían tener una intensidad de señal alrededor de -70 dBm.

        Arguments:
            channel (int): El número de canal (0 a 255).

        Returns:
            La intensidad de señal o ``-128`` si no hay datos observados recientes.

        .. versionadded:: 3.3
        """

    def version(self) -> str:
        """version() -> str

        Obtiene la versión de firmware del chip Bluetooth.

        .. versionadded:: 3.3
        """