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
- It receives grid, which is the 2d list
- Top and left (the row and column of the region's upper-left corner)
- Size (the side length of the square region)
- It may only modify cells inside the square region spanning rows top through top + size - 1 and columns left through left + size - 1, setting filled cells to "#". it must not overwrite empty cells (".") inside the skipped center regions

- **Base case:** which size, and what happens to the grid?
- When size == 1, the region is a single cell at (top, left), so it sets grid[top][left] = "#" directly
- Because size is divided by 3 (size // 3) on every recursive step, size strictly decreases toward 1

- **Recursive case:**
- For size > 1, the square is divided 3x3 arrangement of 9 smaller squares. The sides of each square are side//3. 
- For block indices r (row) in 0, 1, 2 and c (column) in 0, 1, 2, each sub-square's upper left corner is (top + r * sub, left + c * sub). We use the upper left square as the "reference point"
- The center sub-square (r == 1 and c == 1) is skipped, leaving its cells as ".", while fill_carpet is called recursively on each of the remaining eight sub-squares

- **Offsets:**
- Lets say for a 9x9 region (size = 9) starting at top = 3, left = 6 (sub = 3), the top-middle sub-square (r = 0, c = 1) has its upper-left corner at (3 + 0 * 3, 6 + 1 * 3) = (3, 9) (and the center sub-square at r = 1, c = 1 is at (6, 9) and skipped)

### find_quadrant(top, left, size, row, col)

- **What it receives and what it returns:**
- It receives top and left, which are the row and column of the square region's upper-left corner
- size, the length of a square region which is always guranteed to be a power of 2
- row and col, the coordinates of a target cell inside that region
- It returns identifiers (quadrant labels or "TL", "TR", "BL", or "BR"), indicating which of the four quadrants contains (row, col)

- **Rows:**
- With half = size // 2, the top half covers rows top through top + half - 1, and the bottom half covers rows top + half through top + size - 1
- The last row of the top half is top + half - 1, and the first row of the bottom half is top + half

- **Columns:** the same for the left and right halves.
- With half = size // 2, the left half covers columns left through left + half - 1, and the right half covers columns left + half through left + size - 1
- The last column of the left half is left + half - 1, and the first column of the right half is left + half

- **Offsets:**
- For a region with top = 4, left = 6, and size = 8 (half = 4), the row boundary is 8 and the column boundary is 10
- row = 7, col = 9 is just above/left of the boundaries and falls in quadrant 0 (top-left)
- While row = 8, col = 10 is just at/below the boundaries and falls in quadrant 3 (bottom-right)

### fill_tromino(grid, top, left, size, hole_row, hole_col, tile)

- **What it receives, what it changes in the grid and what it returns:**
- It receives grid, the 2d list
- top and left, upper-left corner of the region
- size, power-of-2 side length
- hole_row and hole_col, coordinates of the existing blocked/missing cell in this region
- and tile, next integer tromino ID to assign

- It may only write positive integer tile IDs to empty (0) cells inside rows top through top + size - 1 and columns left through left + size - 1
- It must leave the region's existing blocked cell (hole_row, hole_col)
- It must also not touch any already-filled tromino cells inside the region, and all cells outside the region must also be untouched
- Returns the next available tile integer
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