#pyuic5 -x test1.ui -o test1.py

from test1 import Ui_MainWindow
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QWidget


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent=parent)

        self.api=str('')
        self.state=0

        self.setupUi(self)

        self.pushButton_HandUp.clicked.connect(self.buttonExecute_HandUp)
        self.pushButton_HandDown.clicked.connect(self.buttonExecute_HandDown)
        self.pushButton_HandLeft.clicked.connect(self.buttonExecute_HandLeft)
        self.pushButton_HandRight.clicked.connect(self.buttonExecute_HandRight)

        self.pushButton_BodyUp.clicked.connect(self.buttonExecute_BodyUp)
        self.pushButton_BodyDown.clicked.connect(self.buttonExecute_BodyDown)
        self.pushButton_BodyLeft.clicked.connect(self.buttonExecute_BodyLeft)
        self.pushButton_BodyRight.clicked.connect(self.buttonExecute_BodyRight)

        self.pushButton_StateSwitch.clicked.connect(self.buttonExecute_StateSwitch)
        self.pushButton_APIcall.clicked.connect(self.buttonExecute_APIcall)


        self.setChildrenFocusPolicy(QtCore.Qt.StrongFocus)

    def setChildrenFocusPolicy(self, policy):
        def recursiveSetChildFocusPolicy(parentQWidget):
            for childQWidget in parentQWidget.findChildren(QWidget):
                childQWidget.setFocusPolicy(policy)
                recursiveSetChildFocusPolicy(childQWidget)

        recursiveSetChildFocusPolicy(self)

    def keyPressEvent(self, e):
        if e.key() == 96 :
            #Qt.Key_Escape
            print("Exit")
            self.close()

        elif e.key() == Qt.Key_W:
            self.buttonExecute_HandUp()
        elif e.key() == Qt.Key_S:
            self.buttonExecute_HandDown()
        elif e.key() == Qt.Key_A:
            self.buttonExecute_HandLeft()
        elif e.key() == Qt.Key_D:
            self.buttonExecute_HandRight()

        elif e.key() == Qt.Key_Up:
            self.buttonExecute_BodyUp()
        elif e.key() == Qt.Key_Down:
            self.buttonExecute_BodyDown()
        elif e.key() == Qt.Key_Left:
            self.buttonExecute_BodyLeft()
        elif e.key() == Qt.Key_Right:
            self.buttonExecute_BodyRight()


        else:
            print(e.key())
            self.showCurrentValues()

    def func(self):
        pass

    def showCurrentValues(self):
        print("State: %s \nIndex: %d" % (self.comboBox_State.itemText(self.state), self.state))
        print("API: %s"%self.api)

    def buttonExecute_StateSwitch(self):
        self.state=self.comboBox_State.currentIndex()
        print("State: %s \nIndex: %d" % (self.comboBox_State.itemText(self.state), self.state))

    def buttonExecute_APIcall(self):
        self.api =self.lineEdit_API.text()
        print(self.api)

    def buttonExecute_HandUp(self):
        print("Key pressed: W\nKey code: " + str(Qt.Key_W))

    def buttonExecute_HandDown(self):
        print("Key pressed: S\nKey code: " + str(Qt.Key_S))

    def buttonExecute_HandLeft(self):
        print("Key pressed: A\nKey code: " + str(Qt.Key_A))

    def buttonExecute_HandRight(self):
        print("Key pressed: D\nKey code: " + str(Qt.Key_D))


    def buttonExecute_BodyUp(self):
        print("Key pressed: Up\nKey code: " + str(Qt.Key_Up))

    def buttonExecute_BodyDown(self):
        print("Key pressed: Down\nKey code: " + str(Qt.Key_Down))

    def buttonExecute_BodyLeft(self):
        print("Key pressed: Left\nKey code: " + str(Qt.Key_Left))

    def buttonExecute_BodyRight(self):
        print("Key pressed: Right\nKey code: " + str(Qt.Key_Right))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
