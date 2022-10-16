from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import login_ui

class loginApp(QtWidgets.QMainWindow, login_ui.Ui_Login_page):
    def __init__(self, parent=None):
        super(loginApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = loginApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()