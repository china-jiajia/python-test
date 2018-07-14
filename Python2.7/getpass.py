#!/usr/bin/env python 
# -*- coding: utf-8 -*-



from __future__ import print_function
import getpass


# user = getpass.getuser()
passwd = getpass.getpass('input your password: ')
print(passwd)