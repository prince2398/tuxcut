import sys
from PyQt4 import QtGui
from TuxCut import TuxCut

app = QtGui.QApplication(sys.argv)
tux = TuxCut()
sys.exit(app.exec_())