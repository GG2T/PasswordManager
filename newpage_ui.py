# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import binascii
import hashlib
import json
from zxcvbn import zxcvbn

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QHeaderView, QMessageBox, QAbstractItemView


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
        show_page.resize(624,515)
        self.centralwidget = QtWidgets.QWidget(show_page)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 180, 601, 311))
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setProperty("showDropIndicator", True)
        self.tableView.setDragDropOverwriteMode(False)

        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.model = QtGui.QStandardItemModel(0, 4)
        self.model.setHorizontalHeaderLabels(['Category', 'Url', 'Username', 'Password'])
        self.tableView.setModel(self.model)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.clicked.connect(self.click_on_table)

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
        self.show_info_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_info_btn.setGeometry(QtCore.QRect(460, 130, 151, 31))
        self.show_info_btn.setObjectName("inject_btn")
        # self.show_info_btn.clicked.connect(self.check_strength)


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
        show_page.setWindowTitle(_translate("show_page", "PasswordManager--Get Password"))
        self.lineEdit_url.setPlaceholderText(_translate("show_page", "e.g., www.YouTube.com"))
        self.lineEdit_username.setPlaceholderText(_translate("show_page", "e.g., Alice101"))
        self.label_url.setText(_translate("show_page", "New URL"))
        self.label_username.setText(_translate("show_page", "New Username"))
        self.lineEdit_gpassword.setPlaceholderText(_translate("show_page", " <Show_Password>"))
        self.label_gpassword.setText(_translate("show_page", "Generated Password"))
        self.inject_btn.setText(_translate("show_page", "Inject"))
        self.show_info_btn.setText(_translate("show_page", "Check Strength"))
        self.back_btn.setText(_translate("show_page", "<-Back"))

    def click_on_table(self):

        dict1 = self.model.itemData(self.model.index(self.tableView.currentIndex().row(), 3))
        self.lineEdit_gpassword.setText(dict1[0])
        self.lineEdit_url.setText("")
        self.lineEdit_username.setText("")


    def read_urls_usernames(self):
        self.urls = self.raw_data[self.cata]["urls"]
        self.usernames = self.raw_data[self.cata]["usernames"]
        for i in range(len(self.urls)):
            self.model.appendRow([
                QStandardItem('%s' % self.cata),
                QStandardItem('%s' % self.urls[i]),
                QStandardItem('%s' % self.usernames[i]),
                QStandardItem('%s' % self.pwcalculation(self.string_code, self.urls[i], self.usernames[i]))
            ])
        # print(self.urls)

    def inject_url_username(self):
        if self.lineEdit_url.text() != "" and self.lineEdit_username.text() != "":
            url = self.lineEdit_url.text()
            username = self.lineEdit_username.text()
            password = self.pwcalculation(self.string_code, url, username)
            self.lineEdit_gpassword.setText(password)
            # if (url not in self.urls) or (username not in self.urls)

            self.model.appendRow([
                QStandardItem('%s' % self.cata),
                QStandardItem('%s' % url),
                QStandardItem('%s' % username),
                QStandardItem('%s' % password)
            ])
            self.urls.append(url)
            self.usernames.append(username)
            self.raw_data[self.cata]["urls"] = self.urls
            self.raw_data[self.cata]["usernames"] = self.usernames
            with open("store", "w") as f:
                f.write(json.dumps(self.raw_data))
        else:
            QMessageBox.warning(self.centralwidget,"Error","Please enter url and username")



    def pwcalculation(self, mastercode, url, username):
        conc = mastercode + url + username
        ha = hashlib.sha256(conc.encode("utf-8")).hexdigest()
        a = binascii.unhexlify(ha)
        # print(a.hex("-"))
        b = [int(x) for x in a]
        c = [(j % 127) % 94 + 33 for j in b]
        d = "".join([chr(z) for z in c])
        # print(d)
        return d[:12]

    # def save_to(self):
