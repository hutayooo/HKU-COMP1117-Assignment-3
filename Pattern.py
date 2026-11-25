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
    if size == 1: # Base case: a 1x1 region has only the blocked cell, so place nothing and return tile
        return tile # Next unsued tile number is the same
    
    half = size//2 # Split the region into quadrants
    hole_quad = find_quadrant(top, left, size, hole_row, hole_col) # Quadrant holding the hole
    
    center_cells = [
        (top + half - 1, left + half - 1),  # Quadrant 0
        (top + half - 1, left + half),  # Quadrant 1
        (top + half, left + half - 1),  # Quadrant 2
        (top + half, left + half),  # Quadrant 3
    ]
    
    for q in range(4):
        if q != hole_quad: # Skip quadrant with a blocked cell
            cell = center_cells[q] # Tuple (cr, cc)
            cr = cell[0] # Center row
            cc = cell[1] # Center column 
            grid[cr][cc] = tile # Fill the center cell with the current tile number
    next_tile = tile + 1 # Increment the tile number for the next use
    
    sub_origins = [ # Upper-left corners for each quadrant
        (top, left),  # Quadrant 0
        (top, left + half),  # Quadrant 1
        (top + half, left),  # Quadrant 2
        (top + half, left + half),  # Quadrant 3
    ]
    
    for q in range(4):
        origin = sub_origins[q] # Tuple (sub_top, sub_left)
        sub_top = origin[0] # Top row
        sub_left = origin[1] # Left col
        
        if q == hole_quad: # Quadrant with the blocked cell
            b_row = hole_row    
            b_col = hole_col
            
        else: #Other three quadrants use their newly filled center cell as blocked
            blocked = center_cells[q] # Tuple (cr, cc)
            b_row = blocked[0] # Blocked row
            b_col = blocked[1] # Blocked col
        
        # Pass next_tile in and update it with the next unused tile ID returned
        next_tile = fill_tromino(grid, sub_top, sub_left, half, b_row, b_col, next_tile)
        
    return next_tile


def print_grid(grid):
    # Print each row on its own line without changing grid
    for row in grid:
        line = "" # One output line per row
        for cell in row:
            line = line + "{:>3}".format(cell) # Append and format each cell using the supplied width-3 format
        print(line)


def main():
    # Input
    pattern = int(input("Pattern (1 carpet, 2 tromino): "))
    level = int(input("Level: "))
    
    hole_row = 0
    hole_col = 0 # Default
    if pattern == 2: # For tromino, read the hole coordinates
        hole_row = int(input("Hole row: "))
        hole_col = int(input("Hole column: "))

    if pattern == 1: # Carpet
        size = 3 ** level # Size of the grid
        grid = []
        for r  in range(size): # Fill each cell with '.'
            row = [] 
            for c in range(size):
                row.append(".") # Fill with empty cells
            grid.append(row) # Once each row is filled, append it to the grid   
        
        fill_carpet(grid, 0, 0, size) # Fill the carpet pattern starting from 0,0
        
        # Print grid and summary
        print_grid(grid)
        filled_count = count_filled(level) # Count filled cells without using the grid
        print (f"Filled: {filled_count}") # Summary line, number of filled cells
    
    elif pattern == 2: # Tromino
        size = 2 ** level # Size of the grid
        grid = []
        for r in range(size): # Fill each cell with 0
            row = [] 
            for c in range(size):
                row.append(0) # Fill with empty cells (int 0)
            grid.append(row) # Once each row is filled, append it to the grid
        
        grid[hole_row][hole_col] = "X" # Mark the blocked cell with "X"
        
        val = fill_tromino(grid, 0, 0, size, hole_row, hole_col, 1) # Tile board from tile 1
        
        # Print grid and summary
        print_grid(grid)
        tiles_placed = val - 1 # Number of tiles placed is one less than returned value
        print (f"Tiles: {tiles_placed}") # Summary line, number of tiles placed
        
        

main()  # Don't change this
