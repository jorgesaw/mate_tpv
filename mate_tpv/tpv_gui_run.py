#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 12/02/2015

@author: jorgesaw
'''
from __future__ import absolute_import, print_function, unicode_literals
from mate.vista import factoria
from mate.vista.factoria.mostrarVentanaGui import MostrarVentanaGui
from mate.vista.main.MainWindowMateTPV import MainWindowMateTPV
import PyQt4.QtGui as _qg
import ctypes
import logging
import logging.config
import mate.vista.main.qrc_main_window
import sys

"""
Runs tpv
"""

#u Líneas de código para que el ícono de la app aparezca en la taskbar de Win 7.
#u http://stackoverflow.com/questions/1551605/how-to-set-applications-taskbar-icon-in-windows-7/1552105#1552105
# import ctypes
# myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
# ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
myappid = 'jorgesaw.Bingo.MateTPV.0.7'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

logging.config.fileConfig('logging.conf')

logger = logging.getLogger(__name__)

#logging.getLogger(__name__)
#logging.basicConfig(filename='superbingo.log',level=logging.DEBUG, 
#           format='%(levelname)s | %(asctime)s | %(message)s', 
#                  datefmt='%m-%d-%Y %H:%M:%S')
    
def main():
    logger.info(u'Iniciando la aplicación...')
    
    #app = _qg.QApplication(sys.argv)
    
    #app.setStyle("plastique")
    #app.setOrganizationName("Jorgesaw Inc.")
    #app.setOrganizationDomain("jorgesaw.com.ar")
    #app.setApplicationName(u"Mate TPV")
    #app.setWindowIcon(_qg.QIcon(":/favicon.png"))
    
    #RecursosCSS.cargarRecursoCss(os.curdir + '\\darkorange.qss')
    #app.setStyleSheet(RecursosCSS.CSS)
    
    #splash_pix = QPixmap(':/favicon.png')
    #splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    #splash.setMask(splash_pix.mask()) # this is usefull if the splashscreen is not a regular ractangle...
    #splash.show()
    #splash.showMessage((u'Cargando...'), Qt.AlignCenter | Qt.AlignCenter, Qt.white)

    #time.sleep(2)
    
    #app.processEvents()
    
    mvg = MostrarVentanaGui(factoria.GUI_MATE_TPV)
    window = mvg.prepararVentana()
    return window
    #window.showMaximized()
    #splash.finish(window)
    
    #sys.exit(app.exec_())

if __name__ == "__main__":
    main()