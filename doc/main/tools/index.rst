.. pybricks-requirements::

:mod:`tools <pybricks.tools>` -- Herramientas de propósito general
================================================

.. automodule:: pybricks.tools
    :no-members:

Herramientas de tiempo
---------------

.. autofunction:: wait

.. autoclass:: pybricks.tools.StopWatch
    :no-members:

    .. automethod:: pybricks.tools.StopWatch.time

    .. automethod:: pybricks.tools.StopWatch.pause

    .. automethod:: pybricks.tools.StopWatch.resume

    .. automethod:: pybricks.tools.StopWatch.reset

Herramientas de entrada
-----------------------

.. autofunction:: pybricks.tools.read_input_byte

.. pybricks-requirements:: light-matrix

.. autofunction:: pybricks.tools.hub_menu

.. literalinclude::
    ../../../examples/pup/tools/hub_menu.py

Herramientas de álgebra lineal
--------------------

.. pybricks-requirements:: stm32-float

.. autoclass:: pybricks.tools.Matrix
    :no-members:

    .. autoattribute:: pybricks.tools::Matrix.T

    .. autoattribute:: pybricks.tools::Matrix.shape

.. pybricks-requirements:: stm32-float

.. autofunction:: pybricks.tools.vector

.. autofunction:: pybricks.tools.cross
