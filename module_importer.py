import sys
sys.path.insert(0, './utils')

from utils import *
from module1 import disp1
import utils.module2
from utils.module2 import display

disp1()
# disp2()

module2.display() # pylint: disable=E0602
mmm3.displayM() # pylint: disable=E0602
utils.module2.display();
display()