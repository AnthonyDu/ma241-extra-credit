from sympy.core import *
from sympy.parsing.sympy_parser import *

class Fx:

    def __init__(self, expr):
        self.expr = expr
        self.x = Symbol("x")
        self.transformations = standard_transformations + (implicit_multiplication_application, convert_xor)

    def is_valid_fx(self):
        try:
            f = parse_expr(self.expr, transformations=self.transformations)
        except:
            print("invalid symbols found")
            return False
        if self.x in f.atoms(Symbol) and len(f.atoms(Symbol)) == 1:
            return True
        else:
            print("x is the only variable allowed")
            return False

    def get_fx(self):
        if self.is_valid_fx():
            return parse_expr(self.expr, transformations=self.transformations)

    def evaluate_fx(self, x_value):
        return N((self.get_fx()).subs(self.x, x_value))

def sympy_number_to_str(num):
    if str(num) == "oo" or str(num) == "zoo":
        return "infinity"
    if num % 1 == 0:
        return str(int(num))
    else:
        num_str = str(num)
        while num_str[-1] == "0":
            num_str = num_str[0:-1]
        if num_str[-1] == ".":
            return num_str[0:-1]
        else: return num_str
