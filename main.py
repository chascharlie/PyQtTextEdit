from PyQt6.QtWidgets import *

from dialog import *
from ui_output import Ui_Form
import sys, os

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

        self.addTabButton.clicked.connect(self.newTab)
        self.closeTabButton.clicked.connect(self.closeTab)

        self.newTab()

        self.fileName = None

    def newTab(self):
        self.tabWidget.addTab(QPlainTextEdit(),"New File")
        index = self.tabWidget.currentIndex()+1
        self.tabWidget.setCurrentIndex(index)

    def closeTab(self):
        index = self.tabWidget.currentIndex()
        self.tabWidget.removeTab(index)
        self.tabWidget.setCurrentIndex(index-1)

        if self.tabWidget.count() == 0:
            self.newTab()

    def newFile(self):
        self.fileName = None
        self.tabWidget.currentWidget().clear()
        self.updateTitle()

    def openFile(self):
        self.fileName = QFileDialog.getOpenFileName(self,"Open")[0] or None
        if self.fileName:
            with open(self.fileName,"r") as read:
                contents = read.read()
                self.tabWidget.currentWidget().clear()
                self.tabWidget.currentWidget().insertPlainText(contents)
        
        self.updateTitle()

    def saveFile(self):
        if self.fileName == None:
            self.saveAsFile()

        else:
            with open(self.fileName,"w+") as write:
                contents = self.tabWidget.currentWidget().toPlainText()
                write.write(contents)

    def saveAsFile(self):
        self.fileName = QFileDialog.getSaveFileName(self,"Save As")[0] or None
        if self.fileName:
            self.saveFile()

        self.updateTitle()

    def about(self):
        AboutDialog().exec()

    def updateTitle(self):
        if self.fileName:
            name = os.path.basename(self.fileName)
        else:
            name = "New File"

        index = self.tabWidget.currentIndex()
        self.tabWidget.setTabText(index,name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = MainWindow()
    view.show()
    app.exec()