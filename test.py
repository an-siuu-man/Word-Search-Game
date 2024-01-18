import random as rand
from chatgpt import get_words_for_grid
# declaring a list which contains all the letters of the English alphabet

alphabets = ['A', 'B', 'C', 'D', 'E', 
             'F', 'G', 'H', 'I', 'J', 
             'K', 'L', 'M', 'N', 'O', 
             'P', 'Q', 'R', 'S', 'T', 
             'U', 'V', 'W', 'X', 'Y', 'Z']

# declaring all the possible orientations which a word may be printed inside the grid
# ttd: top to down
# dtt: down to top
# diag: diagonal
# rdiag: reverse diagonal
# ltor: left to right
# rtol: right to left
orientation = ['ttd', 'dtt', 'diag', 'rdiag', 'ltor', 'rtol']

# declaring an empty list called grid which will be a 2D list containing lists of letters which will contain the words...
# ...hidden among random letters
grid = []

# the size of the grid (this is intended to be provided by the user)
grid_size = 14

# the topic from which the words belong (this is intended to be provided by the user)
topic_name = "spanish soccer teams"

# run a loop to first attach empty lists to the grid in order to make it a 2-D list
for i in range(grid_size):
    grid.append([])

# run another loop to insert random letters in the grid to make a square grid of random letters
for i in range(grid_size):
    for i in range(grid_size):

        # the lowercase letter 'a' is added after each randomly generated letter to differentiate it from the letters which will be inserted by the recursive function
        grid[i].append( rand.choice(alphabets) + 'a')

# declare a list called visited_grid which will contain elements of the form [row, col] as coordinates to tell the recursive functions the locations...
# ...where it attempted to fit a word at a spot but couldn't
visited_grid = []

# often times there are cases where it is impossible to fit all the words generated by the API so this list printed_words is used to keep track...
# ...of the words which could actually fit inside the grid
printed_words = []

# a recursive function which writes the word into the grid if there are no conflicts or else it erases the word by re-generating random letters....
# ...inside the grid at the locations where the misfitting word was printed
def place_word(word, row, col, direction):

    # these two variables must be in global scope because they are subject to required changes after each recursive call of the function
    global grid
    global visited_grid
    
    # creating copies of the original values of row and col to perform operations on those values without losing them
    ROW = row      
    COL = col
    
    # a variable which is used to check if a word has been printed in the grid more than once and then erase the extra copies of the same word
    placement_detector = 0

    # a variable which counts the number of times a word overlapped with another word while being printed
    counter = 0

    # a list which stores the overlap locations in the orientations where either the row changes or column changes but not both
    overlap_locations = []

    # a dictionary which stores key-values pairs as row-column in the orientations where both row and column change during iteration
    overlap_coordinates = {}
    
    if direction == 'ttd':
        # a loop which inserts the word into the grid
        for k in word:
            # a condition which checks if there is a period '.' symbol in the grid element which would imply that the grid element...
            # ...belongs to a previously entered word
            if '.' not in grid[ROW][COL]:
                # if there is no conflict then it edits the grid element at the particular coordinate and inserts the letter from the word
                grid[ROW][COL] = k + '.'
                # read the comments the next time this variable is used
                placement_detector += 1
            else:
                # what to do if there is a conflict at the specific location with another word
                if grid[ROW][COL] != k + '.':
                    # the case of a 'bad' overlap, where the overlapping letter is not the same as the letter being inserted
                    counter += 1
                    overlap_locations.append(ROW)
                if grid[ROW][COL] == k + '.':
                    # the case of a 'good' overlap, where the overlapping letter is the same as the letter being inserted
                    overlap_locations.append(ROW)
            # iterating the ROW to traverse the grid in a top to down fashion       
            ROW += 1

        if counter == 0:
            # the case where the word is inserted with no bad overlaps
            # the visited_grid is reset to an empty list for future use by other words
            visited_grid = []

            # the word is then appended to the list printed_words to certify that the word is present in the grid
            printed_words.append(word)
            return True

        # this condition is used to erase the multiple copies of the same word after the recursive function has...
        # ... found a suitable position for the word in the previous condition
        if placement_detector == len(word):
            for i in range(row, ROW):
                grid[i][col] = rand.choice(alphabets) + 'a'
            visited_grid.append([row, col])
            return True
        
        # the control comes here when the word has faced bad overlaps while printing

        # this loop 'erases' the word by regenerating random letters at the positions where the function had inserted letters 
        for i in range(ROW-1, row-1, -1):

            if i not in overlap_locations:
                # this makes sure that only those locations are randomised which aren't overlap locations so that...
                # any previously entered words aren't disturbed
                grid[i][COL] = rand.choice(alphabets) + 'a'
         
        # clearly, by now it is certain that the initial start position was not a good start position for the word, so...
        # ...this location is added to the visited_grid list
        visited_grid.append([row, col])

        #the function then recurses to a new start position which hasn't already been visited
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
        # the control comes here when the recursion could not find any good start positions in the 'ttd' orientation
            
        # the following 5 lines of code declare a variable 'dir' which is a randomly chosen orientation apart from 'ttd'
        orient = []
        for i in orientation:
            if i != 'ttd':
                orient.append(i)
        dir = rand.choice(orient)

        # the function then recurses with this new orientation dir
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
            
        # the control comes here when the function couldn't find a good start position with the previous orientation...
        # so a new orientation is assigned to 'dir' and the function recurses using this new orientation   
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
         
    # the rest of the code in this function can be understood by referring to the corresponding parts of the code above...
    # ...in this function   
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
            visited_grid = []
             
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
            visited_grid = []
             
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
            visited_grid = []
             
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
            visited_grid = []
             
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
            visited_grid = []
             
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

# this function returns a Boolean value by checking if the start position of the word is meaningful...
# ...for example, if a 10-character long word is being fit in top to down fashion in the grid by starting in the bottom row...
# ...then this function would return False (note that it doesn't check for overlap, it only checks if the word fits or not)
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
# this function generates random start positions for words between the valid limits depending on the chosen orientation
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

# this function checks if the start position is valid, and then inserts the word into the grid
def check_and_place(word, row, col, direction = rand.choice(orientation)):
        
    if check_word_limits(word, row, col, direction):
        place_word(word, row, col, direction)

# this variable contains a list of words as generated by the OpenAI API
word_list = get_words_for_grid(topic_name)

# this loop iterates over the word_list and generates a valid start position for each of them and inserts them...
# ...into the grid
for word in word_list:
    direction = rand.choice(orientation)
    k = word_limits(word,grid_size,direction)
    check_and_place(word, k[0], k[1], direction)

# prints the list of words inserted into the grid
print(printed_words)

# prints all the words provided by the API (not really required, only used for testing purposes)
print(word_list)

# this loop basically removes the 'a' and '.' identifiers from the grid elements and prints the letters in a grid format
for i in grid:
    for k in range(len(i)):
        if '.' in i[k]:
            p = i[k]
            i[k] = p.replace('.','')
        if 'a' in i[k]:
            p = i[k]
            i[k] = p.replace('a','')
    print('  '.join(i))