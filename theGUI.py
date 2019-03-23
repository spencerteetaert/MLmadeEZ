import sys
from os import path
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QFileDialog
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QIcon


class Window():

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.mainWidget = QWidget()
        
    def fetch_widget(self):
        return self.app

    def show(self):
        self.mainWidget.show()
        sys.exit(self.app.exec_())
        return True
    
    def mainWidget_title(self, title):
        if not isinstance(title, str):
            raise TypeError("title of a window should be of type: string")
        self.mainWidget.setWindowTitle(title)
        return True
    
    def mainWidget_geometry(self, *dimensions):
        for i in dimensions:
            if not isinstance(i, int):
                raise TypeError("dimensions should all be of type: int")
        self.mainWidget.setGeometry(QRect(*dimensions))
        return True

    def mainWidget_window_icon(self, icon_path):
        self.mainWidget.setWindowIcon(QIcon(icon_path))
        return True


class UserInput():

    def __init__(self, fileIn):
        self.fileIn = fileIn  # fileIn should be of type .txt
        if not self.fileIn.lower.endswith(".txt"):
            raise TypeError("fileIn should be a file of type: .txt")
    
    def fetch_file(self):
        return self.fileIn
    
class Button():

    def __init__(self):
        


    

def gui_window():
    windowObj = Window()
    windowObj.mainWidget_title("Demo")  # page_title
    windowObj.mainWidget_geometry(500, 100, 800, 800)  # openning page dimensions
    icon_path = "bin\images\python.png"
    if path.exists(icon_path):
        windowObj.mainWidget_window_icon(icon_path)
    
    
    
    return windowObj
