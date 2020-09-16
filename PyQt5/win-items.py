import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__():

        self.setWindowTitle("First Application")
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon("rocket.png"))
        self.setToolTip("My Tooltip")

window=MyWindow()

def window():
    app=QApplication(sys.argv)
    win=QMainWindow()

    lbl_name=QtWidgets.QLabel(win)
    lbl_name.setText("Adınız: ")
    lbl_name.move(50,30)

    lbl_surname=QtWidgets.QLabel(win)
    lbl_surname.setText("Soyadınız: ")
    lbl_surname.move(50,70)

    txt_name=QtWidgets.QLineEdit(win) #TextBox
    txt_name.move(150,30)

    txt_surname=QtWidgets.QLineEdit(win)
    txt_surname.move(150,70)

    def clicked(self):
        print(f"Butona tıklandı name: {txt_name.text()} surname: {txt_surname.text()}")

    btn_save=QtWidgets.QPushButton(win)
    btn_save.setText("Kaydet")
    btn_save.move(150,110)
    btn_save.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())

window()
