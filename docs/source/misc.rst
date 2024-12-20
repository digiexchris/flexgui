Miscellaneous Items
===================

Import Python
-------------

`Python Import Tutorial <https://youtu.be/QC4K_8VMc6Y>`_

To import a python module add the following to the INI [FLEX] section using the
name of the python file without the.py extension. The file name must be unique
and can not be any python module name.
::

	[FLEX]
	IMPORT = testpy

.. note:: The module requires the .py extension to be able to import so the
   above module would be named testpy.py.

In the python file you import you must have a `startup` function where you make
any connections from objects in the ui file to code in your module. The parent
is passed to the startup function to give you access to all the objects in the
GUI.
::

	from functools import partial

	def startup(parent):
		# connect a pushbutton without passing parent
		parent.my_test_pb.clicked.connect(test_1)
		parent.get_names_pb.clicked.connect(partial(get_names, parent))

		# connect a pushbutton and pass parent to fhe function
		parent.another_test_pb.clicked.connect(partial(test_2, parent))

	def test_1():
		print('test 1')

	def test_2(parent):
		# in this function you have access to all the objects in parent
		print(f'test 2 {parent.another_test_pb.text()}')

	def get_names(parent):
		# get all the object names from the parent
		print(dir(parent))

Get Variables
-------------

To load a user variable (31-5000) from the var file at startup into a
QDoubleSpinBox add two Dynamic Properties
::

	function get_var
	variable number of variable

.. image:: /images/get-variable-01.png
   :align: center

File Selector
-------------

Add a QListWidget and name it `file_lw`, this can be used with a touch screen by
specifying the touch input. A single left-click or touch is all that's needed to
use the `File Selector`. A left-click or touch on a directory will change to
that directory. A left-click or touch on the up or down arrow will move the list
by one. A left-click or touch inbetween an arrow and the slider will move the
list by one page. Touch-and-hold to move the slider.

If you use the touch input, the selector looks like this

.. image:: /images/file-selector-01.png
   :align: center

.. note:: Make sure you use a QListWidget and not a QListView for the file
   selector.


`File, Error and Information Tutorial <https://youtu.be/kTFMM71VFuU>`_

Code Viewer
-----------

To add a code viewer, add a `QPlainTextEdit` from Input Widgets and name it
`gcode_pte`

.. image:: /images/gcode-viewer-01.png
   :align: center

MDI Viewer
----------

To add a MDI viewer, add a `QListWidget` from Item Widgets and name it
`mdi_history_lw`

.. image:: /images/mdi-viewer-01.png
   :align: center

To enter MDI commands, add a Line Edit and name it `mdi_command_le`.

Error Viewer
------------
To add an error viewer, add a `QPlainTextEdit` from Input Widgets and name it
`errors_pte`

.. image:: /images/error-viewer-01.png
   :align: center

To clear the error history, add a QPushButton and set the objectName to
`clear_errors_pb`.

To copy the errors to the clipboard, add a QPushButton and set the object name
to `copy_errors_pb`.

.. warning:: The error viewer must be a QPlainTextEdit not a QTextEdit.

Information Viewer
------------------

To add an information viewer, add a `QPlainTextEdit` from Input Widgets and name
it `info_pte`. Information messages from MSG, DEBUG and PRINT will show up in
the Information Viewer if it exists.

If `info_pte` is not found and the `errors_pte` is found, then information
messages will show up in the Error Viewer.

To clear the information viewer, add a QPushButton and name it `clear_info_pb`.

.. warning:: The information viewer must be a QPlainTextEdit not a QTextEdit.

Speed & Feed Calculators
------------------------

To add a milling Speeds and Feeds Calculator, add a `QFrame` or `QWidget` and
set the Object Name to `fsc_container`

.. image:: /images/fsc-02.png
   :align: center

To make the entry boxes touch-screen aware, add a Dynamic Property called 
`mode` and set the value to `touch`. Then when you touch an entry field, a 
numeric popup will show up to allow you to enter the value without a keyboard.

.. image:: /images/fsc-01.png
   :align: center


To add a Drill Feed and Speed calculator, add a `QFrame` or `QWidget` and set
the Object Name to `dsf_container`.

To make the entry boxes touch-screen aware, add a Dynamic Property called 
`mode` and set the value to `touch`. Then when you touch it, a numeric popup 
will appear, allowing you to enter the numbers

.. image:: /images/dsc-01.png
   :align: center

