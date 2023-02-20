from PyQt6.QtWidgets import *

class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("About")
        self.setFixedSize(300,150)
        
        self.layout = QVBoxLayout()
        info = QLabel('''
        PyQtTextEdit
        Written by ChasCharlie
        ''')

        self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        self.layout.addWidget(info)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

        self.buttonBox.accepted.connect(lambda: self.close())
