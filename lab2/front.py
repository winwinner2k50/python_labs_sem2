#Еремин Георгий ИУ7-24Б
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt6 import QtCore, QtGui, QtWidgets
import mymodul as my

import sys

#бекспейс
def f_backspace():
    textbox.setText(textbox.text()[:-1])
#окно обо мне
def my_info():
    massage_box = QMessageBox(window)
    massage_box.setWindowTitle("Its me")
    massage_box.setText("Еремин Георгий ИУ7-24Б")
    button = massage_box.exec()

#завершение программы
def stop():
    sys.exit()

#окно ошибки
def error(s):
    massage_box = QMessageBox(window)
    massage_box.setWindowTitle("ERROR")
    massage_box.setText(s)
    button = massage_box.exec()


#создаание окна
app = QApplication(sys.argv)
window = QMainWindow()
window.setFixedSize(400,500)

#поле ввода
textbox = QLineEdit(window)

textbox.move(25, 25)
textbox.resize(350,50)


"""
#кнопка бекспейс
backspace = QPushButton('<--', window)
backspace.setFixedSize(125,50)
backspace.move(250,100)
backspace.clicked.connect(f_backspace)
"""
#создание меню
menu = window.menuBar()

#создание вкладок меню

button_action_myinfo = QAction("&информация об авторе", window)
button_action_myinfo.triggered.connect(my_info)

button_action_stop = QAction("&выход", window)
button_action_stop.triggered.connect(stop)

#создание нескольких меню
menu1 = menu.addMenu("помощь")
menu1.addAction(button_action_myinfo)
menu1.addAction(button_action_stop)
menu1.addSeparator()

table = QTableWidget(window)  # Create a table
table.setFixedSize(350, 350)
table.move(25, 100)
table.setColumnCount(3)     #Set three columns      # and one row
table.setHorizontalHeaderLabels(["Header 1", "Header 2", "Header 3"])
for i in range(0, 20):
    print(i)
    table.setRowCount(i+1) 
    table.setItem(i, 0, QTableWidgetItem("thfh" + str(i)))
    table.setItem(i, 1, QTableWidgetItem("Text in column 2"))
    table.setItem(i, 2, QTableWidgetItem("Text in column 3"))
    

window.show()  

app.exec()
