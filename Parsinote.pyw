from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction, QToolBar, QPushButton, QFontDialog, QMessageBox, QLabel
from AutoCorrection import TextBox
from PyQt5.QtGui import QIcon, QTextCursor
from PyQt5.QtCore import Qt, pyqtSlot, QSize
from sys import argv
import webbrowser
import os


# The MainWindow class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.GUI()


    # The MAinWindow menu
    def pn_menu(self):

        # Create menu bar
        self.menu = self.menuBar()
        self.filemenu = self.menu.addMenu("فایل")
        self.editmenu = self.menu.addMenu("ویرایش")
        self.helpmenu = self.menu.addMenu("راهنما")

        # New button
        self.newitem = QAction(QIcon("data\\file.png"), "جدید", self)
        self.newitem.setShortcut("Ctrl+n")
        self.newitem.triggered.connect(self.new_BTN)

        # Save button
        self.saveitem = QAction(QIcon("data\\save.png"), "ذخیره", self)
        self.saveitem.setShortcut("Ctrl+s")
        self.saveitem.triggered.connect(self.save_BTN)

        # Save as button
        self.saveasitem = QAction(QIcon("data\\save.png"), "ذخیره بعنوان...", self)
        self.saveasitem.setShortcut("Ctrl+Shift+s")
        self.saveasitem.triggered.connect(self.saveas_BTN)

        # Open button
        self.openitem = QAction(QIcon("data\\folder.png"), "باز کردن...", self)
        self.openitem.setShortcut("Ctrl+o")
        self.openitem.triggered.connect(self.open_BTN)

        # Exit button
        self.exititem = QAction(QIcon("data\\exit.png"), "خروج", self)
        self.exititem.setShortcut("esc")
        self.exititem.triggered.connect(self.exit_BTN)

        # Font button
        self.fontitem = QAction(QIcon("data\\fonts.png"), "تغییر فونت", self)
        self.fontitem.setShortcut("Ctrl+f")
        self.fontitem.triggered.connect(self.font_BTN)

        # Bing button
        self.bingitem = QAction(QIcon("data\\internet.png"), "جستجو در بینگ", self)
        self.bingitem.setShortcut("Ctrl+e")
        self.bingitem.triggered.connect(self.bing_BTN)

        # About button
        self.aboutitem = QAction(QIcon("data\\info.png"), "درباره ما", self)
        self.aboutitem.setShortcut("Ctrl+i")
        self.aboutitem.triggered.connect(self.about_BTN)

        # Bug button
        self.bugitem = QAction(QIcon("data\\beetle.png"), "گزارش باگ", self)
        self.bugitem.setShortcut("Ctrl+b")
        self.bugitem.triggered.connect(self.bug_BTN)

        # Add file menu actions
        self.filemenu.addAction(self.newitem)
        self.filemenu.addAction(self.saveitem)
        self.filemenu.addAction(self.saveasitem)
        self.filemenu.addAction(self.openitem)
        self.filemenu.addAction(self.exititem)

        # Add edit menu actions
        self.editmenu.addAction(self.fontitem)
        self.editmenu.addAction(self.bingitem)

        # Add help menu actions
        self.helpmenu.addAction(self.bugitem)
        self.helpmenu.addAction(self.aboutitem)

    
    # The MAinWindow tool bar
    def pn_toolbar(self):
        self.toolbar = QToolBar()
        self.toolbar.move(0, 50)
        self.toolbar.resize(640, 64)
        self.addToolBar(self.toolbar)
        self.toolbar.setMovable(False)
        self.toolbar.setIconSize(QSize(64, 64))
        self.toolbar.setToolButtonStyle(Qt.ToolButtonFollowStyle)

        self.newtool = QAction(QIcon("data\\file.png"), "فایل جدید", self)
        self.newtool.triggered.connect(self.new_BTN)

        self.savetool = QAction(QIcon("data\\save.png"), "ذخیره", self)
        self.savetool.triggered.connect(self.save_BTN)

        self.opentool = QAction(QIcon("data\\folder.png"), "باز کردن...", self)
        self.opentool.triggered.connect(self.open_BTN)

        self.toolbar.addAction(self.newtool)
        self.toolbar.addAction(self.savetool)
        self.toolbar.addAction(self.opentool)


    # The MAinWindow GUI
    def GUI(self):
        self.setWindowTitle("ParsiNote_Lite")
        self.setWindowIcon(QIcon("data\\ParsiNote_Lite.png"))
        self.resize(640, 480)

        # Show menu
        self.pn_menu()

        # Show tool bar
        self.pn_toolbar()

        # Show text box
        self.text = TextBox(self)
        self.text.AutoCorrect()
        self.setCentralWidget(self.text)


    @pyqtSlot()

    # If new button pressed
    def new_BTN(self):
        self.text.new()
        self.setWindowTitle("ParsiNote_Lite" + " - " + os.path.basename(self.text.path))


    # If save button pressed
    def save_BTN(self):
        self.text.save()
        self.setWindowTitle("ParsiNote_Lite" + " - " + os.path.basename(self.text.path))


    # If save as button pressed
    def saveas_BTN(self):
        self.text.saveas()
        self.setWindowTitle("ParsiNote_Lite" + " - " + os.path.basename(self.text.path))


    # If open button pressed
    def open_BTN(self):
        self.text.open()
        self.setWindowTitle("ParsiNote_Lite" + " - " + os.path.basename(self.text.path))


    # If exit button pressed
    def exit_BTN(self):
        exit()


    # If font button pressed
    def font_BTN(self):
        font, _ = QFontDialog.getFont(self.text.font())
        self.text.setFont(font)


    # If bing button pressed
    def bing_BTN(self):
        if self.text.textCursor().selectedText() != "":
            webbrowser.open("https://www.bing.com/search?q={}".format(self.text.textCursor().selectedText()))
        
        else:
            webbrowser.open("https://www.bing.com/search?q={}".format(self.text.toPlainText()))


    # If bug button pressed
    def bug_BTN(self):
        webbrowser.open("https://github.com/mskf1383/parsinote_lite")
        webbrowser.open("https://gitlab.com/mskf1383/parsinote_lite")


    # If about button pressed
    def about_BTN(self):
        
        aboutwindow.show()


