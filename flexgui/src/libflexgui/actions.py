import os, subprocess

from functools import partial

from PyQt5.QtWidgets import QApplication, QFileDialog

import linuxcnc

from libflexgui import dialogs

app = QApplication([])

def load_file(parent, gcode_file):
	parent.command.program_open(gcode_file)
	text = open(gcode_file).read()
	if parent.gcode_pte_exists:
		parent.gcode_pte.setPlainText(text)
	#parent.actionReload.setEnabled(True)
	base = os.path.basename(gcode_file)

	# get recent files from settings
	keys = parent.settings.allKeys()
	file_list = []
	for key in keys:
		if key.startswith('recent_files'):
			file_list.append(parent.settings.value(key))
	# if the g code file is in the list remove it
	if gcode_file in file_list:
		file_list.remove(gcode_file)
	# insert the g code file at the top of the list
	file_list.insert(0, gcode_file)
	# trim the list to 5
	file_list = file_list[:5]

	# add files back into settings
	parent.settings.beginGroup('recent_files')
	parent.settings.remove('')
	for i, item in enumerate(file_list):
		parent.settings.setValue(str(i), item)
	parent.settings.endGroup()

	# clear the recent menu
	parent.menuRecent.clear()

	# add the recent files from settings
	keys = parent.settings.allKeys()
	for key in keys:
		if key.startswith('recent_files'):
			path = parent.settings.value(key)
			name = os.path.basename(path)
			a = parent.menuRecent.addAction(name)
			a.triggered.connect(partial(load_file, parent, path))

def action_open(parent): # actionOpen
	if os.path.isdir(os.path.expanduser('~/linuxcnc/nc_files')):
		gcode_dir = os.path.expanduser('~/linuxcnc/nc_files')
	else:
		gcode_dir = os.path.expanduser('~/')
	gcode_file, file_type = QFileDialog.getOpenFileName(None,
	caption="Select G code File", directory=gcode_dir,
	filter='G code Files (*.ngc *.NGC);;All Files (*)', options=QFileDialog.DontUseNativeDialog,)
	if gcode_file: load_file(parent, gcode_file)

def action_edit(parent): # actionEdit
	parent.status.poll
	gcode_file = parent.status.file or False
	if not gcode_file:
		msg = ('No File is open.\nDo you want to open a file?')
		response = dialogs.warn_msg_yes_no(msg, 'No File Loaded')
		if response:
			action_open(parent)
			return
		else:
			return

	editor = parent.inifile.find('DISPLAY', 'EDITOR') or False
	if editor:
		cmd = ['which', editor]
		output = subprocess.run(cmd, capture_output=True, text=True)
		if output.returncode == 0:
			subprocess.Popen([editor, gcode_file])
		else: # FIXME get fancy and offer up and editor that's installed
			msg = ('The Editor configured in the ini file\n'
				'is not installed.')
			dialogs.warn_msg_ok(msg, 'Error')
	else:
		msg = ('No Editor was found\nin the ini Display section')
		dialogs.warn_msg_ok(msg, 'Editor')

def action_reload(parent): # actionReload
	parent.status.poll
	gcode_file = parent.status.file or False
	if gcode_file:
		parent.status.poll()
		if len(parent.status.file) > 0:
			if parent.status.task_mode != linuxcnc.MODE_MANUAL:
				parent.command.mode(linuxcnc.MODE_MANUAL)
				parent.command.wait_complete()
			gcode_file = parent.status.file 
			# Force a sync of the interpreter, which writes out the var file.
			parent.command.task_plan_synch()
			parent.command.wait_complete()
			parent.command.program_open(gcode_file)
		parent.command.program_open(gcode_file)
		text = open(gcode_file).read()
		if parent.gcode_pte_exists:
			parent.gcode_pte.setPlainText(text)

	else:
		msg = ('No File is open to reload')
		response = dialogs.warn_msg_ok(msg, 'Error')

def action_save_as(parent): # actionSave_As
	print(parent.sender().objectName())

def action_edit_tool_table(parent): # actionEdit_Tool_Table
	print(parent.sender().objectName())

def action_reload_tool_table(parent): # actionReload_Tool_Table
	print(parent.sender().objectName())

def action_ladder_editor(parent): # actionLadder_Editor
	print(parent.sender().objectName())

def action_quit(parent): # actionQuit
	print(parent.sender().objectName())

def action_clear_mdi(parent): # actionClear_MDI
	print(parent.sender().objectName())

def action_copy_mdi(parent): # actionCopy_MDI
	print(parent.sender().objectName())

def action_show_hal(parent): # actionShow_HAL
	print(parent.sender().objectName())
	# subprocess.Popen(r'c:\mytool\tool.exe', cwd=r'd:\test\local')
	# os.path.dirname(os.path.realpath(__file__)) 

def action_hal_meter(parent): # actionHal_Meter
	print(parent.sender().objectName())

def action_hal_scope(parent): # actionHal_Scope
	print(parent.sender().objectName())

def action_about(parent): # actionAbout
	print(parent.sender().objectName())

def action_quick_reference(parent): # actionQuick_Reference
	print(parent.sender().objectName())


