from readInput import *
from solver import Solver

sudokuList = readFromTxt('sample1.txt')
solver = Solver(sudokuList)
solver.solve({'method':'bruteForce'})