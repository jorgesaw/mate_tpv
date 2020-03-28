#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import QSettings, QVariant, QSize, QPoint, Qt
from PyQt4.QtGui import QMainWindow, QFrame, QLabel, QWorkspace, QIcon, \
    QMessageBox, QPixmap, QBrush
from core.gui.Actions import addActions, createAction
from mate.vista.gui.dlg.NewProductDlg import NewProductDlg
import logging
import sys
sys.path.append('./')

logging.getLogger(__name__)

class MainWindow(QMainWindow):
    u"""Ventana principal de la aplicación."""

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        #self.mdiArea = QMdiArea()
        #self.mdiArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        #self.mdiArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.mdi = QWorkspace()
        bc = QPixmap(':/fondo_abstracto.png')
        bc = bc.scaled(700, 640, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        br = QBrush(bc)
        
        self.mdi.setBackground(br)
        self.mdi.setAutoFillBackground(False)
        self.setCentralWidget(self.mdi)

        self.createActions()
        self.createMenus()
        self.createToolBar()
        self.createStatusBar()
        self.loadSettings() # uModifica tamaño y agrega "archivos recientes" y otros.

        #self.setUnifiedTitleAndToolBarOnMac(True)
        self.setWindowIcon(QIcon(":/favicon.png"))
        
        #key = QShortcut(QKeySequence(Qt.Key_F10), self) # uNo funciona cuando la búsqueda devuelve una lista vacía porque no encontró datos.
        #self.connect(key, SIGNAL("activated()"), self.mensaje)
        
    #def mensaje(self):
    #   print "Tecla F10 activada!!!"
        
    def createActions(self):
        self.archivoSalirAction = createAction(self, "&Salir", self.close, "Alt+F4", "quit.png",
                     u"Salir de la aplicación", signal="triggered()")
        self.datosBingoAction = createAction(self, "&Bingos", icon="game.png", 
                                       slot=self.datosBingo, tip=unicode("Crear Bingo"))
        self.datosEmpleadoAction = createAction(self, "&Empleados",
                                             slot=self.datosEmpleado, tip=unicode("Empleados"))
        self.datosInstitAction = createAction(self, "&Instituciones",
                                             slot=self.datosInstit, tip=unicode("Instituciones"))
        self.datosLoteriaAction = createAction(self, "&Loterias",
                                         slot=self.datosLoteria, tip=unicode("Loterias"))
        self.datosCiudadAction = createAction(self, "&Ciudades",
                                        slot=self.datosCiudad, tip=unicode("Ciudades"))
        self.cartonesAddAction = createAction(self, "&Agregar...", icon="sorteos.png", 
                                        slot=self.cartonesAdd, tip=unicode("Agregar..."))
        self.cartonesDetalleAction = createAction(self, u"D&etalle cartón",
                                        slot=self.cartonesDetalle, tip=unicode(u"Detalle cartón"))
        self.cuotasConsigAction = createAction(self, "&Consignar cuota",
                                        slot=self.cuotasConsig, tip=unicode("Consignar cuota"))
        self.cuotasRendirAction = createAction(self, "&Rendir cuota",
                                        slot=self.cartonesAdd, tip=unicode("Rendir cuota"))
        self.datosCargaSorteoAction = createAction(self, "Carga de &Sorteos",
                                             slot=self.cargaSorteos, tip=unicode("Cargar sorteos"))
        self.ganadoresBusquedaAction = createAction(self, "&Buscar...",
                                             slot=self.ganadoresBuscar, tip=unicode("Buscar..."))
        self.dbResguardarAction = createAction(self, "Resguardar",
                                                   slot=self.resguardarDB, tip=unicode("Resguardar"))
        self.dbRestaurarAction = createAction(self, "Restaurar",
                                                   slot=self.restaurarDB, tip=unicode("Restaurar"))
        #self.dbExportarAction = createAction(self, "Exportar",
        #                                          slot=self.exportarDB, tip=unicode("Exportar"))

    def createMenus(self):
        self.archivoMenu = self.menuBar().addMenu("&Archivo")
        
        self.archivoDb = self.archivoMenu.addMenu("&Base de datos")
        self.DBMenuActions = (self.dbResguardarAction, 
                              self.dbRestaurarAction, 
                              #self.dbExportarAction
                              )
        addActions(self, self.archivoDb, self.DBMenuActions)
        
        self.archivoMenuActions = (self.archivoSalirAction, )
        addActions(self, self.archivoMenu, self.archivoMenuActions)

        self.datosMenu = self.menuBar().addMenu("&Datos")
        self.datosMenuActions = (self.datosBingoAction, None,
                                 self.datosEmpleadoAction, self.datosInstitAction,
                                 self.datosLoteriaAction, self.datosCiudadAction, None,
                                 self.datosCargaSorteoAction
                                 )
        addActions(self, self.datosMenu, self.datosMenuActions)

        #self.editMenuCargaSorteo = self.datosMenu.addMenu("Carga de &Sorteos")
        #self.createMenuLoterias()

        self.cartonesMenu = self.menuBar().addMenu('Cart&ones')
        self.cartonesMenuActions = (self.cartonesAddAction, None, self.cartonesDetalleAction)
        addActions(self, self.cartonesMenu, self.cartonesMenuActions)
        self.cartonesMenuMayores = self.cartonesMenu.addMenu('&Mayor...')
        self.cartonesMenuTalon = self.cartonesMenu.addMenu(u'&Talón individual')
        self.createMenuMayores()
        self.createMenuTalon()

        self.cuotasMenu = self.menuBar().addMenu('C&uotas')
        self.cuotasMenuActions = (self.cuotasConsigAction, self.cuotasRendirAction)
        addActions(self, self.cuotasMenu, self.cuotasMenuActions)

        self.ganadoresMenu = self.menuBar().addMenu('Ganadore&s')
        self.ganadoresMenuActions = (self.ganadoresBusquedaAction, )
        addActions(self, self.ganadoresMenu, self.ganadoresMenuActions)

    def createMenuMayores(self):
        self.cartonesVendedoresAction = createAction(self, "por &Vendedor", slot=self.genMayorEmpl)
        self.cartonesGeneralAction = createAction(self, "&General", slot=self.cargaSorteos)
        self.cartonesGrupoVendedoresAction = createAction(self, "G&rupo de vendedores", slot=self.cargaSorteos)
        self.cartonesCuotaAction = createAction(self, "por &Cuota", slot=self.cargaSorteos)
        addActions(self, self.cartonesMenuMayores, (self.cartonesVendedoresAction, self.cartonesGeneralAction, 
                                                    self.cartonesGrupoVendedoresAction,
                                                    self.cartonesCuotaAction))
    def createMenuTalon(self):
        self.cargaDatosAction = createAction(self, "&Carga de datos", slot=self.cargarDatosVenta)
        self.consignarVentaAction = createAction(self, u"&Consignar Cartón", slot=self.consignarVenta)
        self.consignarListaVentasAction = createAction(self, u"&Consignar lista de Cartones",
                                                       slot=self.consignarListaVentas)
        addActions(self, self.cartonesMenuTalon, (self.cargaDatosAction, self.consignarVentaAction,
                                                  self.consignarListaVentasAction))
        
    def createToolBar(self):
        self.datosToolBar = self.addToolBar("Datos")
        self.datosToolBar.setObjectName("datosToolBar")
        addActions(self, self.datosToolBar, (self.datosBingoAction, 
                                             self.cartonesAddAction))

    def createStatusBar(self):
        self.sizeLabel = QLabel("")
        self.sizeLabel.setFrameStyle(QFrame.StyledPanel|QFrame.Sunken)
        status = self.statusBar()
        status.setSizeGripEnabled(False)
        status.addPermanentWidget(self.sizeLabel)
        status.showMessage("Comenzar", 5000)

    def loadSettings(self):
        settings = QSettings()
        size = settings.value("MainWindow/Size",
                              QVariant(QSize(600, 500))).toSize()
        self.resize(size)
        position = settings.value("MainWindow/Position",
                              QVariant(QPoint(0, 0))).toPoint()
        self.move(position)
        self.restoreState(
                settings.value("MainWindow/State").toByteArray())
        self.setWindowTitle(u"SúperBingo")

    def closeEvent(self, event):
        #uTambién guardamos la geometria(tamaño) de la ventana de la app.
        if self.okToContinue():
            settings = QSettings()
            settings.setValue("MainWindow/Size", QVariant(self.size()))
            settings.setValue("MainWindow/Position", QVariant(self.pos()))
            settings.setValue("MainWindow/State", QVariant(self.saveState()))
            #settings.setValue("Geometry", QVariant(self.saveGeometry()))
            logging.info(u'Cerrando la aplicación...')
            event.accept()
        else:
            event.ignore()

    def okToContinue(self):
        #reply = QMessageBox.question(self,
        #                            u"SúperBingo - Salir",
        #                           u"¿Desea salir de la aplicación?",
        #                          QMessageBox.Yes|QMessageBox.No|
        #                         QMessageBox.Cancel)
        #if reply != QMessageBox.Yes:
        reply = QMessageBox.question(self,
                                     u"SúperBingo - Salir",
                                     u"¿Desea salir de la aplicación?",
                                     u'Sí',
                                     u'No',
                                     u'Cancelar')
        if reply != 0: #uSi no eligió sí
            return False
        return True
    
    #def exportarDB(self):
     #   pass
    
    def resguardarDB(self):    
        pass##vista = ProgressFileDlg()
        #db = DataBase(vista)
        #db.resguardarDb()

    def restaurarDB(self):
        pass##vista = ProgressFileDlg()
        #vista.msgLabel.setText('Restaurando base de datos...')
        #db = DataBase(vista)
        #db.restaurarDb()
        
    def datosBingo(self):
        pass#self.cargarVentana(VentanasGui.ADD_BINGO)

    def datosEmpleado(self):
        pass#self.cargarVentana(VentanasGui.CRUD_EMPLEADO)
            
    def datosInstit(self):
        pass#self.cargarVentana(VentanasGui.CRUD_INSTIT)
            
    def datosLoteria(self):
        pass#self.cargarVentana(VentanasGui.CRUD_LOTERIA)
            
    def datosCiudad(self):
        pass#self.cargarVentana(VentanasGui.CRUD_CIUDAD)
        
    def cargaSorteos(self):
        pass#self.cargarVentana(VentanasGui.CARGA_SORTEOS)

    def cartonesAdd(self):
        pass#self.cargarVentana(VentanasGui.ADD_CARTONES)
    
    def cartonesDetalle(self):
        pass#self.cargarVentana(VentanasGui.DETALLE_CARTON)
        
    def consignarVenta(self):
        pass#self.cargarVentana(VentanasGui.CONSIGNAR_VENTA)
        
    def consignarListaVentas(self):
        pass#self.cargarVentana(VentanasGui.CONSIG_LISTA_VENTAS)
        
    def cargarDatosVenta(self):
        pass#self.cargarVentana(VentanasGui.CARGA_DATOS_VENTA)
        
    def ganadoresBuscar(self):
        pass#self.cargarVentana(VentanasGui.BUSCAR_GANADORES)
                
    def cargarVentana(self, ventana):
        gui = None#FactoriaVentanas.crearVentanaGui(ventana)
        if not self.isWindowActived(gui.tipo()):
            dlg = gui.prepararVentana(parent=self.mdi)        
            if dlg:
                self.mostrarWindow(dlg)
                        
    def avisarCrudLoteria(self, tipoLot, cambio):
        pass

    def cuotasConsig(self):
        pass
    
    def cuotasRendir(self):
        pass

    def genMayorEmpl(self):
        pass
    
    def mostrarWindow(self, window):
        if len(self.mdi.windowList()) > 0:
            self.mdi.closeAllWindows()
        self.mdi.addWindow(window)
        window.show()
        
    def isWindowActived(self, tipo):
        u""""""
        for window in self.mdi.windowList():
            if isinstance(window, tipo):
                return True
        return False
    
    def m(self):
        #modelo = ModeloTabla(None, None)
        #ventana = CRUD(modelo)
        
        ventana = NewProductDlg()
        ventana.move(0, 0)
        
        if len(self.mdi.windowList()) > 0:
            self.mdi.closeAllWindows()
        self.mdi.addWindow(ventana)
        ventana.show()