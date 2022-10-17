# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passwordmanager.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QInputDialog, QMessageBox
from PIL import Image
import hashlib
import json
from pathlib import Path

from base64 import b64encode

from PIL.ImageQt import ImageQt


class MyQLabel(QtWidgets.QLabel):
    button_clicked_signal = QtCore.pyqtSignal(str)
    coord = ""

    def __init__(self, parent=None):
        super(MyQLabel, self).__init__(parent)

    def mousePressEvent(self, QMouseEvent):
        self.button_clicked_signal.emit(self.coord)

    #
    # 可在外部与槽函数连接
    def connect_customized_slot(self, func):
        self.button_clicked_signal.connect(func)


class Ui_Login_page(object):

    def __init__(self):
        self.d = {}
        self.gridLayout = None
        self.gridLayoutWidget = None
        self.centralwidget = None
        self.img_path = ""
        self.storage = []
        self.record_table = {}


    def setupUi(self, Login_page):
        self.password_list = set()

        self.img_path = ""
        Login_page.setObjectName("Login_page")
        Login_page.resize(937, 673)
        self.centralwidget = QtWidgets.QWidget(Login_page)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 110, 651, 521))
        # self.gridLayoutWidget.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.d = {}
        for i in range(8):
            for j in range(8):
                self.d["label" + str(i) + str(j)] = MyQLabel(self.gridLayoutWidget)
                self.d["label" + str(i) + str(j)].setObjectName("label" + str(i) + str(j))
                self.gridLayout.addWidget(self.d["label" + str(i) + str(j)], i, j, 1, 1)
                self.d["label" + str(i) + str(j)].connect_customized_slot(self.selected_coordinate)
                self.d["label" + str(i) + str(j)].coord = str(i) + str(j)
                # self.d["label" + str(i) + str(j)].mousePressEvent(str(i))

        self.New_btn = QtWidgets.QPushButton(self.centralwidget)
        self.New_btn.setEnabled(True)
        self.New_btn.setGeometry(QtCore.QRect(50, 50, 191, 28))
        self.New_btn.setObjectName("New_btn")
        self.New_btn.clicked.connect(self.new_catalogue)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(280, 50, 231, 31))
        self.comboBox.setAcceptDrops(True)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        # self.infor = ["Or select an exist catalogue"]
        # self.comboBox.addItems(self.infor)
        self.comboBox.addItem("Or select an exist catalogue")

        self.import_btn = QtWidgets.QPushButton(self.centralwidget)
        self.import_btn.setGeometry(QtCore.QRect(750, 235, 131, 81))
        self.import_btn.setObjectName("import_btn")
        self.import_btn.clicked.connect(self.import_pic)
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(750, 350, 131, 81))
        self.save_btn.setObjectName("save_btn")
        self.save_btn.clicked.connect(self.save_catalogue)
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(750, 120, 131, 81))
        # self.clear_btn.setCheckable(True)
        self.clear_btn.setObjectName("clear_btn")
        self.clear_btn.clicked.connect(self.clear_select)

        Login_page.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(Login_page)
        self.statusBar.setObjectName("statusBar")
        Login_page.setStatusBar(self.statusBar)

        self.retranslateUi(Login_page)
        self.read_storage()
        QtCore.QMetaObject.connectSlotsByName(Login_page)


    def retranslateUi(self, Login_page):
        _translate = QtCore.QCoreApplication.translate
        Login_page.setWindowTitle(_translate("Login_page", "PasswordManager--Login"))
        for i in range(8):
            for j in range(8):
                self.d["label" + str(i) + str(j)].setText(str(i) + str(j))

        self.New_btn.setText(_translate("Login_page", "Set a new catalogue"))
        # self.comboBox.setCurrentText(_translate("Login_page", "Or select an exist catalogue"))
        # self.comboBox.setItemText(0, _translate("Login_page", "Or select an exist catalogue"))
        self.import_btn.setText(_translate("Login_page", "Import picture"))
        self.save_btn.setText(_translate("Login_page", "Save"))
        self.clear_btn.setText(_translate("Login_page", "Clear"))


    def read_storage(self):
        my_file = Path("store")
        if my_file.is_file():
            try:
                with open("store", "r") as file:
                    self.storage = json.loads(file.read())[0]

                list_cata = self.storage.keys()
                self.comboBox.addItems(list_cata)
                # self.comboBox.


            except Exception as e:
                QMessageBox.warning(self.centralwidget, 'Error',
                                    f'The following error occurred:\n{type(e)}: {e}')
        else:
            pass






    def save_catalogue(self):
        try:
            if self.comboBox.currentIndex() == 0:
                raise ValueError("Plase select an catalogue or Create one")
            if self.img_path == "":
                raise ValueError("please choose a picture first")
            if len(self.password_list) == 0:
                raise ValueError("You need to select your password")


            # image = Image.open(self.img_path)
            # image = image.resize((651, 651), Image.ANTIALIAS)
            try:
                with open(self.img_path, 'rb') as jpg_file:
                    byte_content = jpg_file.read()
                base64_bytes = b64encode(byte_content)
                base64_string = base64_bytes.decode('utf-8')
                raw_data = {}
                p = sorted(list(self.password_list))
                print(p)
                key = "".join(p)

                # raw_data["Catalogue"] = self.comboBox.currentText()
                # raw_data["Password"] = hashlib.md5(key.encode("utf-8")).hexdigest()
                # raw_data["image"] = base64_string
                raw_data[self.comboBox.currentText()] = {"Password":hashlib.md5(key.encode("utf-8")).hexdigest(),"image":base64_string}
                self.storage.append(raw_data)
                with open("store","w") as f:
                    f.write(json.dumps(self.storage))



                print("read")
            except Exception as e:
                QMessageBox.warning(self.centralwidget, 'Error',
                                    f'The following error occurred:\n{type(e)}: {e}')
        # else:
        #     QMessageBox.warning(self.centralwidget, 'Error',
        #                         "please choose a picture first")
        except ValueError as e:
            QMessageBox.warning(self.centralwidget, 'Error', repr(e))






    def clear_pic(self):
        for i in range(8):
            for j in range(8):
                self.d["label" + str(i) + str(j)].clear()
                self.d["label" + str(i) + str(j)].setText(str(i) + str(j))

    def new_catalogue(self):
        text, ok = QInputDialog.getText(self.centralwidget, 'Text Input Dialog', 'Set a new catalogue')
        if ok:
            # list1 = self.comboBox.
            self.comboBox.addItem(text)
            self.comboBox.setCurrentText(text)
            self.clear_pic()
            self.clear_select()

        else:
            pass

    def selected_coordinate(self, coord):

        self.d["label" + coord].setFrameShape(QtWidgets.QFrame.Shape.Box)
        # self.d["label" + coord].setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.d["label" + coord].setLineWidth(2)
        self.password_list.add(coord)
        print(self.password_list)

    def clear_select(self):
        for i in range(8):
            for j in range(8):
                self.d["label" + str(i) + str(j)].setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.password_list.clear()

    def cut_image(self, image):
        width, height = image.size
        item_width = int(width / 8)
        box_list = []
        # (left, upper, right, lower)
        for i in range(0, 8):  # 两重循环，生成9张图片基于原图的位置
            for j in range(0, 8):
                # print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))
                box = (j * item_width, i * item_width, (j + 1) * item_width, (i + 1) * item_width)
                box_list.append(box)
        image_list = [image.crop(box) for box in box_list]
        return image_list

    def import_pic(self):

        self.img_path, imgtype = QFileDialog.getOpenFileName(self.centralwidget, "Select a picture", "",
                                                              "*.jpg;;*.png")
        try:
            image = Image.open(self.img_path)

            image = image.resize((651, 651), Image.ANTIALIAS)

            # image.show()
            # image = self.fill_image()
            image_list = self.cut_image(image)

            index = 0
            # pixmap = ImageQt(image_list[0])
            # pixmap = PIL.ImageQt.
            # self.d["label00"].setPixmap(image_list[0])

            for i in range(8):
                for j in range(8):
                    im = image_list[index].convert("RGBA")
                    pix = QtGui.QPixmap.fromImage(ImageQt(im))
                    self.d["label" + str(i) + str(j)].setPixmap(pix)
                    index += 1

        except Exception as e:
            QMessageBox.warning(self.centralwidget, 'Error',
                                f'The following error occurred:\n{type(e)}: {e}')


