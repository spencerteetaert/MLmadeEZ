import sys
from PyQt5.QtWidgets import QApplication, QWidget

def input_type_check(instances):
    pass

class Window():

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.screen = QWidget()
        

    def show(self):
        self.screen.show()
        sys.exit(self.app.exec_())
        return True
    
    def screen_title(self, title):
        if not isinstance(title, str):
            raise TypeError("title of a window should be of type string")
        self.screen.setWindowTitle(title)
        return True
    
    def screen_geometry(self, x, y, width, height):
    
        self.screen.setGeometry()

def main():
    windowObj = Window()
    windowObj.screen_title("Learning NN - Demo")
    windowObj.show()
    return True

main()

