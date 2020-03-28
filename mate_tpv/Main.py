#!/usr/bin/env python
# -*- coding: utf-8 -*-

#u Líneas de código para que el ícono de la app aparezca en la taskbar de Win 7.
#u http://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
# import ctypes
# myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
# ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

import logging
import logging.config
from PyQt4.QtGui import (QApplication, QIcon, QSplashScreen, QPixmap, QMessageBox)
from PyQt4.QtCore import Qt
from core.util.RecursosCSS import RecursosCSS
from mate.vista.main.mainWindow import MainWindow
import ctypes
from core.util.ManejaFechas import ManejaFechas
import sys
import os
import time
from datetime import date
import mate.vista.main.qrc_main_window
myappid = 'jorgesaw.Bingo.Superbingo.1.1'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

sys.path.append('./')

logging.config.fileConfig('logging.conf')

logger = logging.getLogger(__name__)

#logging.getLogger(__name__)
#logging.basicConfig(filename='superbingo.log',level=logging.DEBUG, 
#           format='%(levelname)s | %(asctime)s | %(message)s', 
#                  datefmt='%m-%d-%Y %H:%M:%S')


def main():
    logger.info(u'Iniciando la aplicación...')
    
    app = QApplication(sys.argv)
    
    #app.setStyle("plastique")
    app.setOrganizationName("Jorgesaw Inc.")
    app.setOrganizationDomain("jorgesaw.com.ar")
    app.setApplicationName(u"SúperBingo")
    app.setWindowIcon(QIcon(":/favicon.png"))
    
    #RecursosCSS.cargarRecursoCss(os.curdir + '\\darkorange.qss')
    #app.setStyleSheet(RecursosCSS.CSS)
    
    #splash_pix = QPixmap(':/favicon.png')
    #splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    #splash.setMask(splash_pix.mask()) # this is usefull if the splashscreen is not a regular ractangle...
    #splash.show()
    #splash.showMessage((u'Cargando...'), Qt.AlignCenter | Qt.AlignCenter, Qt.white)

    #time.sleep(2)
    
    #app.processEvents()
    
    window = MainWindow(None)
    
    window.show()
    window.m()
    #splash.finish(window)
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    