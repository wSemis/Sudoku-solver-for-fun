from sys import argv
from time import time

from __init__ import *
from solver import Solver
from readInput import *

def main(sudokuList):
    st = time()
    solver = Solver(sudokuList)
    solver.solve({'method':'bruteForce'})
    print(f'\nRuntime: {time() - st}')
    
if len(argv) == 1:
    sudokuList = readFromTxt('sample3.txt')
elif len(argv) == 2:
    sudokuList = readFromTxt(argv[1])

main(sudokuList)
    
