x=11

# 1st way of import module in current folder
# import mypackage.subpackage1.uutil as uutil 


# 2nd way of import module in current folder 
from . import uutil

def showGood(pig):
    uutil.good(pig)