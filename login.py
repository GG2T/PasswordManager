from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import login_ui
import newpage_ui


class loginApp(QtWidgets.QMainWindow, login_ui.Ui_Login_page):
    switch_window1 = QtCore.pyqtSignal()  # 跳转信号

    # switch_window2 = QtCore.pyqtSignal()  # 跳转信号

    def __init__(self, parent=None):
        super(loginApp, self).__init__(parent)
        self.setupUi(self)
        self.enter_btn.clicked.connect(self.go_new)

    def go_new(self):
        if self.validation():
            self.switch_window1.emit()

    def get_code(self):
        return self.password_list

    def get_dic(self):
        return self.raw_data


class newpage(QtWidgets.QMainWindow, newpage_ui.Ui_show_page):
    def __init__(self, parent=None):
        super(newpage, self).__init__(parent)
        self.setupUi(self)


class Controller:
    def __init__(self):
        self.form = loginApp()
        self.form2 = newpage()


    def show_login(self):
        self.form.switch_window1.connect(self.show_new)
        self.form.show()

    def show_new(self):
        pass_parameters = self.form.get_code()
        string_code = ''.join(sorted(list(pass_parameters)))
        self.form2.set_string_code(string_code,self.form.comboBox.currentText())
        self.form2.set_raw_data(self.form.get_dic())
        self.form2.read_urls_usernames()
        self.form.close()
        self.form2.show()


def main():
    app = QApplication(sys.argv)
    controller = Controller()  # 控制器实例
    controller.show_login()  # 默认展示的是 login
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
