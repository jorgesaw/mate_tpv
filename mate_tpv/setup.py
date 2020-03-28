#!/usr/bin/env python
# -*- encoding: utf8 -*-

#http://stackoverflow.com/questions/1570542/when-using-py2exe-pyqt-application-cannot-load-sqlite-database
#https://bitbucket.org/bjones/documentation/src/22c5d75235cc2da38215b1f7752110209d7d7045/setup.py?at=default Excelente
#http://www.blog.pythonlibrary.org/2010/07/31/a-py2exe-tutorial-build-a-binary-series/

u"""Clase que genera la distribución de la app empquetada."""

import os
import sys
#from setuptools import setup, find_packages
from distutils.core import setup
import py2exe

if 'py2exe' in sys.argv:
    import py2exe
    from glob import glob
    import shutil
    #http://py2exe.org/index.cgi/Tutorial#Step52
    sys.path.append('dll\\Microsoft.VC90.CRT')
    data_files = [
        ("Microsoft.VC90.CRT", glob(r'dll\Microsoft.VC90.CRT\*.*')),
        #("datos_java", glob(r'datos_java\*.*')), 
        #("datos_java\lib", glob(r'datos_java\lib\*.*')), 
        #("BCK", glob(r'BCK\*.*'))
    ]
    shutil.copy(r'config.txt', r'dist/config.txt')
    shutil.copy(r'mate_tpv.db', r'dist/mate_tpv.db')
    #shutil.copy(r'darkorange.qss', r'dist/darkorange.qss')
    shutil.copy(r'logging.conf', r'dist/logging.conf')
    
def find_packages(location):
    packages = []
    for pkg in ['mate']:
        for _dir, subdirectories, files in (
                os.walk(os.path.join(location, pkg))):
            if '__init__.py' in files:
                tokens = _dir.split(os.sep)[len(location.split(os.sep)):]
                packages.append(".".join(tokens))
    return packages

# Avoids "error: compiling 'C:\Python27\lib\site-packages\PyQt4\uic\port_v3\proxy_base.py'  failed: SyntaxError: invalid syntax (proxy_base.py, line 31)".
excludes = [] #['PyQt4.uic.port_v3'],
dll_excludes = [] #["msvcp90.dll",]
includes = ['sip', ]
packages = ["sqlalchemy", "PyQt4"]

setup(name="Mate TPV",
      version="0.6",
      description="Programa para punto de venta.",
      author="Jorge Adrian Gonzalez",
      author_email="jorgesaw@gmail.com",
      url="http://www.jorgesaw.com.ar",
      license="XXX",
      packages=find_packages('mate'),#['superbingo',],
      package_dir={'mate': 'mate'}, 
      package_data={'mate': ['img/*.*',]},
      requires=['PyQt4'],
      data_files = data_files,
      console=['tpv_run.py'],
      windows=[{'script': 'tpv_run.py',
               'icon_resources': [(1, 'mate_tpv.ico')]
                }],
      scripts=["tpv_run.py"], 
      options={"py2exe": {
          "excludes" : excludes,
          "dll_excludes" :  dll_excludes, 
          "includes" : includes,
          "packages" : packages
          }}      
      )