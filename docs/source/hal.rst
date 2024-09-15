HAL Buttons
===========

Any QPushButton, QCheckBox or QRadioButton can have a HAL BIT pin by adding a
string Dynamic Property called `function` with the value of `hal_pin` and a
string Dynamic Property called `pin_name` where n is some non repeated number with a
property of `pin_name, pin_type, pin_dir` seperated by comma's

.. csv-table:: HAL Push Button
   :width: 80%
   :align: center

	Property Name, Pin Value
	pin_name, any unique name
	hal_type, HAL_BIT
	hal_dir, HAL_OUT

Any QSpinBox or QDoubleSpinBox can be a hal pin.

.. csv-table:: HAL Spin Box
   :width: 80%
   :align: center

	Property Name, Pin Value
	pin_name, any unique name
	hal_type, HAL_FLOAT or HAL_S32 or HAL_U32
	hal_dir, HAL_OUT


Pin Types::

	HAL_BIT
	HAL_FLOAT
	HAL_S32
	HAL_U32

Pin Directions::

	HAL_IN
	HAL_OUT
	HAL_IO

Currently only `HAL_BIT` with `HAL_OUT` has been tested.

.. warning:: By default no QRadioButtons are checked unless you set one checked
          in the Designer. Starting up with none checked could be a problem if
          you expect one to be selected at startup.

Step by Step
------------

You can use a QPushButton, QPushButton with checkable selected, QCheckBox or
QRadioButton for a HAL output control.

Drag the widget into the GUI and the widget can have any name you like. Names
are not used by Flex GUI for HAL controls.

Click on the widget to select it then click on the green plus sign in the
Property Editor for that widget to add a Dynamic Property and select String.

.. image:: /images/hal-01.png
   :align: center

Set the Property Name to `function` and click on Ok.

.. image:: /images/hal-02.png
   :align: center

Set the Value to `hal_pin`, this tells Flex GUI that this widget is going to
have a HAL pin.

.. image:: /images/hal-03.png
   :align: center

Add another Dynamic Property named `pin_n` where `n` is a unique number or word
and click Ok. Flex GUI searches the Dynamic Properties for a property that
starts with `pin_` so any unique letters or numbers after the underscore are
valid.

.. image:: /images/hal-04.png
   :align: center

The first item in the Value must be unique Flex HAL name, then seperated by
commas the next item must be the HAL Pin Type then the HAL Pin Direction. The
pin name created by Flex is flexhal.(the name you put first).

.. image:: /images/hal-05.png
   :align: center

If you added Show HAL to your menu you can open up the `Halshow` program and
view the pin names.

.. image:: /images/hal-06.png
   :align: center

The pin names will all start with flexhal then the unique name you gave them.

.. image:: /images/hal-07.png
   :align: center

Now you can connect the Flex HAL pin in the postgui.hal file like normal.
::

	net some-signal-name flexhal.hal-test-01 => some-other-pin-in

After installing Flex GUI from the CNC menu you can copy the Flex GUI examples
and look at the hal-btn example.

Homed Required
--------------

If the HAL button requires all joints to be homed before being enabled you can
specifiy that by adding a Dynamic Property named `required` and set the value to
`homed`.

.. image:: /images/hal-08.png
   :align: center

