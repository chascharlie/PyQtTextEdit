from PyQt6.QtWidgets import * # Import all functionality of QtWidgets module of PyQt6 library

class AboutDialog(QDialog): # Class AboutDialog
    def __init__(self): # Initialising function
        super().__init__()

        self.setWindowTitle("About") # Set title to "About"
        self.setFixedSize(300,150) # Set size to 300x150, cannot be changed
        
        self.layout = QVBoxLayout() # Vertical layout
        info = QLabel('''
        PyQtTextEdit
        Written by ChasCharlie
        ''') # Label declaring name of program and developer

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok) # Button box with an OK button
        self.layout.addWidget(info) # Add info label to layout
        self.layout.addWidget(self.buttonBox) # Add button box to layout
        self.setLayout(self.layout) # Set layout of dialog to self.layout

        self.buttonBox.accepted.connect(lambda: self.close()) # If OK button is clicked, dialog closes
