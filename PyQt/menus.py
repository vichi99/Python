from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.setWindowTitle("My App")

        label = QLabel("Nice")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        toolbar = QToolBar("main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        self.setStatusBar(QStatusBar(self))

        # icon from http://p.yusukekamiyamane.com/
        button_action = QAction(QIcon("box.png"), "&My button", self)
        button_action.setStatusTip("This is my button")
        button_action.triggered.connect(self.BarButtonClick)
        button_action.setCheckable(True)    # set to False, True, Fale....
        button_action.setShortcut(QKeySequence("Ctrl+p"))
        # button_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_P))
        # button_action.setShortcut(QKeySequence(QKeySequence.Print))
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon("box.png"), "My &button2", self)
        button_action2.setStatusTip("This is my button 2")
        button_action2.triggered.connect(self.BarButtonClick)
        button_action2.setCheckable(True)    # set to False, True, Fale....
        toolbar.addAction(button_action2)

        toolbar.addSeparator()

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        menu = self.menuBar()
        menu.setNativeMenuBar(False) # Disable the global menu bar on macOS

        file_menu = menu.addMenu(u"&File")
        file_menu.addAction(button_action)

        file_menu.addSeparator()

        file_submenu = file_menu.addMenu("Submenu")

        file_submenu.addAction(button_action2)

    def BarButtonClick(self,s):
        print("click", s)

app = QApplication(sys.argv)
Window = MainWindow()
Window.show()
app.exec_()
