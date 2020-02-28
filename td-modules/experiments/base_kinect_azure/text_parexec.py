# me - this DAT
# par - the Par object that has changed
# val - the current value
# prev - the previous value
# 
# Make sure the corresponding toggle is enabled in the Parameter Execute DAT.

windowOp = op('../window1')

def onValueChange(par, prev):
	# use par.eval() to get current value
	return

def onPulse(par):
	if par.name == 'Openwindow':
		windowOp.par.winopen.pulse()
	
	elif par.name == 'Closewindow':
		windowOp.par.winclose.pulse()
	return

def onExpressionChange(par, val, prev):
	return

def onExportChange(par, val, prev):
	return

def onEnableChange(par, val, prev):
	return

def onModeChange(par, val, prev):
	return
	