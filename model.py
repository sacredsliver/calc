
import Komp
import rac
TYPE_NUM = None

def init(in_a, in_b, type_num):
    global TYPE_NUM
    TYPE_NUM = type_num
    if type_num:
        Komp.init(in_a, in_b)
        
    else:
        rac.init(in_a, in_b)
            
def mult():
    if TYPE_NUM:
        return Komp.mult()   # указать функцию
    else:
        return rac.mult()

def sum():
    if TYPE_NUM:
        return Komp.sum()   # указать функцию
    else:
        return rac.sum()

def div():
    if TYPE_NUM:
        return Komp.div()   # указать функцию
    else:
        return rac.div()

def sub():
    if TYPE_NUM:
        return Komp.sub()   # указать функцию
    else:
        return rac.sub()





