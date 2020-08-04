# Incrimental built of sudoku solver(s)

This is a leisure project for me to explore some techniques used in this classic game and also to review some programming techniques to keep my code quality up. The solver mentioned in the usage manual is correctly implemented.

## Usage mannual

To use the program, simply type

    python3 main.py [sudoku puzzle file name]

The puzzle file shall

* Only contains one puzzle
* Only contains __numbers__
* __Empty cells__ shall be denoted by __0__
* Each newline corresponds a line in the puzzle
* Spaces and empty lines are tolerated

## Solver introductions

### __Smart Brute Force Solver__

This is a solver that will be the base of future more complicated solver, as well as a validation tool.

Highlights of the solver

* Use bitwise operations to track the eligibility of cell candidate numbers. Thus, backtracking will not require copying the entire puzzle grid
* OOP and clean code style

## Disclaimer

* Thanks for _[SudokuWiki](https://www.sudokuwiki.org/)_'s inspirations and provision of puzzle examples.