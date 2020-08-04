from copy import copy, deepcopy
from collections import Counter
from sortedcontainers import SortedList
from __init__ import *

class Sudoku:
    def __init__(self, sudokuList, advancedInit=True):
        self.sudokuList = sudokuList
        self.canFill = [[False] * 9 for _ in range(9)]
        self.toFillCount = 0
        self.numberChangeCount = 0
        self.backtrackCount = 0
        self.candidates = [[SortedList(range(1,10)) for i in range(9)] for j in range(9)]
        self.candidatesSupport = [[[0b111] * 10 for i in range(9)] for j in range(9)]
        
        if advancedInit:
            if not self.isLegalGame():
                raise Exception('Invalid input grid')
            for i, r in enumerate(sudokuList):
                for j, c in enumerate(r):
                    if c == 0:
                        self.canFill[i][j] = True
                        self.toFillCount += 1
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
            self.candidatesSupport[i][c][val] &= 0b110
        for j in range(9):
            if j == c: continue
            if val in self.candidates[r][j]:
                self.candidates[r][j].remove(val)
            self.candidatesSupport[r][j][val] &= 0b101

        #Square
        a, b = (r//3) * 3, (c//3) * 3
        for i in range(3):
            for j in range(3):
                if a+i==r and b+j==c: continue
                if val in self.candidates[a + i][b + j]:
                    self.candidates[a + i][b + j].remove(val) 
                self.candidatesSupport[a + i][b + j][val] &= 0b011
    
    def unsiege(self, r, c, val):
        if val == 0: return
        # line
        for i in range(9):
            if i == r: continue
            self.candidatesSupport[i][c][val] |= 0b001
            if self.candidatesSupport[i][c][val] == 0b111:
                self.candidates[i][c].add(val)
        for j in range(9):
            if j == c: continue
            self.candidatesSupport[r][j][val] |= 0b010
            if self.candidatesSupport[r][j][val] == 0b111:
                self.candidates[r][j].add(val)

        #Square
        a, b = (r//3) * 3, (c//3) * 3
        for i in range(3):
            for j in range(3):
                if a+i==r and b+j==c: continue
                self.candidatesSupport[a + i][b + j][val] |= 0b100
                if self.candidatesSupport[a + i][b + j][val] == 0b111:
                    self.candidates[a + i][b + j].add(val) 
    
    def __repr__(self):
        return '\n'.join([' '.join(list(map(str,line))) for line in self.sudokuList])
    
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
            if not self.noDuplicate(row) or not self.noDuplicate(column) or not self.noDuplicate(square):
                return False
        return True
        
    def noDuplicate(self,li):
        c = Counter(li)
        c.pop(0, None)
        return len(c) == 0 or max(list(c.values())) < 2
    
    def changeNumber(self, row, column, toChange):
        """Fill in number at given position. No changes made for unsuccessful fillin.

        Args:
            row (int): Value of [0, 8]
            column (int): Value of [0, 8]
            number (int): Value of [0, 9]

        Returns:
            int: 0 for successfullin; -1 for wrong position; 1 for illegal game
        """        

        if not self.canFill[row][column]:
            return -1
        
        prev = self.sudokuList[row][column]
        if toChange == prev: return 0
        
        self.numberChangeCount += 1
        self.sudokuList[row][column] = toChange
        if self.isLegalChange(row, column):
            self.siege(row, column, toChange)
            self.unsiege(row, column, prev)
            if prev == 0:
                self.toFillCount -= 1
            if toChange == 0:
                self.toFillCount += 1
            return 0
        else:
            self.sudokuList[row][column] = prev
            return 1