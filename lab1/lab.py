#Еремин Георгий ИУ7-24Б
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt6 import QtCore, QtGui, QtWidgets
import mymodul as my

import sys

def format_text(res):
    textbox.setText("{numder:<9.6f}".format(numder = res))

#работы кнопок
def button_script():
    button = QApplication.instance().sender()
    if button.text() != '=':
        if len(textbox.text()) <= 10:
            if button.text() != '.':
                textbox.setText(textbox.text()+button.text())
            else:
                if len(textbox.text()) != 0:
                    if textbox.text()[-1:] != '.':
                        textbox.setText(textbox.text()+button.text())
    else:
        button_script_equally()

"""
def button_script_equally():
    
    s = textbox.text()
    for x in '+-*/':
        s = s.replace(x, ' '+x+' ')
    s = s.split()
    while '*' in s or '/' in s:
        if '/' not in s:
            index_operation = s.index('*')
            s[index_operation] = int(s[index_operation-1]) * int(s[index_operation+1])
        elif '*' not in s:
            index_operation = s.index('/')
            s[index_operation] = int(s[index_operation-1]) / int(s[index_operation+1])
        elif s.index('*') < s.index('/'):
            index_operation = s.index('*')
            s[index_operation] = int(s[index_operation-1]) * int(s[index_operation+1])
        else:
            index_operation = s.index('/')
            s[index_operation] = int(s[index_operation-1]) / int(s[index_operation+1])
        
        s[index_operation]=str(int(s[index_operation]))
        s.pop(index_operation-1)
        s.pop(index_operation)


    while '-' in s or '+' in s:
        if '-' not in s:
            index_operation = s.index('+')
            s[index_operation] = int(s[index_operation-1]) + int(s[index_operation+1])
        elif '+' not in s:
            index_operation = s.index('-')
            s[index_operation] = int(s[index_operation-1]) - int(s[index_operation+1])
        elif s.index('+') < s.index('-'):
            index_operation = s.index('+')
            s[index_operation] = int(s[index_operation-1]) + int(s[index_operation+1])
        else:
            index_operation = s.index('-')
            s[index_operation] = int(s[index_operation-1]) - int(s[index_operation+1])
        
        s[index_operation]=str(int(s[index_operation]))
        s.pop(index_operation-1)
        s.pop(index_operation)
    textbox.setText(''.join(s))
"""
#перевод из 10 в 8 

def to_oct():
    
    s = textbox.text()
    if len(s) == 0 :
        error("Пустое поле")
        return 0
    res = my.my_to_oct(s)
    format_text(res)
    
#перевод из 8 в 10 
def to_des():
    s = textbox.text()
    if len(s) == 0 :
        error("Пустое поле")
        return 0
    if '8' in s or '9' in s:
        error("Символы которых нет в системе исчисления")
        return 0
    res = my.my_to_des(s)
    
    format_text(res)

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


def make_button(buttons):
    buttontext = '!!!789456123!0.'
    for i in range(4):
        buttons.append([])
        for j in range(3):
            if buttontext[i*3+j+3] != '!':
                buttons[i].append(QPushButton(buttontext[i*3+j+3], window))
                buttons[i][j].setFixedSize(50,50)
                buttons[i][j].move(25+j*75,100+i*75+75)
                buttons[i][j].clicked.connect(button_script)
            else:
                buttons[i].append('')

#создаание окна
app = QApplication(sys.argv)
window = QMainWindow()
window.setFixedSize(400,500)

#поле ввода
textbox = QLineEdit(window)
textbox.setValidator(QRegularExpressionValidator(QRegularExpression("^([1-9][0-9]*|0)(\\.)[0-9]{50}")))
textbox.move(25, 25)
textbox.resize(350,50)

#создание кнопок
buttons = []
make_button(buttons)

#создание кнопок для перевода систем исчесления
button_to_dec = QPushButton('10->8', window)
button_to_dec.setFixedSize(75,50)
button_to_dec.move(25,100)
button_to_dec.clicked.connect(to_oct)

button_to_oct = QPushButton('8->10', window)
button_to_oct.setFixedSize(75,50)
button_to_oct.move(150,100)
button_to_oct.clicked.connect(to_des)


"""
buttontext2='+-*/='
buttonfuncs = []
for i in range(2):
    buttonfuncs.append([])
    for j in range(2):
        buttonfuncs[i].append(QPushButton(buttontext2[i*2+j], window))
        buttonfuncs[i][j].setFixedSize(50,50)
        buttonfuncs[i][j].move(250+(j*75),175+i*75)
        buttonfuncs[i][j].clicked.connect(button_script)
buttonfuncs = QPushButton(buttontext2[-1], window)
buttonfuncs.setFixedSize(125,125)
buttonfuncs.move(250,175)
buttonfuncs.clicked.connect(button_script)
"""
#кнопка бекспейс
backspace = QPushButton('<--', window)
backspace.setFixedSize(125,50)
backspace.move(250,100)
backspace.clicked.connect(f_backspace)

#создание меню
menu = window.menuBar()

#создание вкладок меню
button_action_to_dec = QAction("&8  --> 10", window)
button_action_to_dec.triggered.connect(to_des)

button_action_to_oct = QAction("&10 -->  8", window)
button_action_to_oct.triggered.connect(to_oct)

button_action_myinfo = QAction("&информация об авторе", window)
button_action_myinfo.triggered.connect(my_info)

button_action_stop = QAction("&выход", window)
button_action_stop.triggered.connect(stop)

#создание нескольких меню
menu1 = menu.addMenu("помощь")
menu1.addAction(button_action_myinfo)
menu1.addAction(button_action_stop)
menu1.addSeparator()

menu2 = menu.addMenu("вычисления")
menu2.addAction(button_action_to_dec)
menu2.addAction(button_action_to_oct)
menu2.addSeparator()

window.show()  

app.exec()
