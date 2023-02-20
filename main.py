from PyQt6.QtWidgets import *

from dialog import *
from ui_output import Ui_Form
import sys

class MainWindow(QWidget,Ui_Form):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)

        self.filemenu.addAction("New",self.newFile).setShortcut("Ctrl+N")
        self.filemenu.addAction("Open",self.openFile).setShortcut("Ctrl+O")
        self.filemenu.addAction("Save",self.saveFile).setShortcut("Ctrl+S")
        self.filemenu.addAction("Save As",self.saveAsFile)
        self.filemenu.addSeparator()
        self.filemenu.addAction("Exit",lambda: self.close())
        self.helpmenu.addAction("About",self.about)

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

    def about(self):
        AboutDialog().exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = MainWindow()
    view.show()
    app.exec()