# The AboutWindow class
class AboutWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.GUI()

    
    # The AboutWindow GUI
    def GUI(self):
        self.setWindowTitle("About Us")
        self.setWindowIcon(QIcon("data\\ParsiNote_Lite.png"))
        self.setFixedSize(320, 240)

        # Info Label
        self.label = QLabel("نام برنامه: پارسی نوت لایت\nنسخه: بتا1\nسازنده: محمدصالح کامیاب\nنوشته شده با: پایتون و PyQt5\nگرافیک از:\nhttps://www.flaticon.com\n", self)
        self.label.setAlignment(Qt.AlignCenter)

        # GitHub button
        self.github = QPushButton("سورس در گیت‌هاب", self)
        self.github.resize(160, 40)
        self.github.move(0, 200)
        self.github.clicked.connect(self.goHub)

        # GitLab button
        self.gitlab = QPushButton("سورس در گیت‌لب", self)
        self.gitlab.resize(160, 40)
        self.gitlab.move(160, 200)
        self.gitlab.clicked.connect(self.goLab)

        self.setCentralWidget(self.label)

        self.setStyleSheet("QMainWindow{background: #eee;}")


    @pyqtSlot()

    # If GitHub button pressed
    def goHub(self):
        webbrowser.open("https://gitlab.com/mskf1383/parsinote_lite")


    # If GitLab button pressed
    def goLab(self):
        webbrowser.open("https://github.com/mskf1383/parsinote_lite")


# Run the app
if __name__ == "__main__":
    app = QApplication(argv)
    app.setLayoutDirection(Qt.RightToLeft)
    with open("data\\style.css") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()

    aboutwindow = AboutWindow()

    app.exec_()