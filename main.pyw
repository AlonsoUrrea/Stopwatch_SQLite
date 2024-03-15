#libaries
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# local
from StopWatchInterface import InflatedStopwatchInterface

app = QtWidgets.QApplication(sys.argv)
main_window = QtWidgets.QMainWindow() # ventana principal
ui = InflatedStopwatchInterface()
ui.setupUi(main_window)
ui.setupDb()

ui.seconder.timeout.connect(ui.addSecond)
ui.btnStart.clicked.connect(ui.clickStart)
ui.btnPause.clicked.connect(ui.clickPause)
ui.btnStop.clicked.connect(ui.clickStop)
app.aboutToQuit.connect(ui.clickClose)

main_window.show()
sys.exit(app.exec_())