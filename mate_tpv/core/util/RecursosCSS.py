#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 22/01/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals

class RecursosCSS(object):
    
    CSS = ''
    
    @staticmethod
    def cargarRecursoCss(file):
        with open(file, 'r') as fh:
            RecursosCSS.CSS = fh.read()
            