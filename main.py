# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from nltk.sem import Expression
from nltk.test.inference_fixt import setup_module

from nltk import *

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    read_expr = Expression.fromstring
    p1 = read_expr('man(socrates)')
    p2 = read_expr('all x.(man(x) -> mortal(x))')
    c = read_expr('mortal(socrates)')
    print (Prover9().prove(c, [p1, p2]))
    prover = ResolutionProverCommand(c, [p1,p2])
    prover.proof()
    print(prover.proof())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
