from UI.ui_main import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5 import QtCore

class View(QWidget):
    def __init__(self):
        self.app = QApplication(sys.argv)
        QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.header.installEventFilter(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.moved = False
        self.ui.baud_rate.addItems([str(50), str(75), str(110), str(134), str(150), str(200), str(300),\
             str(600), str(1200), str(1800), str(2400), str(4800), str(9600), str(19200), str(38400), str(57600), str(115200)])
        self.ui.baud_rate.setCurrentText('9600')
     
    def start_app(self):
        self.show()
        sys.exit(self.app.exec_())
    
    def eventFilter(self, obj, event) -> bool:
        if obj == self.ui.header:
            if self.ui.close.underMouse():
                    return True
            elif self.ui.max.underMouse():
                        return True
            elif self.ui.min.underMouse():
                    return True
            elif self.ui.settings.underMouse():
                    return True
            else:
                if event.type() == QtCore.QEvent.MouseButtonRelease:
                     if event.globalPos().y() < 10 and self.moved:
                        self.prevGeo = self.geometry()
                        self.showMaximized()
                        return True

                elif event.type() == QtCore.QEvent.MouseButtonDblClick:
                    self.setWindowState(self.windowState() ^ QtCore.Qt.WindowFullScreen)
                    return True
                elif event.type() == QtCore.QEvent.MouseButtonPress:
                        self.oldPosition = event.globalPos()
                elif event.type() == QtCore.QEvent.MouseMove:
                    delta = QtCore.QPoint(event.globalPos() - self.oldPosition)
                    self.move(self.x() + delta.x(), self.y() + delta.y())
                    self.oldPosition = event.globalPos()
                    self.moved = True
                else:
                    return True
            
        return True
    
    def ui_controls(self, controller):
         self.ui.close.clicked.connect(lambda:controller.on_close_run(self.close))
         self.ui.baud_rate.currentIndexChanged.connect(lambda:controller.switch_baurd_rate(self.ui.baud_rate.currentText()))
         self.ui.port_number.currentIndexChanged.connect(lambda:controller.switch_port(self.ui.port_number.currentText()))
         self.ui.stopstart.clicked.connect(controller.start_stop_reading_data)