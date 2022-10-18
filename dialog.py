# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tanchuang.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog,thing):
        Dialog.setObjectName("Dialog")
        Dialog.resize(563, 472)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(0, 6, 561, 461))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 559, 459))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textinside = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textinside.setGeometry(QtCore.QRect(3, 6, 551, 451))
        self.textinside.setReadOnly(True)
        self.textinside.setObjectName("textinside")
        self.textinside.setText(thing)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


