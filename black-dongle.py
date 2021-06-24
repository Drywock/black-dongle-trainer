import sys
from random import randrange

from PySide6.QtCore import Qt, QTimer, Slot
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
                               QVBoxLayout, QWidget)


def generate_number():
    numbers = ''
    for i in range(12):
        numbers += str(randrange(0,10))
    return numbers

cheat = False

class TestWidget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(800, 300)
        self.setStyleSheet("background-color: #284c78; color: white; font-weight: bold; font-size: 50px")

        self.startButton = QPushButton("Start")
        self.startButton.clicked.connect(self.switchShowPasswordPhase)
        self.startButton.setFixedSize(800, 130)

        self.message = QLabel("")
        self.message.setTextFormat(Qt.RichText)
        self.message.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setTextMessage("Black dongle trainer")

        self.input = QLineEdit()
        self.input.setMaxLength(12)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.message)
        self.layout.addWidget(self.startButton)
        
        print("[INFO ] ==========================================")
        print("[INFO ] =          Black Dongle Trainer          =")
        print("[INFO ] ==========================================")

    def switchShowPasswordPhase(self):
        print("[INFO ] Showing password")
        self.startButton.setParent(None)
        self.response = generate_number()
        self.setTextMessage(self.response)
        if cheat:
            print("[DEBUG] password: "+ self.response)
        QTimer.singleShot(3000, self.switchPhase2)

    def switchPhase2(self):
        print("[INFO ] intial time out")
        print("[INFO ] requesting password")
        self.setTextMessage("Enter password:")
        self.layout.addWidget(self.input)
        self.input.clear()
        self.input.setFocus()
        QTimer.singleShot(5000, self.switchResultPhase)


    def switchResultPhase(self):
        self.input.setParent(None)
        if self.input.text() == self.response:
            self.setTextMessage("Success, system bypassed")
            print("[INFO ] success!\npassword: " + self.response)
        else:
            self.setTextMessage("Failure, system locked")
            print("[ERROR] failed: incorect password\n[ERROR]    expected:\t" + self.response + "\n[ERROR]    user input:\t" + self.input.text())

        self.startButton.setText("Restart")
        self.layout.addWidget(self.startButton)

    def setTextMessage(self, message):
        self.message.setText(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cheat = True
    widget = TestWidget()
    widget.show()
    sys.exit(app.exec())
