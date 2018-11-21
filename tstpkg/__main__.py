#!/usr/bin/env python
import os, sys
 
print('__main__')
print('__main__.__name__', __name__)
print('__main__.__package__', __package__)
 
if not __package__:
  path = os.path.join(os.path.dirname(__file__), os.pardir)
  sys.path.insert(0, path)
 
print('sys.path', sys.path)
 
import tstpkg
tstpkg.main()