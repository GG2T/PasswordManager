# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import binascii
import hashlib

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_show_page(object):

    def __init__(self):
        self.string_code = ""
        self.raw_data = dict()
        self.urls = []
        self.usernames = []
        self.cata = ""

    def set_string_code(self, string_code, cata):
        self.string_code = string_code
        self.cata = cata

    def set_raw_data(self, raw_data):
        self.raw_data = raw_data

    def setupUi(self, show_page):
        show_page.setObjectName("show_page")
        show_page.resize(624, 491)
        self.centralwidget = QtWidgets.QWidget(show_page)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 180, 601, 311))
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setProperty("showDropIndicator", False)
        self.tableView.setDragDropOverwriteMode(False)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setCascadingSectionResizes(True)
        self.lineEdit_url = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_url.setGeometry(QtCore.QRect(200, 50, 251, 31))
        self.lineEdit_url.setObjectName("lineEdit_url")
        self.lineEdit_username = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_username.setGeometry(QtCore.QRect(200, 90, 251, 31))
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.label_url = QtWidgets.QLabel(self.centralwidget)
        self.label_url.setGeometry(QtCore.QRect(130, 50, 61, 31))
        self.label_url.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_url.setObjectName("label_url")
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setGeometry(QtCore.QRect(90, 90, 101, 31))
        self.label_username.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_username.setObjectName("label_username")
        self.lineEdit_gpassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_gpassword.setGeometry(QtCore.QRect(200, 130, 251, 31))
        self.lineEdit_gpassword.setText("")
        self.lineEdit_gpassword.setReadOnly(True)
        self.lineEdit_gpassword.setObjectName("lineEdit_gpassword")
        self.label_gpassword = QtWidgets.QLabel(self.centralwidget)
        self.label_gpassword.setGeometry(QtCore.QRect(40, 130, 151, 31))
        self.label_gpassword.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_gpassword.setObjectName("label_gpassword")
        self.inject_btn = QtWidgets.QPushButton(self.centralwidget)
        self.inject_btn.setGeometry(QtCore.QRect(460, 50, 151, 71))
        self.inject_btn.setObjectName("inject_btn")
        self.inject_btn.clicked.connect(self.inject_url_username)
        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(10, 10, 71, 28))
        self.back_btn.setObjectName("back_btn")
        show_page.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(show_page)
        self.statusBar.setObjectName("statusBar")
        show_page.setStatusBar(self.statusBar)

        self.retranslateUi(show_page)

        QtCore.QMetaObject.connectSlotsByName(show_page)

    def retranslateUi(self, show_page):
        _translate = QtCore.QCoreApplication.translate
        show_page.setWindowTitle(_translate("show_page", "PasswordManager--Login"))
        self.lineEdit_url.setPlaceholderText(_translate("show_page", " <YouTube>"))
        self.lineEdit_username.setPlaceholderText(_translate("show_page", " <Master_Ma_Bao_Guo>"))
        self.label_url.setText(_translate("show_page", "New URL"))
        self.label_username.setText(_translate("show_page", "New Username"))
        self.lineEdit_gpassword.setPlaceholderText(_translate("show_page", " <Please click Inject>"))
        self.label_gpassword.setText(_translate("show_page", "Generated Password"))
        self.inject_btn.setText(_translate("show_page", "Inject"))
        self.back_btn.setText(_translate("show_page", "<-Back"))

    def read_urls_usernames(self):
        self.urls = self.raw_data[self.cata]["urls"]
        self.usernames = self.raw_data[self.cata]["usernames"]
        # print(self.urls)

    def inject_url_username(self):
        url = self.lineEdit_url.text()
        username = self.lineEdit_username.text()
        password = self.pwcalculation(self.string_code,url,username)
        self.lineEdit_gpassword.setText(password)

    def pwcalculation(self,mastercode,url,username):
        conc = mastercode + url + username
        ha = hashlib.sha256(conc.encode("utf-8")).hexdigest()
        a = binascii.unhexlify(ha)
        print(a.hex("-"))
        b = [int(x) for x in a]
        c = [(j % 127) % 94 + 33 for j in b]
        d = "".join([chr(z) for z in c])
        print(d)
        return d[:12]
