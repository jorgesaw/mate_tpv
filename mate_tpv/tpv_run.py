#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 12/02/2015

@author: jorgesaw
'''

"""
Runs tpv
"""
import ctypes
myappid = 'jorgesaw.Mate_TPV.Mate_TPV.0.6'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

import mate

mate.run()
