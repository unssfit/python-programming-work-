import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setGeometry(50,50,500,400)
window.setWindowTitle("hello YOUNESS")

window.show()


sys.exit(app.exec_())
