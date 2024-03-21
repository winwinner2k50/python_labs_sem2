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

def gen_window(size_x, size_y):
    window = QMainWindow()
    window.setFixedSize(size_x, size_y)
    return window

def gen_textbox(window, x, y, size_x, size_y, text):
    textbox = QLineEdit(window, placeholderText = text)
    textbox.move(x, y)
    textbox.resize(size_x, size_y)
    return textbox




def gen_button(window, x, y, size_x, size_y, text):
    button = QPushButton(text, window)
    button.move(x, y)
    button.setFixedSize(size_x, size_y)
    
    button.clicked.connect(button_script)
    return button

def gen_table(window, x, y, size_x, size_y):
    table = QTableWidget(window)
    table.move(x, y)
    table.setFixedSize(size_x, size_y)
    table.setColumnCount(6)  
    table.setHorizontalHeaderLabels(["N", "x1 - x2", "x", "f(x)", "Количество\nитераций", "Код ошибки"])
    return table

def button_script():
    print(type(window))
    window.table.setRowCount(window.ti+1)
    window.table.setItem(window.ti, 0, QTableWidgetItem(str(window.ti)))
    window.table.setItem(window.ti, 1, QTableWidgetItem(str(window.ti)))
    window.table.setItem(window.ti, 2, QTableWidgetItem(str(window.ti)))
    window.table.setItem(window.ti, 3, QTableWidgetItem(str(window.ti)))
    window.table.setItem(window.ti, 4, QTableWidgetItem(str(window.ti)))
    window.table.setItem(window.ti, 5, QTableWidgetItem(str(window.ti)))
    window.ti+=1
   

#создаание окна

app = QApplication(sys.argv)
window = gen_window(1500, 800)

#поля ввода
window.textbox_func = gen_textbox(window, 25, 25, 350, 50, "Введите функцию")
window.textbox_a  = gen_textbox(window, 25, 100, 100, 50, "Введите a")
window.textbox_b  = gen_textbox(window, 150, 100, 100, 50, "Введите b")
window.textbox_h = gen_textbox(window, 275, 100, 100, 50, "Введите h")
window.textbox_nmax = gen_textbox(window, 25, 175, 150, 50, "Введите h")
window.textbox_eps = gen_textbox(window, 225, 175, 150, 50, "Введите h")

#таблица
window.table = gen_table(window, 400, 25, 625, 725)
window.ti = 0
window.tj = 0
window.table.setRowCount(window.ti+1)
#кнопка
window.button = gen_button(window, 175, 250, 50 , 50, "GO")
"""
for i in range(0, 20):
    print(i)
    table.setRowCount(i+1) 
    table.setItem(i, 0, QTableWidgetItem("thfh" + str(i)))
    table.setItem(i, 1, QTableWidgetItem("Text in column 2"))
    table.setItem(i, 2, QTableWidgetItem("Text in column 3"))
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


    

window.show()  

app.exec()
