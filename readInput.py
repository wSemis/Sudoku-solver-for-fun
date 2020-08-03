'''
Regulates passing format for this sudoku solver

Use nested lists as input
__sudokuList[row][col]__
'''

import sys

def readFromTxt(fn):
    with open(fn, 'r') as f:
        lines = f.readlines()
    
    sudokuList = []
    for line in lines:
        if line.strip() == '':
            pass
        else:
            l = list(map(int, list(line.strip())))
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
            l = list(map(int, list(line.strip())))
            sudokuList.append(l)

    assert len(sudokuList) == 9, f'Corrupted file with line number of {len(sudokuList)}'
    return sudokuList