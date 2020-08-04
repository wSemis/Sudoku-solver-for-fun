from readInput import *
from solver import Solver
from __init__ import *

sudokuList = readFromTxt('sample3.txt')
solver = Solver(sudokuList)
solver.solve({'method':'bruteForce'})