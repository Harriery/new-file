# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(600, 700)
        LoginWindow.setMinimumSize(QtCore.QSize(600, 700))
        LoginWindow.setMaximumSize(QtCore.QSize(600, 700))
        LoginWindow.setStyleSheet("QWidget {\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"stop:0 #7CCBA2, stop:1 #5FAFD3);\n"
"\n"
"}\n"
"QPushButton {\n"
"    background-color: #2196F3;\n"
"    border-radius: 8px;\n"
"    border: 2px solid #1976D2;\n"
"    padding: 10px 20px;\n"
"    font-size: 22px;\n"
"    color: white;\n"
"    box-shadow: 0 4px #1976D2;\n"
"    transition: all 0.3s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #42A5F5;\n"
"    box-shadow: 0 6px #1976D2;\n"
"    transform: translateY(-4px);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E88E5;\n"
"    box-shadow: 0 2px #1976D2;\n"
"    transform: translateY(2px);\n"
"}\n"
"")
        self.pushButton_login = QtWidgets.QPushButton(parent=LoginWindow)
        self.pushButton_login.setGeometry(QtCore.QRect(130, 400, 345, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_login.sizePolicy().hasHeightForWidth())
        self.pushButton_login.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_login.setFont(font)
        self.pushButton_login.setObjectName("pushButton_login")
        self.pushButton_cikis = QtWidgets.QPushButton(parent=LoginWindow)
        self.pushButton_cikis.setGeometry(QtCore.QRect(220, 590, 169, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_cikis.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/exit.png.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_cikis.setIcon(icon)
        self.pushButton_cikis.setObjectName("pushButton_cikis")
        self.label_2 = QtWidgets.QLabel(parent=LoginWindow)
        self.label_2.setGeometry(QtCore.QRect(120, 240, 345, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QWidget {\n"
"    font: bold 25px \"Verdana\";\n"
"    color: #004080;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"stop:0 #C2D9F0, stop:1 #85B1CF);\n"
"    text-shadow: 2px 2px 3px #996600;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=LoginWindow)
        self.label.setGeometry(QtCore.QRect(120, 130, 345, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QWidget {\n"
"    font: bold 25px \"Verdana\";\n"
"    color: #004080;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, \n"
"stop:0 #C2D9F0, stop:1 #85B1CF);\n"
"    text-shadow: 2px 2px 3px #996600;\n"
"    border-radius: 10px;\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.lineEdit_userName = QtWidgets.QLineEdit(parent=LoginWindow)
        self.lineEdit_userName.setGeometry(QtCore.QRect(120, 160, 345, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_userName.sizePolicy().hasHeightForWidth())
        self.lineEdit_userName.setSizePolicy(sizePolicy)
        self.lineEdit_userName.setStyleSheet("border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.lineEdit_userName.setObjectName("lineEdit_userName")
        self.lineEdit_password = QtWidgets.QLineEdit(parent=LoginWindow)
        self.lineEdit_password.setGeometry(QtCore.QRect(120, 270, 345, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_password.sizePolicy().hasHeightForWidth())
        self.lineEdit_password.setSizePolicy(sizePolicy)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.login_error_label = QtWidgets.QLabel(parent=LoginWindow)
        self.login_error_label.setEnabled(False)
        self.login_error_label.setGeometry(QtCore.QRect(180, 480, 231, 51))
        self.login_error_label.setStyleSheet("QLabel {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: transparent;\n"
"}\n"
"")
        self.login_error_label.setObjectName("login_error_label")

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.pushButton_login.setText(_translate("LoginWindow", "Login"))
        self.pushButton_cikis.setText(_translate("LoginWindow", "Exit"))
        self.label_2.setText(_translate("LoginWindow", "Password"))
        self.label.setText(_translate("LoginWindow", "User Name"))
        self.login_error_label.setText(_translate("LoginWindow", "Invalid entry, please try again."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QWidget()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec())
