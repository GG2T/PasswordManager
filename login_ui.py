# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passwordmanager.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PIL import Image
# from PIL.ImageQt import ImageQt

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

    # def __init__(self):
    #     self.statusBar = None
    #     self.clear_btn = None
    #     self.save_btn = None
    #     self.import_btn = None
    #     self.d = None
    #     self.gridLayout = None
    #     self.gridLayoutWidget = None
    #     self.centralwidget = None
    #     self.password_list = None
    #     self.comboBox = None
    #     self.New_btn = None

    def setupUi(self, Login_page):
        self.password_list = set()
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
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(280, 50, 231, 31))
        self.comboBox.setAcceptDrops(True)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.import_btn = QtWidgets.QPushButton(self.centralwidget)
        self.import_btn.setGeometry(QtCore.QRect(750, 235, 131, 81))
        self.import_btn.setObjectName("import_btn")
        self.import_btn.clicked.connect(self.import_pic)
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(750, 350, 131, 81))
        self.save_btn.setObjectName("save_btn")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(750, 120, 131, 81))
        self.clear_btn.setCheckable(True)
        self.clear_btn.setObjectName("clear_btn")
        self.clear_btn.clicked.connect(self.clear_select)

        Login_page.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(Login_page)
        self.statusBar.setObjectName("statusBar")
        Login_page.setStatusBar(self.statusBar)

        self.retranslateUi(Login_page)
        QtCore.QMetaObject.connectSlotsByName(Login_page)

    def retranslateUi(self, Login_page):
        _translate = QtCore.QCoreApplication.translate
        Login_page.setWindowTitle(_translate("Login_page", "PasswordManager--Login"))
        for i in range(8):
            for j in range(8):
                self.d["label" + str(i) + str(j)].setText(str(i) + str(j))

        self.New_btn.setText(_translate("Login_page", "Set a new catalogue"))
        self.comboBox.setCurrentText(_translate("Login_page", "Or select an exist catalogue"))
        self.comboBox.setItemText(0, _translate("Login_page", "Or select an exist catalogue"))
        self.import_btn.setText(_translate("Login_page", "Import picture"))
        self.save_btn.setText(_translate("Login_page", "Save"))
        self.clear_btn.setText(_translate("Login_page", "Clear"))

    def selected_coordinate(self, coord):

        self.d["label" + coord].setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.password_list.add(coord)
        print(self.password_list)

    def clear_select(self):
        for i in range(8):
            for j in range(8):
                self.d["label" + str(i) + str(j)].setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.password_list.clear()

    def fill_image(self,image):
        width, height = image.size
        # 选取长和宽中较大值作为新图片的
        new_image_length = width if width > height else height
        # 生成新图片[白底]
        new_image = Image.new(image.mode, (new_image_length, new_image_length), color='white')
        # 将之前的图粘贴在新图上，居中
        if width > height:  # 原图宽大于高，则填充图片的竖直维度
            # (x,y)二元组表示粘贴上图相对下图的起始位置
            new_image.paste(image, (0, int((new_image_length - height) / 2)))
        else:
            new_image.paste(image, (int((new_image_length - width) / 2), 0))
        return new_image
    def cut_image(self,image):
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
        imgname, imgtype = QFileDialog.getOpenFileNames(self.centralwidget, "Select a picture", "", "*.jpg;;*.png;;All Files(*)")
        image = Image.open(imgname[0])
        image = image.resize((651, 651),Image.ANTIALIAS)


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

