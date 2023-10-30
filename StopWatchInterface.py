#libaries
from PyQt5 import QtCore, QtGui, QtWidgets
import datetime

#local
from QtUi import Ui_MainWindow
import storetime

class InflatedStopwatchInterface(Ui_MainWindow):
    INTERVAL = 1000
    LOG_PATH = "C:\\Users\\Alonso\\Documents\\Code\\Python\\working_hours.log"
    DATE_FORMAT = "%Y-%m-%d"
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.today = datetime.datetime.today()
        self.seconder = QtCore.QTimer()
        self.counter = storetime.Time()

        self.display()
    #end def

    # -- Behaviors
    def display(self):
        self.lcdTime.display(str(self.counter))
    #end def

    def log(self):
        with open(self.LOG_PATH, "a") as log_file:
            log_file.write("%s, %s\n" 
                %(self.today.strftime(self.DATE_FORMAT),
                str(self.counter)
            ))
        #end with
    #end def

    # -- Events
    def addSecond(self):
        self.seconder.start(self.INTERVAL)
        self.counter.addSecond()
        self.display()
    #end def

    def clickStart(self):
        self.seconder.start(self.INTERVAL)
    #end def

    def clickPause(self):
        self.seconder.stop()
    #end def

    def clickStop(self):
        self.seconder.stop()
        if not self.counter.isReset():
            self.log()
        #end if
        self.counter.reset()
        self.display()
    #end def

    def clickClose(self):
        self.clickStop()
    #end def
#end class
