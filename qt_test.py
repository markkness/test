#!/usr/bin/env python
'''
qt_test.py - Qt test program to check PySide installation.

Taken from:
http://en.wikipedia.org/wiki/PySide
'''

import sys
from PySide import QtCore, QtGui

app = QtGui.QApplication(sys.argv)
win = QtGui.QWidget()

win.resize(320, 240)
win.setWindowTitle("Hello, World!")
win.show()

sys.exit(app.exec_())
