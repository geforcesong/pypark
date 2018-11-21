import sys
sys.path.insert(0, './utils')

from utils import *
from module1 import disp1

disp1()
# disp2()

module2.display() # pylint: disable=E0602
mmm3.displayM() # pylint: disable=E0602