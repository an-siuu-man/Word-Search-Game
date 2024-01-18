import random as rand
from chatgpt import get_words_for_grid
alphabets = ['A', 'B', 'C', 'D', 'E', 
             'F', 'G', 'H', 'I', 'J', 
             'K', 'L', 'M', 'N', 'O', 
             'P', 'Q', 'R', 'S', 'T', 
             'U', 'V', 'W', 'X', 'Y', 'Z']
orientation = ['ttd', 'dtt', 'diag', 'rdiag', 'ltor', 'rtol']

grid = []
grid_size = 14
placement = []
for i in range(grid_size):
    grid.append([])
for i in range(grid_size):
    for i in range(grid_size):
        grid[i].append( rand.choice(alphabets) + 'a')
visited_grid = []
printed_words = []
def place_word(word, row, col, direction):
    global grid
    global visited_grid

    ROW = row      
    COL = col
    placement_detector = 0
    counter = 0
    overlap_locations = []
    overlap_coordinates = {}
    
    if direction == 'ttd':
        for k in word:
            if '.' not in grid[ROW][COL]:
                grid[ROW][COL] = k + '.'
                placement_detector += 1
            else:
                if grid[ROW][COL] != k + '.':
                    counter += 1
                    overlap_locations.append(ROW)
                if grid[ROW][COL] == k + '.':
                    overlap_locations.append(ROW)       
            ROW += 1

        if counter == 0:
            visited_grid.append([row, col])
            placement.append(True)
            printed_words.append(word)
            return True

        if placement_detector == len(word):
            for i in range(row, ROW):
                grid[i][col] = rand.choice(alphabets) + 'a'
            visited_grid.append([row, col])
            return True

        for i in range(ROW-1, row-1, -1):
            if i not in overlap_locations:
                grid[i][COL] = rand.choice(alphabets) + 'a'
         
        visited_grid.append([row, col])
        if check_word_limits(word, row, col-1, 'ttd') and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, 'ttd')
            if valid_pos:
                 
                return True
        if check_word_limits(word, row-1, col, 'ttd') and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, 'ttd')
            if valid_pos:
                 
                return True
        if check_word_limits(word, row, col+1, 'ttd') and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, 'ttd')
            if valid_pos:
                 
                return True
        if check_word_limits(word, row+1, col, 'ttd') and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, 'ttd')
            if valid_pos:
                 
                return True
        orient = []
        for i in orientation:
            if i != 'ttd':
                orient.append(i)
        dir = rand.choice(orient)
        if check_word_limits(word, row, col-1, dir) and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row-1, col, dir) and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row, col+1, dir) and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row+1, col, dir) and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, dir)
            if valid_pos:
                 
                return True
        orient.remove(dir)
        dir = rand.choice(orient)
        if check_word_limits(word, row, col-1, dir) and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row-1, col, dir) and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row, col+1, dir) and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row+1, col, dir) and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, dir)
            if valid_pos:
                 
                return True
        orient.remove(dir)
        dir = rand.choice(orient)
        if check_word_limits(word, row, col-1, dir) and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row-1, col, dir) and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row, col+1, dir) and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row+1, col, dir) and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, dir)
            if valid_pos:
                 
                return True
         
        
    if direction == 'dtt':
        for k in word:
            if '.' not in grid[ROW][COL]:
                grid[ROW][COL] = k + '.'
                placement_detector += 1
            else:
                if grid[ROW][COL] != k + '.':
                    counter += 1
                    overlap_locations.append(ROW)
                if grid[ROW][COL] == k + '.':
                    overlap_locations.append(ROW)
            ROW -= 1
        if counter == 0:
            visited_grid.append([row, col])
            placement.append(True)
            printed_words.append(word)
            return True
        if placement_detector == len(word):
            for i in range(ROW+1,row+1):
                grid[i][col] = rand.choice(alphabets) + 'a'
            visited_grid.append([row, col])
            return True
        for i in range(ROW+1, row+1):
            if i not in overlap_locations:         
                grid[i][COL] =  rand.choice(alphabets) + 'a'
                
        visited_grid.append([row, col])
         
        if check_word_limits(word, row, col-1, 'ttd') and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, 'ttd')
            if valid_pos:
                 
                return True
        if check_word_limits(word, row-1, col, 'ttd') and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, 'ttd')
            if valid_pos:
                 
                return True
        if check_word_limits(word, row, col+1, 'ttd') and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, 'ttd')
            if valid_pos:
                 
                return True
        if check_word_limits(word, row+1, col, 'ttd') and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, 'ttd')
            if valid_pos:
                 
                return True
        orient = []
        for i in orientation:
            if i != 'dtt':
                orient.append(i)
        dir = rand.choice(orient)
        if check_word_limits(word, row, col-1, dir) and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row-1, col, dir) and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row, col+1, dir) and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row+1, col, dir) and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, dir)
            if valid_pos:
                 
                return True
        orient.remove(dir)
        dir = rand.choice(orient)
        if check_word_limits(word, row, col-1, dir) and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row-1, col, dir) and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row, col+1, dir) and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row+1, col, dir) and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, dir)
            if valid_pos:
                 
                return True
        orient.remove(dir)
        dir = rand.choice(orient)
        if check_word_limits(word, row, col-1, dir) and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row-1, col, dir) and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row, col+1, dir) and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row+1, col, dir) and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, dir)
            if valid_pos:
                 
                return True
         
    if direction == 'diag':
        for k in word:
            if '.' not in grid[ROW][COL]:
                grid[ROW][COL] = k + '.'
                placement_detector += 1
            else:
                if grid[ROW][COL] != k + '.':
                    counter += 1
                    overlap_coordinates[ROW] = COL
                if grid[ROW][COL] == k + '.':
                    overlap_coordinates[ROW] = COL
            ROW += 1
            COL += 1
        if counter == 0:
            visited_grid.append([row, col])
            placement.append(True)
            printed_words.append(word)
            return True
        if placement_detector == len(word):
            for i in range(row, ROW):
                grid[i][overlap_coordinates[i]] = rand.choice(alphabets) + 'a'
            visited_grid.append([row, col])
            return True
        
        for i in range(ROW-1, row-1, -1):
            if i not in overlap_coordinates.keys():         
                grid[i][COL-1] =  rand.choice(alphabets) + 'a'
            COL -= 1

        visited_grid.append([row, col])
         
        if check_word_limits(word, row, col-1, 'diag') and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, 'diag')
            if valid_pos:
                return True
        if check_word_limits(word, row-1, col, 'diag') and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, 'diag')
            if valid_pos: 
                return True
        if check_word_limits(word, row, col+1, 'diag') and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, 'diag')
            if valid_pos:
                 
                return True
        if check_word_limits(word, row+1, col, 'diag') and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, 'diag')
            if valid_pos:
                 
                return True
        orient = []
        for i in orientation:
            if i != 'diag':
                orient.append(i)
        dir = rand.choice(orient)
        if check_word_limits(word, row, col-1, dir) and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row-1, col, dir) and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row, col+1, dir) and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row+1, col, dir) and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, dir)
            if valid_pos:
                 
                return True
        orient.remove(dir)
        dir = rand.choice(orient)
        if check_word_limits(word, row, col-1, dir) and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row-1, col, dir) and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row, col+1, dir) and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row+1, col, dir) and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, dir)
            if valid_pos:
                 
                return True
        orient.remove(dir)
        dir = rand.choice(orient)
        if check_word_limits(word, row, col-1, dir) and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row-1, col, dir) and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row, col+1, dir) and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, dir)
            if valid_pos:
                 
                return True
        if check_word_limits(word, row+1, col, dir) and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, dir)
            if valid_pos:
                 
                return True
         
    if direction == 'rdiag':
        for k in word:
            if '.' not in grid[ROW][COL]:
                grid[ROW][COL] = k + '.'
                placement_detector += 1
            else:
                if grid[ROW][COL] != k + '.':
                    counter += 1
                    overlap_coordinates[ROW] = COL
                if grid[ROW][COL] == k + '.':
                    overlap_coordinates[ROW] = COL
            COL -=1 
            ROW += 1
        if counter == 0:
            visited_grid.append([row, col])
            placement.append(True)
            printed_words.append(word)
            return True

        if placement_detector == len(word):
            for i in range(row, ROW):
                grid[i][overlap_coordinates[i]] = rand.choice(alphabets) + 'a'
            visited_grid.append([row, col])
            return True
        
        for i in range(ROW-1,row-1,-1):
                if i not in overlap_coordinates.keys():
                    grid[i][COL+1] =  rand.choice(alphabets) + 'a'
                COL += 1
        
        visited_grid.append([row, col])
         
        if check_word_limits(word, row, col-1, 'rdiag') and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, 'rdiag')
            if valid_pos:
                 
                return True
        if check_word_limits(word, row-1, col, 'rdiag') and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, 'rdiag')
            if valid_pos:
                 
                return True
        if check_word_limits(word, row, col+1, 'rdiag') and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, 'rdiag')
            if valid_pos:
                 
                return True
        if check_word_limits(word, row+1, col, 'rdiag') and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, 'rdiag')
            if valid_pos:
                return True
        orient = []
        for i in orientation:
            if i != 'rdiag':
                orient.append(i)
        dir = rand.choice(orient)
        if check_word_limits(word, row, col-1, dir) and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row-1, col, dir) and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row, col+1, dir) and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row+1, col, dir) and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, dir)
            if valid_pos:
                return True
        orient.remove(dir)
        dir = rand.choice(orient)
        if check_word_limits(word, row, col-1, dir) and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row-1, col, dir) and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row, col+1, dir) and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row+1, col, dir) and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, dir)
            if valid_pos:
                return True
        orient.remove(dir)
        dir = rand.choice(orient)
        if check_word_limits(word, row, col-1, dir) and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row-1, col, dir) and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row, col+1, dir) and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row+1, col, dir) and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, dir)
            if valid_pos:
                return True
         
    if direction == 'ltor':
        for k in word:
            if '.' not in grid[ROW][COL]:
                grid[ROW][COL] = k + '.'
                placement_detector += 1
            else:
                if grid[ROW][COL] != k + '.':
                    counter += 1
                    overlap_locations.append(COL)
                if grid[ROW][COL] == k + '.':
                    overlap_locations.append(COL)
            COL += 1
        if counter == 0:
            visited_grid.append([row, col])
            placement.append(True)
            printed_words.append(word)
            return True
        
        if placement_detector == len(word):
            for i in range(col,COL):
                grid[row][i] = rand.choice(alphabets) + 'a'
            visited_grid.append([row, col])
            return True
        
        for i in range(col, COL):
            if i not in overlap_locations:         
                grid[ROW][i] =  rand.choice(alphabets) + 'a'

        visited_grid.append([row, col])
         
        if check_word_limits(word, row, col-1, 'ltor') and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, 'ltor')
            if valid_pos:
                return True
        if check_word_limits(word, row-1, col, 'ltor') and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, 'ltor')
            if valid_pos:
                return True
        if check_word_limits(word, row, col+1, 'ltor') and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, 'ltor')
            if valid_pos:
                return True
        if check_word_limits(word, row+1, col, 'ltor') and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, 'ltor')
            if valid_pos:
                return True
        orient = []
        for i in orientation:
            if i != 'ltor':
                orient.append(i)
        dir = rand.choice(orient)
        if check_word_limits(word, row, col-1, dir) and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row-1, col, dir) and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row, col+1, dir) and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row+1, col, dir) and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, dir)
            if valid_pos:
                return True
        orient.remove(dir)
        dir = rand.choice(orient)
        if check_word_limits(word, row, col-1, dir) and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row-1, col, dir) and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row, col+1, dir) and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row+1, col, dir) and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, dir)
            if valid_pos:
                return True
        orient.remove(dir)
        dir = rand.choice(orient)
        if check_word_limits(word, row, col-1, dir) and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row-1, col, dir) and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row, col+1, dir) and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row+1, col, dir) and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, dir)
            if valid_pos:
                return True
         
    if direction == 'rtol':
        for k in word:
            if '.' not in grid[ROW][COL]:
                grid[ROW][COL] = k + '.'
                placement_detector += 1
            else:
                if grid[ROW][COL] != k + '.':
                    counter += 1
                    overlap_locations.append(COL)
                if grid[ROW][COL] == k + '.':
                    overlap_locations.append(COL)
            COL -= 1
        if counter == 0:
            visited_grid.append([row, col])
            placement.append(True)
            printed_words.append(word)
            return True
        if placement_detector == len(word):
            for i in range(COL+1,col+1):
                grid[row][i] = rand.choice(alphabets) + 'a'
            visited_grid.append([row, col])
            return True
        
        for i in range(COL+1, col+1):
            if i not in overlap_locations:         
                grid[ROW][i] =  rand.choice(alphabets) + 'a'

        visited_grid.append([row, col])
         
        if check_word_limits(word, row, col-1, 'rtol') and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, 'rtol')
            if valid_pos:
                return True
        if check_word_limits(word, row-1, col, 'rtol') and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, 'rtol')
            if valid_pos:
                return True
        if check_word_limits(word, row, col+1, 'rtol') and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, 'rtol')
            if valid_pos:
                return True
        if check_word_limits(word, row+1, col, 'rtol') and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, 'rtol')
            if valid_pos:
                return True
        orient = []
        for i in orientation:
            if i != 'rtol':
                orient.append(i)
        dir = rand.choice(orient)
        if check_word_limits(word, row, col-1, dir) and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row-1, col, dir) and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row, col+1, dir) and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row+1, col, dir) and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, dir)
            if valid_pos:
                return True
        orient.remove(dir)
        dir = rand.choice(orient)
        if check_word_limits(word, row, col-1, dir) and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row-1, col, dir) and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row, col+1, dir) and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row+1, col, dir) and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, dir)
            if valid_pos:
                return True
        orient.remove(dir)
        dir = rand.choice(orient)
        if check_word_limits(word, row, col-1, dir) and [row, col-1] not in visited_grid:
            valid_pos = place_word(word, row, col-1, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row-1, col, dir) and [row-1, col] not in visited_grid:
            valid_pos = place_word(word, row-1, col, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row, col+1, dir) and [row, col+1] not in visited_grid:
            valid_pos = place_word(word, row, col+1, dir)
            if valid_pos:
                return True
        if check_word_limits(word, row+1, col, dir) and [row+1, col] not in visited_grid:
            valid_pos = place_word(word, row+1, col, dir)
            if valid_pos: 
                return True
    return False
