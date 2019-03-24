import sys
from os import path
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QFileDialog, QPushButton, QInputDialog
from PyQt5.QtCore import QRect, pyqtSignal
from PyQt5.QtGui import QIcon, QIntValidator, QFont
import PyQt5
sys.path.insert(0, "neural_network")
import neural_network as nn

class Window():

    def __init__(self, dataStore):
        self.app = QApplication(sys.argv)
        self.mainWidget = QWidget()
        self.init_ui()
        self.dataStore = dataStore
    
    def init_ui(self):
        # Import .txt data Button
        self.DataInButton = Button("Import Data", self.mainWidget)
        self.DataInButton.move(100, 50)
        self.DataInButton.clicked.connect(self.upload_file)
        
        #Layers Input
        self.epochs = QLineEdit(self.mainWidget)
        self.epochs.setValidator(QIntValidator())
        self.epochs.move(75, 100)
        self.epochs.setPlaceholderText("# of epochs")
        self.epochs.textChanged.connect(self.number_of_epoch)
        #Nodes Per Lay
        self.numNodes = QLineEdit(self.mainWidget)
        self.numNodes.move(75, 125)
        self.numNodes.setPlaceholderText("# of nodes (csv)")
        self.numNodes.textChanged.connect(self.number_of_nodes)
        #Learning Rate
        self.numLR = QLineEdit(self.mainWidget)
        self.numLR.move(75, 150)
        self.numLR.setPlaceholderText("learning rate (#)")
        #self.numLR.textChanged.connect(self.number_of_nodes)
        
        # Final Submit Button before NN
        go = Button("GO", self.mainWidget)
        go.setFont(QFont("Helvetica", 25))
        go.resize(100,100)
        go.move(190, 190)
        go.clicked.connect(self.go_time)
        
        self.test_data = Button("Test", self.mainWidget)
        self.test_data.move(10, 260)
        self.test_data.clicked.connect(self.test_inputs)

        

        return True

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
    
    def number_of_epoch(self):
        self.update_epoch()
        return True
    
    def update_epoch(self):
        self.dataStore.epochs = int(self.epochs.text())
    
    def number_of_nodes(self):
        self.update_nodes()
        return True
    
    def update_nodes(self):
        try:
            self.dataStore.nodes = int(self.numNodes.text())
        except:
            return False
        return True
        #nodesByLayer = []
        #for i in range(0, len(nodesByLayerStr), 1):
        #    if not nodesByLayerStr[i].isnumeric():
        #        continue
        #    nodesByLayer += int(nodesByLayerStr[i])
        #self.dataStore.nodes = nodesByLayer
        #return True

    def update_learning_rate(self):
        try:
            float_value = float(self.numLR.text())
            self.dataStore.learningRate = float_value
        except:
            return False
        return True

    def go_time(self):
        self.update_learning_rate()
        if self.dataStore.importedFilePath == None: #or self.dataStore.epochs == None or self.dataStore.nodes == None or self.dataStore.learningRate == None:
            return False
        nn.bridge(self.dataStore)
        return True

    def test_inputs(self):
        textLayer, results = QInputDialog.getText(self.mainWidget, "Test Inputs", "Input Layers")
        if results:
            print(textLayer)



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
        self.epochs = None
        self.nodes = None
        self.learningRate = None

    def update_imported_file_path(self, filePath):
        self.importedFilePath = filePath
        return True
    
    def update_epoch(self, numberOfLayer):
        self.epochs = numberOfLayer
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
    windowObj.mainWidget_geometry(300, 300, 300, 300)  # openning page dimensions
    icon_path = "bin\images\python.png"
    if path.exists(icon_path):
        windowObj.mainWidget_window_icon(icon_path)
    
    return windowObj
