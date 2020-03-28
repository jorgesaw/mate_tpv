#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('./')

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import PyQt4
import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

class FilterReturn(QtCore.QObject):
    def eventFilter(self, source, event):
        if (event.type()==QEvent.KeyPress):
            if event.key()==Qt.Key_Return:
                source.emit(SIGNAL("returnPressed()"))
        return QtGui.QWidget.eventFilter(self, source, event)