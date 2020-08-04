from Sudoku import Sudoku
from __init__ import *

class Solver:
    def __init__(self, sudokuList):
        self.puzzle = Sudoku(sudokuList)
        
    def solve(self, params):
        if params['method'] == 'bruteForce':
            result = self.smartBruteForce(0) and self.puzzle.isLegalGame()
            print('Success:',result)
            print(f'Number change count: {self.puzzle.numberChangeCount}')
            print(f'Backtrack count: {self.puzzle.backtrackCount}')
            
        if 'print' not in params or params['print']:
            if result:
                print(self.puzzle)
            
    def smartBruteForce(self, num):
        if num >= 81 or self.puzzle.isComplete():
            return True
        i, j = num //9, num % 9
        
        if self.puzzle.canFill[i][j]:
            candidates = self.puzzle.candidates[i][j]
            if DEBUG: print(f'{(i,j)} candidates: {candidates}')
            for _, val in enumerate(candidates):
                if DEBUG: print(f'    {(i,j)} --- {val}  -- {_}th in {candidates}')
                result = self.puzzle.changeNumber(i, j, val)
                assert result == 0, 'Candidate system buggy'
                if self.smartBruteForce(num + 1):
                    return True
                    
            result = self.puzzle.changeNumber(i, j, 0)
            self.puzzle.backtrackCount += 1
            if DEBUG: print('backtrack\n')
            assert result == 0, 'Failed to backtrack'
            return False
        else:
            return self.smartBruteForce(num + 1)