#!/usr/bin/env python
# -*- coding utf8 -*-

import  multiprocessing as mp

value = mp.Value('d',1)
array = mp.Array('i',[1,2,3])


#   Python C type code种类
#   https://docs.python.org/3.5/library/array.html