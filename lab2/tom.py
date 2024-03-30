#Метод секущих
#Экстремумы

#Еремин Георгий ИУ7-24Б
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt6 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


import numpy as np
import sys
import ben

#окно обо мне

def my_info():
    massage_box = QMessageBox(window)
    massage_box.setWindowTitle("Its me")
    massage_box.setText("Еремин Георгий ИУ7-24Б")
    button = massage_box.exec()


#информация об ошибках

def info():

    massage_box = QMessageBox(window)
    massage_box.setWindowTitle("ERROR INFO")
    massage_box.setText("Коды Ошибок\n"
        "0 -всё верно\n"
        "1 - превышенно максимальное число итераций\n"
        "2 - деление на 0\n"
        "3 - корень вышел за границы отрезка")
    
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


#сощдание окна

def gen_window(size_x, size_y):
    window = QMainWindow()
    window.setFixedSize(size_x, size_y)
    return window


#создание поля ввода

def gen_textbox(window, x, y, size_x, size_y, text):

    textbox = QLineEdit(window, placeholderText = text)

    textbox.move(x, y)

    textbox.resize(size_x, size_y)
    return textbox


#создание кнопок

def gen_button(window, x, y, size_x, size_y, text, scrips):
    button = QPushButton(text, window)
    button.move(x, y)
    button.setFixedSize(size_x, size_y)
    button.clicked.connect(scrips)
    return button


#проверка

def check(a, f):

    try:
        f(a)

        return 0

    except ValueError:

        return 1


#ввод элемента

def input_el(text, f, text_error):

    if len(text) == 0 or check(text, f):
        error(text_error)

        return None
    return f(text)


#функция основной кнопки

def button_script():

    func = window.textbox_func.text()

    if len(func) == 0 or ben.func(func, 1) == "error":
        error("Поле функции заданно не верно")
        return 0


    a = input_el(window.textbox_a.text(), float, "Поле а заданно не верно")
    if a == None:
        return 0
    b = input_el(window.textbox_b.text(), float, "Поле b заданно не верно")
    if b == None:
        return 0
    h = input_el(window.textbox_h.text(), float, "Поле h заданно не верно")
    if h == None:
        return 0
    eps = input_el(window.textbox_eps.text(), float, "Поле eps заданно не верно")
    if eps == None:
        return 0
    nmax = input_el(window.textbox_nmax.text(), int, "Поле Nmax заданно не верно")
    if nmax == None:
        return 0
    
    if (a > b):
        error("А больше Б")
        return 0

    if (h <= 0):
        error("Не верный шаг")
        return 0

    if (nmax <= 0):
        error("Не верное число итераций")
        return 0

    if (eps < 0):
        error("Отрицательная погрешность")
        return 0

    root = ben.gen_roots(func, a, b, h, eps, nmax)

    root_for_graph = []

    for x in root:
        if x[4] == 0:
            root_for_graph.append(x)
        
    gen_table(root)
    gen_graph(label, root_for_graph)


#кнопка генирации таблицы

def button_gen_table():

    if len(window.textbox_a.text()) == 0 or check(window.textbox_a.text(), float):

        error("Поле а заданно не верно")

        return 0

    if len(window.textbox_b.text()) == 0 or check(window.textbox_b.text(), float):

        error("Поле b заданно не верно")

        return 0

    if len(window.textbox_h.text()) == 0 or check(window.textbox_h.text(), float):

        error("Поле h заданно не верно")

        return 0

    if len(window.textbox_eps.text()) == 0 or check(window.textbox_eps.text(), float):

        error("Поле погрешности заданно не верно")

        return 0

    if len(window.textbox_nmax.text()) == 0 or check(window.textbox_nmax.text(), int):

        error("Поле Nmax заданно не верно")

        return 0

    if len(window.textbox_func.text()) == 0 or ben.func(window.textbox_func.text(), 1) == "error":

        error("Поле функции заданно не верно")

        return 0
    
    func = window.textbox_func.text()
    a = float(window.textbox_a.text())
    b = float(window.textbox_b.text())

    if (a > b):

        error("А больше Б")

        return 0

    h = float(window.textbox_h.text())

    nmax = int(window.textbox_nmax.text())

    if (nmax < 0):

        error("Отрицательное число итераций")

        return 0

    eps = float( window.textbox_eps.text())

    if (eps < 0):

        error("Отрицательная погрешность")

        return 0

    root = ben.gen_roots(func, a, b, h, eps, nmax)
    gen_table(root)


#cоздание таблицы

def gen_table(root):

    window.table.setRowCount(0)

    for i in range(len(root)):

        window.table.setRowCount(i + 1)

        window.table.setItem(i, 0, QTableWidgetItem(str(i+1)))

        window.table.setItem(i, 1, QTableWidgetItem(f"{root[i][0][0]:.3g} - {root[i][0][1]:.3g}"))

        window.table.setItem(i, 2, QTableWidgetItem(f"{root[i][1]:.3g}"))

        window.table.setItem(i, 3, QTableWidgetItem(f"{root[i][2]:.3g}"))

        window.table.setItem(i, 4, QTableWidgetItem(f"{root[i][3]:.3g}"))

        window.table.setItem(i, 5, QTableWidgetItem(f"{root[i][4]:.3g}"))
