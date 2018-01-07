#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we dispay an image
on the window.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

from PyQt5.QtWidgets import (
        QWidget,
        QApplication,
        QTextEdit,
        QSplitter,
        QVBoxLayout,
        QPushButton,
        QLabel
        )
from PyQt5.QtCore import Qt
import sys


class SnipNTop(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def clipboard(self):
        return QApplication.clipboard()

    def initUI(self):
        hbox = QVBoxLayout(self)
        hbox.setSpacing(0)
        hbox.setContentsMargins(0, 0, 0, 0)
        pixmap = self.clipboard().pixmap()

        splitter = QSplitter(Qt.Vertical)

        if pixmap:
            lbl = QLabel(self)
            lbl.setPixmap(
                    pixmap.scaled(pixmap.width() / 2, pixmap.height() / 2)
                    )

            button = QPushButton('Copiar y cerrar', self)
            splitter.addWidget(lbl)
        else:
            button = QPushButton('cerrar', self)

        button.clicked.connect(self.copy_and_exit)
        button.setFocusPolicy(Qt.NoFocus)

        self.textEdit = QTextEdit()
        self.textEdit.setFocus()

        splitter.addWidget(self.textEdit)
        splitter.addWidget(button)
        hbox.addWidget(splitter)
        self.setLayout(hbox)

        self.move(0, 0)
        self.setWindowTitle('snip-n-top')
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.show()

    def copy_and_exit(self, event):
        self.clipboard().setText(self.textEdit.toPlainText())
        return self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SnipNTop()
    sys.exit(app.exec_())
