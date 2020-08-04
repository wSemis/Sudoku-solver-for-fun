'''
Regulates passing format for this sudoku solver

Pass in: 9 lines of cell numbers without space; empty cells filled with 0s
return __sudokuList[row][col]__ = integer
'''

import sys
from __init__ import *

def readLine(line):
    
    return list(map(int, list(line.replace(' ','').strip())))

def readFromTxt(fn):
    with open(fn, 'r') as f:
        lines = f.readlines()
    
    sudokuList = []
    for line in lines:
        if line.strip() == '':
            pass
        else:
            l = readLine(line)
            sudokuList.append(l)
            
    assert len(sudokuList) == 9, f'Corrupted file with line number of {len(sudokuList)}'
    return sudokuList

def readFromConsole():
    sudokuList = []
    
    complete_inout = sys.stdin.read()
    
    for line in complete_inout:
        if line.strip() == '':
            pass
        elif line.strip() == 'del':
            sudokuList.pop(-1)
        elif line.strip() == 'clear':
            sudokuList = []
        
        else:
            l = readLine(line)
            sudokuList.append(l)

    assert len(sudokuList) == 9, f'Corrupted file with line number of {len(sudokuList)}'
    return sudokuList