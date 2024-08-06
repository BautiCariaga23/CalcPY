from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore

from googletrans import Translator

class Home(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.settings()

    def initUI(self):
        self.output_box = QLineEdit("0")
        self.output_box.setReadOnly(True)
        self.output_box.setAlignment(QtCore.Qt.AlignRight)
        self.output_box.setStyleSheet("height:30px;")
        self.num1 = QPushButton("1")
        self.num2 = QPushButton("2")
        self.num3 = QPushButton("3")
        self.num4 = QPushButton("4")
        self.num5 = QPushButton("5")
        self.num6 = QPushButton("6")
        self.num7 = QPushButton("7")
        self.num8 = QPushButton("8")
        self.num9 = QPushButton("9")
        self.num0 = QPushButton("0")
        self.multiply = QPushButton("×")
        self.multiply.setObjectName("special")
        self.divide = QPushButton("÷")
        self.divide.setObjectName("special")
        self.sum = QPushButton("+")
        self.sum.setObjectName("special")
        self.less = QPushButton("-")
        self.less.setObjectName("special")
        self.c = QPushButton("C")
        self.c.setObjectName("special")
        self.equal = QPushButton("=")
        self.equal.setObjectName("special")

        self.num1.clicked.connect(self.button_click)
        self.num2.clicked.connect(self.button_click)
        self.num3.clicked.connect(self.button_click)
        self.num4.clicked.connect(self.button_click)
        self.num5.clicked.connect(self.button_click)
        self.num6.clicked.connect(self.button_click)
        self.num7.clicked.connect(self.button_click)
        self.num8.clicked.connect(self.button_click)
        self.num9.clicked.connect(self.button_click)
        self.num0.clicked.connect(self.button_click)
        self.c.clicked.connect(self.button_click)
        self.multiply.clicked.connect(self.button_click)
        self.divide.clicked.connect(self.button_click)
        self.sum.clicked.connect(self.button_click)
        self.less.clicked.connect(self.button_click)
        self.equal.clicked.connect(self.resolve)
        

        self.master = QVBoxLayout()

        col1 = QHBoxLayout()
        col2 = QHBoxLayout()
        col3 = QHBoxLayout()
        col4 = QHBoxLayout()
        col5 = QHBoxLayout()

        col1.addWidget(self.output_box)

        col2.addWidget(self.num7)
        col2.addWidget(self.num8)
        col2.addWidget(self.num9)
        col2.addWidget(self.multiply)

        col3.addWidget(self.num4)
        col3.addWidget(self.num5)
        col3.addWidget(self.num6)
        col3.addWidget(self.divide)

        col4.addWidget(self.num1)
        col4.addWidget(self.num2)
        col4.addWidget(self.num3)
        col4.addWidget(self.sum)

        col5.addWidget(self.c)
        col5.addWidget(self.num0)
        col5.addWidget(self.equal)
        col5.addWidget(self.less)

        self.master.addLayout(col1, 20)
        self.master.addLayout(col2, 40)
        self.master.addLayout(col3, 40)
        self.master.addLayout(col4, 40)
        self.master.addLayout(col5, 40)
        self.maxdigit = 6

        self.setLayout(self.master)
        QFontDatabase.addApplicationFont("Inter.ttf")

        self.setStyleSheet("""
            QWidget {
                background-color: #15171f;
                color: white;
                font-family: 'Inter 18pt Light';
                font-size: 14px;
            }      
            QPushButton {        
                background-color: #242836;
                color: white;
                border-radius: 5px;
                padding: 11px;
                font-size: 25px;
                font-weight: 100;
                text-align:center;
            }
            QPushButton#special {        
                background-color: #323645;
                color: white;
                border-radius: 5px;
                padding: 11px;
                font-size: 25px;
                font-weight: 100;
                text-align:center;
            }
            QPushButton:hover{
                background-color:#1a1c24;
            }
            QPushButton#special:hover{
                background-color:#4b4f5e;
            }
            QComboBox {
                border-radius:10px;
                padding: 2px;
                background-color: #1a1c24;
            }
            QComboBox::drop-down:button {
                border-radius:5px; background:rgba(0,0,0,0)
            }
            QLineEdit{
                background-color: #1a1c24;
                border:none;
                border-radius: 5px;
                text-align:right;
                width:100%;
                height:30px;
                font-size: 30px;
                padding:10px;
                padding-top: 20px;
                padding-bottom: 20px;
            }
                           
         """)

    def settings(self):
        self.setWindowTitle("Calculator")
        self.setGeometry(550,150,370,486)

    def button_click(self):
        button = self.sender()
        text = button.text()
        currtext = self.output_box.text()
        
        
        if text == "C":
            self.output_box.clear()
            self.output_box.setText("0")
            self.maxdigit = 6
        else:
            if currtext == "0":
                self.output_box.setText(str(text))
            elif self.maxdigit > 0 and text not in ["×","÷","+","-"]:
                self.output_box.setText(currtext + str(text))
                self.maxdigit-=1
            elif text in ["×","÷","+","-"] and currtext[len(currtext)-1] not in ["×","÷","+","-"]:
                self.output_box.setText(currtext + str(text))
                self.maxdigit = 6

    def resolve(self):
        text = self.output_box.text()
        symb = ["×","÷","+","-"]
        currsymb = ""
        for b in text:
            for a in symb:
                if b == a:
                    currsymb = b
                    break
        first = ""
        second = ""
        for a in text:
            if a.isnumeric():
                first+= a
            else:
                break
        for a in reversed(text):
                if a.isnumeric():
                    second+= a
                else:
                    break
        match currsymb:
                    case "×":
                        self.output_box.setText(str(int(first) * int(second)))
                    case "+":
                        self.output_box.setText(str(int(first) + int(second)))
                    case "-":
                        self.output_box.setText(str(int(first) - int(second)))
                    case "÷":
                        self.output_box.setText(str(int((int(first) / int(second)))))
                

if __name__ in "__main__":
    app = QApplication([])
    main = Home()
    main.show()
    app.exec()