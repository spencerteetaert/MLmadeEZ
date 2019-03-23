import sys
from os import path
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QFileDialog, QPushButton
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QIcon




class Window():

    def __init__(self, dataStore):
        self.app = QApplication(sys.argv)
        self.mainWidget = QWidget()
        self.init_ui()
        self.dataStore = dataStore
    
    def init_ui(self):
        # Import .txt data Button
        data_in_button = Button("Import Data", self.mainWidget)
        data_in_button.move(20, 20)
        data_in_button.clicked.connect(self.upload_file)
        go = Button("GO", self.mainWidget)
        go.resize(100,100)
        go.move(500, 500)
        go.clicked.connect(self.pr)
        return True

    def pr(self):
        print(self.dataStore.importedFilePath)

    def fetch_widget(self):
        return self.app

    def run(self):
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

    def upload_file(self):  
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            UserFileInput(fileName, self.dataStore)
        return True
    

class UserFileInput():

    def __init__(self, ImportedFile, dataStore):
        self.importedFile = ImportedFile  # fileIn should be of type .txt
        if not self.importedFile.lower().endswith(".txt"):
            raise TypeError("Imported file should be a file of type: .txt")
        else:
            dataStore.update_imported_file_path(self.importedFile)

class Button(QPushButton):

    def __init__(self, title, parentWidget):
        super().__init__(title, parentWidget)

class DataStorage:

    def __init__(self):
        self.importedFilePath = None  # path to .txt file
        self.layers = None
        self.nodes = None
        self.learningRate = None

    def update_imported_file_path(self, filePath):
        self.importedFilePath = filePath
        return True
    
    def update_layers(self, numberOfLayer):
        self.layers = numberOfLayer
        return True
    
    def update_nodes(self, numberOfNodes):
        self.nodes = numberOfNodes
        return True
    
    def update_learning_rate(self, learningRateValue):
        self.learningRate = learningRateValue
        return True


def gui_setup():
    dataStore = DataStorage()
    windowObj = Window(dataStore)
    windowObj.mainWidget_title("Demo")  # page_title
    windowObj.mainWidget_geometry(500, 100, 800, 800)  # openning page dimensions
    icon_path = "bin\images\python.png"
    if path.exists(icon_path):
        windowObj.mainWidget_window_icon(icon_path)
    
    return windowObj
