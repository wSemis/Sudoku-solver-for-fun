from Sudoku import Sudoku

class Solver:
    def __init__(self, sudokuList):
        self.puzzle = Sudoku(sudokuList)
        
    def solve(self, params):
        if params['method'] == 'bruteForce':
            print('Success:',self.bruteForce(0))
            
        if 'print' not in params or params['print']:
            print(self.puzzle)
            
    def bruteForce(self, num):
        if num >= 81 or self.puzzle.isComplete():
            return True
        i, j = num //9, num % 9
        
        if self.puzzle.canFill[i][j]:
            vals = self.puzzle.candidates[i][j]
            for val in vals:
                print('num',num,'\nval',val,)
                prev = self.puzzle.sudokuList[i][j]
                result = self.puzzle.changeNumber(i, j, val)
                if result == 0:
                    if self.bruteForce(num + 1):
                        return True
                    else:
                        result = self.puzzle.changeNumber(i, j, prev)
                        assert result == 0, 'Failed to backtrack'
            
            return False
        else:
            return self.bruteForce(num + 1)