import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QCursor


class Main():
    def __init__(self):
        self.widget = QWidget()        
        self.widget.setWindowTitle('BaseUI')        
        self.widget.resize(1000,694)
        self.widget.move(480,173)
        self.widget.setWindowFlag(Qt.FramelessWindowHint)
        
        self.line_edit = QLineEdit(self.widget)
        self.line_edit.setClearButtonEnabled(True)
        self.line_edit.setPlaceholderText('Type something here')
        self.line_edit.setFont(QFont('Courier', 10))
        self.line_edit.resize(300,40)
        self.line_edit.move(350,327)

        self.esc_button = QPushButton('x', self.widget)
        self.esc_button.clicked.connect(self.close)
        self.esc_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.esc_button.resize(20,20)
        self.esc_button.move(960,20)        

        self.min_button = QPushButton('-',self.widget)
        self.min_button.resize(20,20)
        self.min_button.move(920,20)
        
        self.widget.setStyleSheet('''QWidget {background-color: #423c6d; border: 2px solid #f4b777}
                                     QLineEdit {border: none; border-bottom: 2px solid #9ec8cf; color: #b098b4;}
                                     QPushButton {border: 1px solid #b098b4; border-radius: 10px; color: #b098b4; font-weight: bold}                                     
                                    ''')
        self.widget.show()

    def close(self):
        self.widget.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)    
    m = Main()
    sys.exit(app.exec())
