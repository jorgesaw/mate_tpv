#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 15/02/2015

@author: jorgesaw
'''

from __future__ import absolute_import, print_function, unicode_literals
from mate.core.util import util
from mate.vista import factoria

PATH_MODELS = 'mate.model.dto.'

MODEL_NAMES = {factoria.ARTICLE_NEW: 'Article', 
               factoria.ARTICLE_SHOW: 'Article'}

IDX_ARTICLE = range(1)

def getClaseModelo(tipo):
    return util.import_class(PATH_MODELS + MODEL_NAMES[tipo])