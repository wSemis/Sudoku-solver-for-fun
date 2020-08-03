from copy import copy, deepcopy
from collections import Counter

class Sudoku:
    def __init__(self, sudokuList, advancedInit=True):
        self.sudokuList = sudokuList
        self.canFill = [[False] * 9 for _ in range(9)]
        self.toFillCount = 0
        self.candidates = [[[list(range(1,10))] for i in range(9)] for i in range(9)]
        self.candidatesSupport = [[[7] * 9 for i in range(9)] for j in range(9)]
        
        if advancedInit:
            if not self.isLegalGame():
                raise Exception('Invalid input grid')
            for i, r in enumerate(sudokuList):
                for j, c in enumerate(r):
                    if c == 0:
                        self.canFill[i][j] = True
                        self.toFill += 1
                    if c < 0 or c > 9:
                        raise Exception(f'Wrong Format, got {c}')
    
            for i, r in enumerate(sudokuList):
                for j, c in enumerate(r):
                    self.siege(i, j, c)
                
    def siege(self, r, c, val):
        if val == 0: return
        # line
        for i in range(9):
            if i == r: continue
            if val in self.candidates[i][c]:
                self.candidates[i][c].remove(val)
            self.candidatesSupport[i][c] &= 0 + 2 + 4
        for j in range(9):
            if j == c: continue
            if val in self.candidates[r][j]:
                self.candidates[r][j].remove(val)
            self.candidatesSupport[r][j] &= 1 + 0 + 4

        #Square
        a, b = (r//3) * 3, (c//3) * 3
        for i in range(3):
            for j in range(3):
                if a+i==r and b+j==c: continue
                if val in self.candidates[a + i][b + j]:
                    self.candidates[a + i][b + j].remove(val) 
                self.candidatesSupport[a + i][b + j] &= 1 + 2 + 0
    
    def unsiege(self, r, c, val):
        if val == 0: return
        # line
        for i in range(9):
            if i == r: continue
            self.candidatesSupport[i][c] |= 1
            if self.candidatesSupport[i][c] == 7:
                self.candidates[i][c].append(val)
        for j in range(9):
            if j == c: continue
            self.candidatesSupport[r][j] |= 2
            if self.candidatesSupport[r][j] == 7:
                self.candidates[r][j].append(val)

        #Square
        a, b = (r//3) * 3, (c//3) * 3
        for i in range(3):
            for j in range(3):
                if a+i==r and b+j==c: continue
                self.candidatesSupport[a + i][b + j] |= 4
                if self.candidatesSupport[a + i][b + j] == 7:
                    self.candidates[a + i][b + j].append(val) 
    
    def __repr__(self):
        return '\n'.join([' '.join(line) for line in self.sudokuList])
    
    def __copy__(self):
        new = Sudoku(deepcopy(self.sudokuList))
        return new
            
    def __deepcopy__(self):
        new = Sudoku(deepcopy(self.sudokuList), advancedInit=False)
        new.canFill = deepcopy(self.canFill)
        new.candidates = deepcopy(self.candidates)
        new.candidatesSupport = deepcopy(self.candidatesSupport)
        new.toFillCount = self.toFillCount
        return new
    
    def getRow(self, r): return self.sudokuList[r]
    
    def getColumn(self, c): return [line[c] for line in self.sudokuList]
    
    def getSquare(self, r, c):
        a, b = 3 * r, 3 * c    
        square = []
        for i in range(3):
                for j in range(3):
                    square.append(self.sudokuList[a+i][b+j])
        return square    
                
    def isComplete(self):
        return self.toFillCount == 0
    
    def isLegalChange(self, r, c):
        row = self.getRow(r)
        column = self.getColumn(c)
        square = self.getSquare(r//3, c//3)
        return self.noDuplicate(row) and self.noDuplicate(column) and self.noDuplicate(square)
    
    def isLegalGame(self):
        # lines
        for i in range(9):
            row = self.getRow(i)
            column = self.getColumn(i)
            square = self.getSquare(i//3, i%3)
            if not self.noDuplicate(row) or not self.noDuplicate(column) or not self.noDuplicate(sqaure):
                return False
        return True
        
    def noDuplicate(self,li):
        c = Counter(li)
        c.pop(0, None)
        return max(c.values()) < 2
    
    def changeNumber(self, row, column, number):
        """Fill in number at given position. No changes made for unsuccessful fillin.

        Args:
            row (int): Value of [0, 8]
            column (int): Value of [0, 8]
            number (int): Value of [1, 9]

        Returns:
            int: 0 for successfullin; -1 for wrong position; 1 for illegal game
        """        

        if not self.canFill[row][column]:
            return -1
        
        prev = self.sudokuList[row][column]
        self.sudokuList[row][column] = number
        if self.isLegalChange(row, column):
            self.unsiege(prev)
            self.siege(val)
            if prev == 0:
                self.toFillCount -= 1
            return 0
        else:
            self.sudokuList[row][column] = prev
            return 1