####################################################################################################################
def check_word_limits(word, row, col, direction):
    if direction == 'ttd':
        if row + len(word) - 1 > grid_size-1 or row not in range(0,grid_size) or col not in range(0,grid_size):
            return False
        else:
            return True

    if direction == 'dtt':
        if row - len(word) + 1 < 0 or row not in range(0,grid_size) or col not in range(0,grid_size):
            return False
        else:
            return True

    if direction == 'diag':
        if row + len(word) - 1> grid_size-1 or row not in range(0,grid_size) or col + len(word) - 1 > grid_size-1 or col not in range(0,grid_size):
            return False
        else:
            return True

    if direction == 'rdiag':
        if row + len(word) - 1 > grid_size-1 or row not in range(0,grid_size) or col - len(word) + 1 < 0 or col not in range(0,grid_size):
            return False
        else:
            return True

    if direction == 'ltor':
        if col + len(word) - 1 > grid_size-1 or col not in range(0,grid_size) or row not in range(0,grid_size):
            return False
        else:
            return True

    if direction == 'rtol':
        if col - len(word) + 1 < 0 or col not in range(0,grid_size) or row not in range(0,grid_size):
            return False
        else:
            return True

    if direction == 'invdiag':
        if row - len(word) + 1 < 0 or row not in range(0,grid_size) or col - len(word) + 1 < 0 or col not in range(0,grid_size):
            return False
        else:
            return True
