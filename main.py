from PyQt6.QtWidgets import QApplication, QWidget, QFileDialog

from ui_output import Ui_Form
import sys

class MainWindow(QWidget,Ui_Form):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)

        self.newButton.clicked.connect(self.newFile)
        self.openButton.clicked.connect(self.openFile)
        self.saveButton.clicked.connect(self.saveFile)
        self.saveAsButton.clicked.connect(self.saveAsFile)

        self.fileName = None

    def newFile(self):
        self.fileName = None
        self.plainTextEdit.clear()

    def openFile(self):
        self.fileName = QFileDialog.getOpenFileName(self,"Open")[0] or None
        if self.fileName:
            with open(self.fileName,"r") as read:
                contents = read.read()
                self.plainTextEdit.clear()
                self.plainTextEdit.insertPlainText(contents)
    
    def saveFile(self):
        if self.fileName == None:
            self.saveAsFile()

        else:
            with open(self.fileName,"w+") as write:
                contents = self.plainTextEdit.toPlainText()
                write.write(contents)

    def saveAsFile(self):
        self.fileName = QFileDialog.getSaveFileName(self,"Save As")[0] or None
        if self.fileName:
            self.saveFile()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = MainWindow()
    view.show()
    app.exec()