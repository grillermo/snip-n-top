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
        QPushButton
        )
from PyQt5.QtCore import Qt, QCoreApplication, QSize
import sys
from PyQt5.QtGui import QIcon


class SnipNTop(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QVBoxLayout(self)
        hbox.setSpacing(0)
        hbox.setContentsMargins(0, 0, 0, 0)
        pixmap = QApplication.clipboard().pixmap()

        splitter = QSplitter(Qt.Vertical)

        if pixmap:
            button = QPushButton('', self)
            button.setIcon(QIcon(pixmap))
            button.isFlat = True
            button.setIconSize(
                    QSize(
                        pixmap.width() / 2,
                        pixmap.height() / 2
                        )
                    )

            button.clicked.connect(QCoreApplication.instance().quit)
            button.setFocusPolicy(Qt.NoFocus)
            splitter.addWidget(button)

        textEdit = QTextEdit()
        textEdit.setFocus()

        splitter.addWidget(textEdit)
        hbox.addWidget(splitter)
        self.setLayout(hbox)

        self.move(0, 0)
        self.setWindowTitle('snip-n-top')
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.show()

    def exit(self, event):
        return self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SnipNTop()
    sys.exit(app.exec_())
