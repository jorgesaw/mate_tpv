#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 10/02/2015

@author: jorgesaw
'''

import logging
import logging.config

logging.config.fileConfig('logging.conf')

# create logger
logger = logging.getLogger(__name__)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

logger = logging.getLogger('__name__')

# 'application' code
logger.debug('debug message'.upper())
logger.info('info message'.upper())
logger.warn('warn message'.upper())
logger.error('error message'.upper())
logger.critical('critical message'.upper())