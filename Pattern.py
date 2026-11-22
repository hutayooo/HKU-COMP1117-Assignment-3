def count_filled(level):
    # Returns the number of filled cells in a carpet of the given level. Does not use a grid.
    if level == 0:
        return 1
    return 8 * count_filled(level - 1) # Each level adds 8 times the previous. Same thing as 8 ** level


def fill_carpet(grid, top, left, size):
    if size == 1:
        # Base case: a 1x1 cell becomes filled with '#'
        grid[top][left] = "#"
        return # Stop recursing
    sub = size//3
    
    for r in range(3):
        for c in range(3): # Loops through the 3x3 grid of sub-squares
            if r == 1 and c == 1:
                # The center square is skipped
                continue
            sub_top = top + r * sub  # Top row of the sub-square
            sub_left = left + c * sub  # Left column of the sub-square
            fill_carpet(grid, sub_top, sub_left, sub) # Recurse


def find_quadrant(top, left, size, row, col):
    half = size // 2  # Splits the region along row and col
    in_bottom = row >= top + half  # True if row is in the lower half
    in_right = col >= left + half  # True if col is in the right half
    
    if not in_bottom and not in_right:  # Top-left quadrant
        return 0
    if not in_bottom and in_right:  # Top-right quadrant
        return 1
    if in_bottom and not in_right:  # Bottom-left quadrant
        return 2
    return 3  # Bottom-right quadrant


def fill_tromino(grid, top, left, size, hole_row, hole_col, tile):
    # Tiles the square region with upper-left corner (top, left) and side size,
    # whose blocked cell is (hole_row, hole_col), numbering trominoes from tile.
    # Returns the next unused tile number.
    pass  # your code here


def print_grid(grid):
    # Print each row on its own line without changing grid
    for row in grid:
        line = "" # One output line per row
        for cell in row:
            line = line + "{:>3}".format(cell) # Append and format each cell using the supplied width-3 format
        print(line)


def main():
    # main() is yours to write, by working it out with the AI assistant.
    # Some things it will need to do:
    #   - read the pattern and the level, and for a tromino the hole position
    #   - build a starting grid of the right size, filled with the right starting value
    #   - call fill_carpet or fill_tromino once, on the whole grid
    #   - print the grid with print_grid
    #   - print the summary line: for a carpet use count_filled, for a tiling
    #     use the value fill_tromino returns
    pass


main()  # Don't change this
