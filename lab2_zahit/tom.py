from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt6 import QtCore, QtGui, QtWidgets
import sys

import ben

def sum():
    textbox3.setText(ben.sum_9(textbox1.text(), textbox2.text()))

def gen_window():
    window = QMainWindow()
    window.setFixedSize(400,500)
    return window

app = QApplication(sys.argv)
wwindow = gen_window()

textbox1 = QLineEdit(window)
textbox1.move(25, 25)
textbox1.resize(350,50)

textbox2 = QLineEdit(window)
textbox2.move(25, 100)
textbox2.resize(350,50)

textbox3 = QLineEdit(window)
textbox3.move(25, 250)
textbox3.resize(350,50)

button1 = QPushButton('+', window)
button1.setFixedSize(350,50)
button1.move(25,175)

button1.clicked.connect(sum)




window.show()  

app.exec()

