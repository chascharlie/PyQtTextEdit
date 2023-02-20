from PyQt6.QtWidgets import * # Import all functionality of QtWidgets module of PyQt6 library

from dialog import * # Import all functionality from dialog
from ui_output import Ui_Form # Import Ui_Form class from ui_output; this is the GUI designed in Qt Designer
import sys, os # Import sys and os modules

class MainWindow(QWidget,Ui_Form): # Class MainWindow
    def __init__(self,parent=None): # Initialising function
        super(MainWindow,self).__init__(parent)
        self.setupUi(self) # Setup UI

        self.filemenu.addAction("New",self.newFile).setShortcut("Ctrl+N") # Add New action to filemenu and give it the shortcut CTRL+N
        self.filemenu.addAction("Open",self.openFile).setShortcut("Ctrl+O")
        self.filemenu.addAction("Save",self.saveFile).setShortcut("Ctrl+S")
        self.filemenu.addAction("Save As",self.saveAsFile)
        self.filemenu.addSeparator() # Add separator to file menu
        self.filemenu.addAction("Exit",lambda: self.close()) # Add Exit action to filemenu that closes window when clicked
        self.helpmenu.addAction("About",self.about) # Add About action to helpmenu

        self.addTabButton.clicked.connect(self.newTab) # When addtabButton is clicked, self.newTab function executed
        self.closeTabButton.clicked.connect(self.closeTab) # When closeTabButton is clicked, self.closeTab function executed

        self.newTab() # Open new tab

        self.fileName = None # self.fileName will be used for determing if an existing file is open or not

    def newTab(self): # self.newTab function
        self.tabWidget.addTab(QPlainTextEdit(),"New File") # Add tab to tabWidget containing a QPlainTextEdit widget and titled "New file"
        index = self.tabWidget.currentIndex()+1 # Determine index of new tab
        self.tabWidget.setCurrentIndex(index) # Change tab based on index

    def closeTab(self): # self.closeTab function
        index = self.tabWidget.currentIndex() # Determine index of current tab
        self.tabWidget.removeTab(index) # Remove tab based on index
        self.tabWidget.setCurrentIndex(index-1) # Set current tab one to the left

        if self.tabWidget.count() == 0: # If there are no tabs left
            self.newTab() # Open a new one

    def newFile(self): # self.newFile function
        self.fileName = None # self.fileName is None; this indicates no existing file is open
        self.tabWidget.currentWidget().clear() # Clear contents of QPlainTextEdit in tab
        self.updateTitle() # Update title; because this is a new file, title will be "New File"

    def openFile(self): # self.openFile function
        self.fileName = QFileDialog.getOpenFileName(self,"Open")[0] or None # Prompt user to select a file; if they don't, self.fileName is None
        if self.fileName: # If self.fileName has a value
            with open(self.fileName,"r") as read: # Open in read-only mode
                contents = read.read() # Read contents
                self.tabWidget.currentWidget().clear() # Clear contents of QPlainTextEdit in tab
                self.tabWidget.currentWidget().insertPlainText(contents) # Insert contents of chosen file
        
        self.updateTitle() # Update title; because this is an existing file, it will be the name of the file

    def saveFile(self): # self.saveFile function
        if self.fileName: # If self.fileName has a value
            with open(self.fileName,"w+") as write: # Open in write mode, creating file if it doesn't exist
                contents = self.tabWidget.currentWidget().toPlainText() # Get plain text from QPlainTextEdit in tab
                write.write(contents) # Write to file, because we're in write mode existing contents will be overriden
            
        else: # Otherwise, so self.fileName is None
            self.saveAsFile() # Run self.saveAsFile

    def saveAsFile(self): # self.saveAsFile function
        self.fileName = QFileDialog.getSaveFileName(self,"Save As")[0] or None # Prompt user to select a file; if they don't, self.fileName is None
        if self.fileName: # If self.fileName has a value
            self.saveFile() # Run self.saveFile

        self.updateTitle() # Update title

    def about(self): # self.about function
        AboutDialog().exec() # Execute AboutDialog

    def updateTitle(self): # self.updateTitle function
        if self.fileName:
            name = os.path.basename(self.fileName) # Name of file stored at path self.fileName
        else:
            name = "New File" # File has no name so does not exist, so we'll call it "New File"

        index = self.tabWidget.currentIndex() # Get index of current tab
        self.tabWidget.setTabText(index,name) # Set label of tab to decided name

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = MainWindow()
    view.show()
    app.exec()