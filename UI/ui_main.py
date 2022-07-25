from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from UI import icons

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(678, 416)
        self.verticalLayout_6 = QVBoxLayout(Form)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.frame)
        self.header.setObjectName(u"header")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.header)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.header)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3, 0, Qt.AlignLeft)

        self.widget = QWidget(self.frame_7)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.settings = QPushButton(self.widget)
        self.settings.setObjectName(u"settings")
        self.settings.setMaximumSize(QSize(28, 28))
        icon = QIcon()
        icon.addFile(u":/images/images/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon)

        self.horizontalLayout.addWidget(self.settings)

        self.min = QPushButton(self.widget)
        self.min.setObjectName(u"min")
        self.min.setMaximumSize(QSize(28, 28))
        icon1 = QIcon()
        icon1.addFile(u":/images/images/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.min.setIcon(icon1)

        self.horizontalLayout.addWidget(self.min)

        self.max = QPushButton(self.widget)
        self.max.setObjectName(u"max")
        self.max.setMaximumSize(QSize(28, 28))
        icon2 = QIcon()
        icon2.addFile(u":/images/images/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.max.setIcon(icon2)

        self.horizontalLayout.addWidget(self.max)

        self.close = QPushButton(self.widget)
        self.close.setObjectName(u"close")
        self.close.setMaximumSize(QSize(28, 28))
        icon3 = QIcon()
        icon3.addFile(u":/images/images/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon3)

        self.horizontalLayout.addWidget(self.close)


        self.horizontalLayout_4.addWidget(self.widget, 0, Qt.AlignRight)


        self.horizontalLayout_3.addWidget(self.frame_7)


        self.verticalLayout_4.addWidget(self.frame_6)


        self.verticalLayout_5.addWidget(self.header)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.display_table = QTableWidget(self.frame_3)
        if (self.display_table.columnCount() < 2):
            self.display_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.display_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.display_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.display_table.rowCount() < 9):
            self.display_table.setRowCount(9)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.display_table.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.display_table.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.display_table.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.display_table.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.display_table.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.display_table.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.display_table.setVerticalHeaderItem(6, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.display_table.setVerticalHeaderItem(7, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.display_table.setVerticalHeaderItem(8, __qtablewidgetitem10)
        self.display_table.setObjectName(u"display_table")
        self.display_table.setGeometry(QRect(35, 35, 203, 300))
        sizePolicy.setHeightForWidth(self.display_table.sizePolicy().hasHeightForWidth())
        self.display_table.setSizePolicy(sizePolicy)
        self.display_table.setMinimumSize(QSize(0, 0))
        self.display_table.setMaximumSize(QSize(203, 300))
        self.display_table.horizontalHeader().setVisible(True)
        self.display_table.verticalHeader().setVisible(False)
        self.widget1 = QWidget(self.frame_3)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(273, 42, 372, 148))
        self.gridLayout = QGridLayout(self.widget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget1)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.baud_rate = QComboBox(self.widget1)
        self.baud_rate.setObjectName(u"baud_rate")

        self.gridLayout.addWidget(self.baud_rate, 1, 1, 1, 1)

        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.port_number = QComboBox(self.widget1)
        self.port_number.setObjectName(u"port_number")

        self.gridLayout.addWidget(self.port_number, 2, 1, 1, 1)

        self.stopstart = QPushButton(self.widget1)
        self.stopstart.setObjectName(u"stopstart")

        self.gridLayout.addWidget(self.stopstart, 3, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_6.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Serial port streaming ", None))
        self.settings.setText("")
        self.min.setText("")
        self.max.setText("")
        self.close.setText("")
        ___qtablewidgetitem = self.display_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Parameter", None));
        ___qtablewidgetitem1 = self.display_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"value", None));
        ___qtablewidgetitem2 = self.display_table.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem3 = self.display_table.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem4 = self.display_table.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem5 = self.display_table.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem6 = self.display_table.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem7 = self.display_table.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem8 = self.display_table.verticalHeaderItem(6)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem9 = self.display_table.verticalHeaderItem(7)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"New Row", None));
        ___qtablewidgetitem10 = self.display_table.verticalHeaderItem(8)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"New Row", None));
        self.label_4.setText(QCoreApplication.translate("Form", u"Control setting", None))
        self.label.setText(QCoreApplication.translate("Form", u"Baud rate", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Port number", None))
        self.stopstart.setText(QCoreApplication.translate("Form", u"Stop streaming", None))
    # retranslateUi


