import sys
from PyQt6.QtWidgets import QApplication,  QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()

        self.initUI()

    def initUI(self):

        m = PlotCanvas(self, width=5, height=3)
        
        m.setFixedSize(100, 100)
        
 

        self.setGeometry(10, 10, 1000, 1000)
        m.move(100,100)
        self.setWindowTitle('Post 6')
        self.show()
        
                 
class PlotCanvas(FigureCanvas):

    def __init__(self, parent=None, width=100, height=100, dpi=115):
        fig = Figure(figsize=(width, height), dpi=dpi)
 

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.updateGeometry(self)
        self.plot()



    def plot(self):
        x = [0, 0, 25, 22, 0, 0, 0, 50, 78, 260, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        z = [0, 0, 75, 42, 0, 0, 0, 150, 165, 400, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        a = [0, 0, 1005, 72, 0, 0, 0, 350, 350, 650, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        y = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
        
        ax = self.figure.add_subplot(111)
        ax.lineplot(x=[1], y=[1], marker='o', markersize=10, color='r')
        ax.plot(y,x)
        ax.plot(y,z)
        ax.plot(y,a)
        self.draw()
        
def main():

    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()