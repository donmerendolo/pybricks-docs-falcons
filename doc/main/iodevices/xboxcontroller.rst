Mando de Xbox
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/diagrams_source/xboxcontroller.png
   :width: 60 %

.. autoclass:: pybricks.iodevices.XboxController
  :no-members:

  .. automethod:: pybricks.iodevices::XboxController.buttons.pressed

    Los botones incluyen:

      * ``Button.A``, ``Button.B``, ``Button.X``, ``Button.Y``.
      * ``Button.UP``, ``Button.DOWN``, ``Button.LEFT``, ``Button.RIGHT``
        (pad direccional). Se pueden presionar, como máximo, dos de estos al mismo tiempo.
      * ``Button.LB`` y ``Button.RB`` (bumper).
      * ``Button.LJ`` y ``Button.RJ`` (presionando los joysticks).
      * ``Button.VIEW``, ``Button.MENU``, ``Button.GUIDE`` (el logo de Xbox), y ``Button.UPLOAD``.
      * ``Button.P1``, ``Button.P2``, ``Button.P3``, y ``Button.P4`` (solo Elite Series 2).
        Presionar las paletas también puede detectarse como otras pulsaciones de botones,
        dependiendo del perfil activo.

  .. automethod:: pybricks.iodevices::XboxController.joystick_left

  .. automethod:: pybricks.iodevices::XboxController.joystick_right

  .. automethod:: pybricks.iodevices::XboxController.triggers

  .. automethod:: pybricks.iodevices::XboxController.dpad

  .. automethod:: pybricks.iodevices::XboxController.profile

  .. automethod:: pybricks.iodevices::XboxController.rumble

.. _xbox-controller-pairing:

Instrucciones para emparejar el mando de Xbox
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

La primera vez que uses un mando con un hub, tendrás que emparejarlos:
enciende el mando y luego mantén pulsado el botón de emparejamiento
en la parte trasera del mando durante unos segundos. Cuando lo sueltes,
el botón de Xbox comenzará a parpadear más rápidamente. Luego, inicia tu
programa.

Cuando el emparejamiento y la conexión sean exitosos, el botón de Xbox
dejará de parpadear y permanecerá encendido mientras el programa esté en
ejecución.

Repetir conexiones
==================

Si usas el mismo mando con el mismo hub, puedes simplemente encenderlo
la próxima vez y el hub se conectará automáticamente cuando tu programa
ejecute esta clase.

El mando de Xbox solo soporta esta conexión más rápida con el dispositivo
usado más recientemente. Así que si lo vuelves a conectar a tu consola Xbox,
o lo conectas a otro hub, tendrás que emparejarlos de nuevo como se describe
arriba.

Mandos compatibles
==================

Todos los mandos lanzados después del 2016 son compatibles. Esto incluye el
mando de la One S (``1708`` de 2016), el Elite Series 2 (``1797`` de 2019), y el
Series X/S (``1914`` de 2020), que es el modelo más reciente hasta la fecha de esta redacción.

.. raw:: html

  <p>Ver también <a href="https://en.wikipedia.org/wiki/Xbox_Wireless_Controller#Summary" target="_blank">
  este resumen</a> de números de modelo que incluye imágenes de cada mando.</p>

Actualizar el mando de Xbox
===========================

Si usas el mando con una consola Xbox, probablemente esté ya actualizado. Si
no lo has usado durante un tiempo o si lo has comprado recientemente, es posible
que tengas actualizarlo.

Para actualizar el mando sin una consola Xbox, puedes usar la app Xbox Accessories
en un ordenador con Windows. Puedes descargarla desde la Microsoft Store.
Conecta el mando al ordenador mediante USB y sigue las instrucciones en la
app para hacer clic en "Actualizar ahora".

Limitaciones del Technic Hub
============================

Debido a limitaciones del Technic Hub, el hub se desconectará del
ordenador al buscar el mando de Xbox. Esto significa que no podrás
ver la salida del comando ``print``. Además, tendrás que conectarte
de nuevo al ordenador si quieres cambiar tu programa.
