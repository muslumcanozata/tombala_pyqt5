# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import Tombala

import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(808, 568)
        MainWindow.setMinimumSize(QtCore.QSize(808, 568))
        MainWindow.setFixedSize(808, 568)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(808, 507))
        self.centralwidget.setMaximumSize(QtCore.QSize(808, 540))
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 80, 111, 111))
        self.label.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: #333;\n"
"border: 2px solid #ff7f00;\n"
"    border-radius: 50%;\n"
"    width: 200px;\n"
"    height: 200px; \n"
"border-style: outset;\n"
"background: #ff7f00;\n"
"padding: 5px;\n"
"")
        self.label.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 371, 181))
        self.label_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setPixmap(QtGui.QPixmap("tombala1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 280, 371, 181))
        self.label_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_3.setText("")
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setPixmap(QtGui.QPixmap("tombala2.jpeg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 56, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(107, 57, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(True)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(188, 58, 40, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(True)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(266, 59, 40, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(True)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(307, 59, 41, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setAutoFillBackground(True)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(66, 108, 40, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_9.setFont(font)
        self.label_9.setAutoFillBackground(True)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(148, 109, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_10.setFont(font)
        self.label_10.setAutoFillBackground(True)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(224, 109, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setAutoFillBackground(True)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(306, 110, 40, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_12.setFont(font)
        self.label_12.setAutoFillBackground(True)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(345, 111, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_13.setFont(font)
        self.label_13.setAutoFillBackground(True)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(29, 160, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_14.setFont(font)
        self.label_14.setAutoFillBackground(True)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(104, 161, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_15.setFont(font)
        self.label_15.setAutoFillBackground(True)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(185, 161, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_16.setFont(font)
        self.label_16.setAutoFillBackground(True)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(263, 161, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_17.setFont(font)
        self.label_17.setAutoFillBackground(True)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(345, 162, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_18.setFont(font)
        self.label_18.setAutoFillBackground(True)
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(18, 290, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_19.setFont(font)
        self.label_19.setAutoFillBackground(True)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(98, 290, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_20.setFont(font)
        self.label_20.setAutoFillBackground(True)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(178, 290, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_21.setFont(font)
        self.label_21.setAutoFillBackground(True)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(255, 290, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_22.setFont(font)
        self.label_22.setAutoFillBackground(True)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(297, 290, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_23.setFont(font)
        self.label_23.setAutoFillBackground(True)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(57, 347, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_24.setFont(font)
        self.label_24.setAutoFillBackground(True)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(137, 347, 42, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_25.setFont(font)
        self.label_25.setAutoFillBackground(True)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(216, 345, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_26.setFont(font)
        self.label_26.setAutoFillBackground(True)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(295, 345, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_27.setFont(font)
        self.label_27.setAutoFillBackground(True)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(337, 345, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_28.setFont(font)
        self.label_28.setAutoFillBackground(True)
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(15, 401, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_29.setFont(font)
        self.label_29.setAutoFillBackground(True)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(98, 401, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_30.setFont(font)
        self.label_30.setAutoFillBackground(True)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(178, 401, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_31.setFont(font)
        self.label_31.setAutoFillBackground(True)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(257, 401, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_32.setFont(font)
        self.label_32.setAutoFillBackground(True)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(336, 401, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_33.setFont(font)
        self.label_33.setAutoFillBackground(True)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(440, 30, 181, 221))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.InitializeCards)
        self.pushButton.setEnabled(False)

        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.setEnabled(False)
        self.pushButton_2.clicked.connect(self.pickButton)

        self.verticalLayout.addWidget(self.pushButton_2)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(460, 310, 331, 81))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_34 = QtWidgets.QLabel(self.widget1)
        self.label_34.setObjectName("label_34")
        self.horizontalLayout.addWidget(self.label_34)
        self.label_35 = QtWidgets.QLabel(self.widget1)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout.addWidget(self.label_35)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_36 = QtWidgets.QLabel(self.widget1)
        self.label_36.setObjectName("label_36")
        self.horizontalLayout_2.addWidget(self.label_36)
        self.label_37 = QtWidgets.QLabel(self.widget1)
        self.label_37.setObjectName("label_37")
        self.horizontalLayout_2.addWidget(self.label_37)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(610, 500, 186, 27))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_4.clicked.connect(self.endGame)
        self.pushButton_4.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(self.newGame)

        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.label_3.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.label_27.raise_()
        self.label_28.raise_()
        self.label_29.raise_()
        self.label_30.raise_()
        self.label_31.raise_()
        self.label_32.raise_()
        self.label_33.raise_()
        self.label_34.raise_()
        self.label_35.raise_()
        self.label_36.raise_()
        self.label_37.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.Player1 = Tombala.Stamp()
        self.Player2 = Tombala.Stamp()

        

        self.listLabel = list()
        
        j = 4
        for i in range(30):
            self.listLabel.append(getattr(self, "label_%d" %(j)))
            j+=1
        for i in range(30):
            self.listLabel[i].setAutoFillBackground(True)
            
    
    def InitializeCards(self):
        self.pushButton_2.setEnabled(True)
        self.pushButton.setEnabled(False)
        self.Player1.generateRandomNumber()
        self.Player2.generateRandomNumber()
        i=0
        for x in range(3):
            for y in range(5):
                self.listLabel[i].setText(str(self.Player1.getStampValue(x, y)))
                i+=1
        for x in range(3):
            for y in range(5):
                self.listLabel[i].setText(str(self.Player2.getStampValue(x, y)))
                i+=1


    def pickButton(self):
        numb = self.Player1.takeRandom()
        self.label.setText(str(numb))
        self.Player1.checkTakenNumber(numb)
        self.Player2.checkTakenNumber(numb)
        i=0
        for x in range(3):
            for y in range(5):
                self.listLabel[i].setText(str(self.Player1.getStampValue(x, y)))
                if self.listLabel[i] == 0:
                    self.listLabel[i].setStyleSheet("QLabel = { background-color : black }")
                i+=1
        for x in range(3):
            for y in range(5):
                self.listLabel[i].setText(str(self.Player2.getStampValue(x, y)))
                i+=1
        self.Player1.checkBingo()
        self.Player2.checkBingo()
        self.setPoints()

    def setPoints(self):
        self.label_36.setText(str(self.Player1.getPoint()) + " Puan")
        self.label_37.setText(str(self.Player2.getPoint()) + " Puan")
        if self.label_36.text() == "70 Puan":
            if self.label_37.text() == "70 Puan":
                self.label_36.setText("Scoreless")
                self.label_37.setText("Scoreless")
                self.finish()
            else:
                self.label_36.setText("Won")
                self.finish()
        elif self.label_37.text() == "70 Puan":
            self.label_37.setText("Won")
            self.finish()

                
                
            
            

    def finish(self):
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_3.setEnabled(True)

    #new game button function
    def newGame(self):
        self.Player1 = Tombala.Stamp()
        self.Player2 = Tombala.Stamp()
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(True)
        self.pushButton.setEnabled(True)
        self.label_36.setText("0 Puan")
        self.label_37.setText("0 Puan")

        for i in range(30):
            self.listLabel[i].setText("")

    #end game button function
    def endGame(self):
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_3.setEnabled(True)

        for i in range(30):
            self.listLabel[i].setText("")
        

    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tombala Game"))
        self.label.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "0"))
        self.label_12.setText(_translate("MainWindow", "0"))
        self.label_13.setText(_translate("MainWindow", "0"))
        self.label_14.setText(_translate("MainWindow", "0"))
        self.label_15.setText(_translate("MainWindow", "0"))
        self.label_16.setText(_translate("MainWindow", "0"))
        self.label_17.setText(_translate("MainWindow", "0"))
        self.label_18.setText(_translate("MainWindow", "0"))
        self.label_19.setText(_translate("MainWindow", "0"))
        self.label_20.setText(_translate("MainWindow", "0"))
        self.label_21.setText(_translate("MainWindow", "0"))
        self.label_22.setText(_translate("MainWindow", "0"))
        self.label_23.setText(_translate("MainWindow", "0"))
        self.label_24.setText(_translate("MainWindow", "0"))
        self.label_25.setText(_translate("MainWindow", "0"))
        self.label_26.setText(_translate("MainWindow", "0"))
        self.label_27.setText(_translate("MainWindow", "0"))
        self.label_28.setText(_translate("MainWindow", "0"))
        self.label_29.setText(_translate("MainWindow", "0"))
        self.label_30.setText(_translate("MainWindow", "0"))
        self.label_31.setText(_translate("MainWindow", "0"))
        self.label_32.setText(_translate("MainWindow", "0"))
        self.label_33.setText(_translate("MainWindow", "0"))
        self.pushButton.setText(_translate("MainWindow", "Initialize Cards"))
        self.pushButton_2.setText(_translate("MainWindow", "Pick"))
        self.label_34.setText(_translate("MainWindow", "Player 1"))
        self.label_35.setText(_translate("MainWindow", "Player 2"))
        self.label_36.setText(_translate("MainWindow", "0 Puan"))
        self.label_37.setText(_translate("MainWindow", "0 Puan"))
        self.pushButton_4.setText(_translate("MainWindow", "End Game"))
        self.pushButton_3.setText(_translate("MainWindow", "New Game"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
