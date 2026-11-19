# A3 Recursive Patterns: My Specifications

**Finish this file first, before any code is written.** You supply the
reasoning and fill in this worksheet in your own words, with the AI
assistant's help.

## Input and output types

- **Inputs:** 
- All inputs are read as whole numbers, or int, in main, as all inputs are whole numbers and there are no decimals to take into account for 
- Pattern: int, 1 for sierpinski, 2 for L-tromino
- In the case of carpet (pattern == 1), it reads level, which is an integer from 0-3
- In the case of tiling (pattern == 2), it reads level as an integer from 0-4, followed by hole_row and hole_col. Both of which are integers ranging from 0 to side-1. side = 2^level

- **Outputs:**
- After drawing, it prints the grid row by row from top to bottom, one line per row
- Then, prints a summary. For carpet, it is "Filled: <int>". For tiling, it is "Tiles: <int>"
- A level k carpet has side length 3^k. Hence, it'll print 3^k + 1 lines (+1 because of the 1 summary line)
- A level k tiling has side length 2^k. Hence, it'll print 2^k + 1 lines (+1 because of the 1 summary line)

- **The grid:**
- A grid is a list of rows, and each row is a list of cells. Represented by grid[row][col] with 0,0 being top left
- For carpet, the grid is of size 3^level x 3^level, and the list will store strings. Initially, every cell is initialized with "." (str). During the filling process, the filled cells will become "#", while unfilled ones will remain as ".". Then prints the grid and summary as intended
- For tiling, the grid is os length 2^level x 2^level, and the list will store both a string and integers. Initially, every cell is set to 0 (int), then the specified cell will be set to 'X' (str). The placed tiles then become numbers (int, starting from 1) while "X" stays as X. There should be no 0 left after the filling 

## The rules for each function in my own words

State each rule in your own words, not the assignment's wording pasted back.
For every boundary, write **both sides**: what happens exactly on it, and
what happens just past it. For each recursive function, say what its base
case is and why every recursive call gets closer to it.

### count_filled(level)

- **What it receives and what it returns:**
- It takes level, as an int from 0-3 and returns the total number of filled in that level carpet without building a grid
- **Base case:** 
- The smallest case is a level 0 carpet of side 1. That cell is filled, so it returns the count as 1
- **Recursive case:**
- For level > 0, splitting a 3x3 grid leaves the center sub-square empty. However, it leaves 8 sub-squares each of side 3^level-1, which is a level-1 carpet. Therefore, the total filled count is 8 * count_filled(level - 1) (each call reduces level by 1, so it always reaches 0)
- Check:
Level 1 = 8x1 = 8 filled
Level 2 (Example 1)= 8x8 = 64 filled
Level 3 (Example 2)= 8x64 = 512 filled

### fill_carpet(grid, top, left, size)

- **What it receives, and what it changes in the grid:**
- it receives grid, which is the 2d list
- top and left (the row and column of the region's upper-left corner)
- size (the side length of the square region)

- **Base case:** which size, and what happens to the grid?
- **Recursive case:** the nine smaller squares. What is each one's side, and
  where is each one's upper-left corner, counted from (top, left)? Which
  square is skipped, and what is left in its cells?
- **Offsets:** for a region that does not start at (0, 0), give one example
  of the smaller squares' corners.

### find_quadrant(top, left, size, row, col)

- **What it receives and what it returns:**
- **Rows:** which rows of the region are in the top half and which are in
  the bottom half? Give the last row of the top half and the first row of
  the bottom half.
- **Columns:** the same for the left and right halves.
- **Offsets:** give one example with a region that does not start at (0, 0),
  on both sides of a boundary.

### fill_tromino(grid, top, left, size, hole_row, hole_col, tile)

- **What it receives, what it changes in the grid and what it returns:**
  which cells may it change, and which must it leave alone?
- **Base case:** which size, what is placed, and what is returned?
- **The center cells:** for a region starting at (top, left), which four
  cells are they? Which quadrant is each one in?
- **The center tromino:** which three center cells does it cover, and which
  number does it get?
- **Each quadrant's blocked cell:** for the quadrant that holds the region's
  blocked cell, and for the other three.
- **The numbering:** the order the quadrants are tiled in, which number each
  quadrant starts from, and what the whole call returns. Check your rule
  against your trace of Example 3.

### print_grid(grid)

- **What it receives, what it prints and what it returns:** how many lines,
  how many characters per cell, and what does it leave unchanged?

### main()

- **What it does, in order:** reading input, building the starting grid,
  drawing, printing.
- **The summary line:** what is counted for each pattern, and where does the
  number come from? Why is the number of tiles one less than the value the
  first call of `fill_tromino` returns?

## Edge cases

The inputs where something special happens, and what the program must do in
each. For example: level 0 of each pattern, a hole on one of the four center
cells, a hole on the edge of the board, or a region in a recursive call that
does not start at (0, 0).