"""

def button_graph():

    if len(window.textbox_a.text()) == 0 or check(window.textbox_a.text(), float):

        error("Поле а заданно не верно")

        return 0

    if len(window.textbox_b.text()) == 0 or check(window.textbox_b.text(), float):

        error("Поле b заданно не верно")

        return 0

    if len(window.textbox_h.text()) == 0 or check(window.textbox_h.text(), float):

        error("Поле h заданно не верно")

        return 0

    if len(window.textbox_eps.text()) == 0 or check(window.textbox_eps.text(), float):

        error("Поле погрешности заданно не верно")

        return 0

    if len(window.textbox_nmax.text()) == 0 or check(window.textbox_nmax.text(), int):

        error("Поле Nmax заданно не верно")

        return 0

    if len(window.textbox_func.text()) == 0 or ben.func(window.textbox_func.text(), 1) == "error":

        error("Поле функции заданно не верно")

        return 0
    
    func = window.textbox_func.text()
    a = float(window.textbox_a.text())
    b = float(window.textbox_b.text())

    if (a > b):

        error("А больше Б")

        return 0

    h = float(window.textbox_h.text())

    nmax = int(window.textbox_nmax.text())

    if (nmax < 0):

        error("Отрицательное число итераций")

        return 0

    eps = float( window.textbox_eps.text())

    if (eps < 0):

        error("Отрицательная погрешность")

        return 0

    root = ben.gen_roots(func, a, b, h, eps, nmax)

    graph(label, root)
"""
#создание графа 
def gen_graph(label, root):
    a = float(window.textbox_a.text())
    b =  float(window.textbox_b.text())

    x = list(np.arange(a, b, (b-a)/100))

    x1 = [root[i][1] for i in range(len(root))]

    y1 = [root[i][2] for i in range(len(root))]

    y = [ben.func(window.textbox_func.text(), i) for i in x]

    fig = Figure(figsize=(5, 5))

    ax = fig.add_subplot()

    point_x, point_y = ben.gen_point(x, y)

    ax.plot(x, y, label="f")

    ax.scatter(point_x, point_y, color = "red", s = 30, label = "экстемумы")

    ax.scatter(x1, y1, color = "blue", s = 30, label = "корни")
    
    ax.grid()

    ax.legend(prop={'size': 8})

    canvas = FigureCanvasQTAgg(fig)

    layout = QVBoxLayout()

    layout.deleteLater()

    layout.addWidget(canvas)

    layout.addStretch(1)

    label.setLayout(layout)

#очистка графа 
def clear_graph():

    fig = Figure(figsize=(5, 5))

    ax = fig.add_subplot()
    ax.plot(0, 0)
    ax.grid()

    canvas = FigureCanvasQTAgg(fig)


    layout = QVBoxLayout()
    layout.deleteLater()
    layout.addWidget(canvas)
    layout.addStretch(1)
    label.setLayout(layout)

#очистка графа 
def clear_table():

    window.table.setRowCount(0)

#очистка ввода
def clear_input():

    window.textbox_a.setText("")

    window.textbox_b.setText("")

    window.textbox_eps.setText("")

    window.textbox_h.setText("")

    window.textbox_func.setText("")

    window.textbox_nmax.setText("")

#очистка всего
def clear_all():
    clear_graph()
    clear_input()
    clear_table()

#создаание окна
app = QApplication(sys.argv)

window = gen_window(1700, 800)

label = QLabel(window)
label.resize(500, 800)
label.move(1050, 25)


#поля ввода
window.textbox_func = gen_textbox(window, 25, 25, 350, 50, "Введите функцию")
window.textbox_a  = gen_textbox(window, 25, 100, 100, 50, "Введите a")
window.textbox_b  = gen_textbox(window, 150, 100, 100, 50, "Введите b")
window.textbox_h = gen_textbox(window, 275, 100, 100, 50, "Введите h")
window.textbox_nmax = gen_textbox(window, 25, 175, 150, 50, "Введите nmax")
window.textbox_eps = gen_textbox(window, 225, 175, 150, 50, "Введите eps")

#

#таблица
window.table = QTableWidget(window)
window.table.move(400, 25)
window.table.setFixedSize(625, 725)
window.table.setColumnCount(6)  
window.table.setHorizontalHeaderLabels(["N", "x1 - x2", "x", "f(x)", "Количество\nитераций", "Код ошибки"])

#кнопки
window.button = gen_button(window, 175, 250, 50 , 50, "GO", button_script)

#создание графа
clear_graph()

#создание меню
menu = window.menuBar()

#создание вкладок меню

button_action_myinfo = QAction("&информация об авторе", window)
button_action_myinfo.triggered.connect(my_info)

button_action_stop = QAction("&выход", window)
button_action_stop.triggered.connect(stop)

button_action_go = QAction("Запустить всё", window)
button_action_go.triggered.connect(button_script)

button_action_clearall = QAction("Очистить всё", window)
button_action_clearall.triggered.connect(clear_all)

button_action_info_error = QAction("Справка об ошибках", window)
button_action_info_error.triggered.connect(info)


#создание нескольких меню
menu1 = menu.addMenu("помощь")

menu1.addAction(button_action_myinfo)

menu1.addAction(button_action_stop)

menu1.addSeparator()


menu2 = menu.addMenu("Функции")

menu2.addAction(button_action_go)


menu2.addAction(button_action_clearall)

menu2.addSeparator()

menu3 = menu.addMenu("справка")

menu3.addAction(button_action_info_error)

menu3.addSeparator()


window.show()


app.exec()
