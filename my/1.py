class Graph:
    def __init__(self):
        self.LIMIT_Y = range(0, 11)

    def set_data(self, data):
        self.data = data

    def draw(self):
        for x in self.data:
            if x in self.LIMIT_Y:
                print(x, end=" ")

graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()



    
