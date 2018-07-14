#!/usr/bin/env python 
# -*- coding: utf-8 -*-


import logging
from logging.config import logging

logging.config.fileConfig('logging.cnf')

logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')
