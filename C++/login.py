from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import user


class Login(object):

    switch_window = QtCore.pyqtSignal()

    def setupUi(self, Form):
        #Form.setObjectName("Form")
        Form.resize(570, 435)
        self.loginButton = QtWidgets.QPushButton(Form)
        self.loginButton.setGeometry(QtCore.QRect(210, 280, 151, 51))
        self.loginButton.setStyleSheet("background-color:rgb(156, 123, 183);\n"
"font: 25 9pt \"Bookman Old Style\";\n"
"color: rgb(255, 255, 255);\n"
"font-size:20px;\n"
"font-weight:bold;\n"
"border : 0;")
        #self.pushButton.setObjectName("pushButton")
        self.loginButton.clicked.connet(self.login)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(140, 160, 291, 31))
        self.textEdit.setStyleSheet("border : 5px;\n"
"\n"
"align:center;")
        #self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(140, 210, 291, 31))
        self.textEdit_2.setStyleSheet("border : 5px;")
        #self.textEdit_2.setObjectName("textEdit_2")
        self.lineEdit = QtWidgets.QPushButton(Form)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 571, 71))
        self.lineEdit.setStyleSheet("background-color:rgb(135, 39, 176);\n"
"font: 25 9pt \"Bookman Old Style\";\n"
"color: rgb(255, 255, 255);\n"
"font-size:20px;\n"
"font-weight:bold;\n"
"align:center;\n"
"text-align:center;\n"
"border : 5px;")
        #self.lineEdit.setObjectName("lineEdit")

        #self.lineEdit.clicked.connect(self.userPage)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "LOGIN PAGE"))
        self.loginButton.setText(_translate("Form", "login"))
        self.textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">student number</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">password</span></p></body></html>"))
        self.lineEdit.setText(_translate("Form", " POOC"))


    def login(self):
        self.switch_window.emit()


class Controller:
    Form = QtWidgets.QWidget()

    def __init__(self):
        pass

    def show_login(self):
        self.login = Login()
        Form = QtWidgets.QWidget()
        self.login.setupUi(Form)
        self.login.switch_window.connect(self.show_user)
        self.Form.show()

    def show_user(self,text):
        self.user = user.UserPage()
        #self.user = user.UserPage(text)
        #self.window.switch_window.connect(self.show_window_two)
        self.login.close()
        self.user.show()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())

    """
    Form = QtWidgets.QWidget()
    ui = Login_page()
    ui.setupUi(Form)
    Form.show()
    """
