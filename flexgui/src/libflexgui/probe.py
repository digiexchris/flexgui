import linuxcnc as emc

def toggle(parent):
	if parent.sender().isChecked():
		for item in parent.probe_controls:
			getattr(parent, item).setEnabled(True)
		parent.spindle_speed = 0
		if 'spindle_speed_lb' in parent.children:
			parent.spindle_speed_lb.setText(f'{parent.spindle_speed}')
		parent.command.spindle(emc.SPINDLE_OFF)

	else:
		for item in parent.probe_controls:
			getattr(parent, item).setEnabled(False)