####################################################################################################################
def word_limits(word, grid_size, direction):
    if direction == 'ttd':
        return [rand.randint(0,grid_size-len(word)), rand.randint(0,grid_size-1)]
    if direction == 'dtt':
        return [rand.randint(len(word)-1,grid_size-1), rand.randint(0,grid_size-1)]
    if direction == 'diag':
        return [rand.randint(0,grid_size-len(word)),rand.randint(0,grid_size-len(word))]
    if direction == 'rdiag':
        return [rand.randint(0,grid_size-len(word)), rand.randint(len(word)-1,grid_size-1)]
    if direction == 'ltor':
        return [rand.randint(0,grid_size-1),rand.randint(0,grid_size-len(word))]
    if direction == 'rtol':
        return[rand.randint(0,grid_size-1), rand.randint(len(word)-1,grid_size-1)]        
####################################################################################################################
def check_and_place(word, row, col, direction = rand.choice(orientation)):
        
    if check_word_limits(word, row, col, direction):
        place_word(word, row, col, direction)

word_list = get_words_for_grid("italian soccer teams")

for word in word_list:
    direction = rand.choice(orientation)
    k = word_limits(word,grid_size,direction)
    check_and_place(word, k[0], k[1], direction)

print(printed_words)

print(word_list)

for i in grid:
    # for k in range(len(i)):
    #     if '.' in i[k]:
    #         p = i[k]
    #         i[k] = p.replace('.','')
    #     if 'a' in i[k]:
    #         p = i[k]
    #         i[k] = p.replace('a','')
    print('  '.join(i))