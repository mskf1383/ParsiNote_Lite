from PyQt5.QtWidgets import QTextEdit, QMenu, QAction, QFileDialog
from PyQt5.QtCore import Qt, QLocale
from PyQt5.QtGui import QCursor

class TextBox(QTextEdit):
    path = ""


    # Auto correction function
    def AutoCorrect(self):
        self.textChanged.connect(self.text_changed)
        self.setAcceptRichText(False)

        self.setLayoutDirection(Qt.RightToLeft)
        self.setLocale(QLocale(QLocale.Persian, QLocale.Iran))
        self.setPlainText(self.toPlainText())
        

    # New metod
    def new(self):
        self.path, _ = QFileDialog.getSaveFileName(self, "New file", "", "Text documents (*.txt)")

        if self.path:
            try:
                with open(self.path, "w") as f:
                    f.write()
                    self.setPlainText("")
            
            except:
                pass
        
    
    # Save metod
    def save(self):
        if self.path:
            try:
                with open(self.path, "w") as f:
                    f.write(self.toPlainText())
            
            except:
                pass
        
        else:
            self.saveas()


    # Save as metod
    def saveas(self):
        self.path, _ = QFileDialog.getSaveFileName(self, "Save", "", "Text documents (*.txt)")

        if self.path:
            try:
                with open(self.path, "w") as f:
                    f.write(self.toPlainText())
            
            except:
                pass

    
    # Open as metod
    def open(self):
        self.path, _ = QFileDialog.getOpenFileName(self, "Open...", "", "Text documents (*.txt)")

        if self.path:
            try:
                with open(self.path, "r") as f:
                    self.setPlainText(f.read())
            
            except:
                pass

    # When the text change this function run
    def text_changed(self):

        # Get the mouse position
        old_position = self.textCursor().position()
        new_cursor = self.textCursor()
        new_cursor.setPosition(old_position)

        # Correct space
        if "  " in self.toPlainText():
            self.setPlainText(self.toPlainText().replace("  ", " "))
            self.setTextCursor(new_cursor)


        symb = [".", "،", "؛", ",", "؟", "!", ":"]

        alph = ["آ", "ا", "ب", "پ", "ت", "ث", "ج", "چ", "ح", "خ", "د", "ذ", "ر", "ز", "ژ", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل", "م", "ن", "و", "ه", "ی", "ئ", "ِ", "ُ", "َ", "ّ", "ۀ", "ي", "ؤ", "إ", "أ", "ء", "ٍ", "ٌ", "ً"]

        # Correct symbols
        for a in alph:
            for s in symb:
                if " ." in self.toPlainText():
                    self.setPlainText(self.toPlainText().replace(" {}".format(s), "{} ".format(s)))
                    self.setTextCursor(new_cursor)

                if "{}{}".format(s, a) in self.toPlainText().lower():
                    self.setPlainText(self.toPlainText().replace("{}{}".format(s, a), "{} {}".format(s, a)))
                    self.setTextCursor(new_cursor)

        self.lenght = len(self.toPlainText())