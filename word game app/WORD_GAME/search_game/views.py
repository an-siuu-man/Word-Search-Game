from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import random as rand
from openai import OpenAI
import requests
class MakeAGridForm (forms.Form):
    topic_name = forms.CharField(label = "Enter the topic name ", widget=forms.TextInput(attrs={"class": 'topic_name'}) )
    grid_size = forms.IntegerField(label = "Enter the desired grid size ", max_value= 30, min_value=5, widget= forms.NumberInput(attrs={'class': 'grid_size'}))

def recommendation_topics():

    # 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       <---------------- ChatGPT API key (DON'T REMOVE THIS FROM THIS LINE)

    # Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
    openai_api_key = 'YOUR_OPENAI_API_KEY'

    # OpenAI API endpoint
    api_endpoint = 'https://api.openai.com/v1/chat/completions'

    # Request headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai_api_key}'
    }

    # Request payload
    payload1 = {
    'model': 'gpt-4',
    'messages': [{'role': 'user', 'content': 'Give me three creative topics in a comma separated list to make a crossword game, one topic from sports, one topic from science, and one topic from tv entertainment.'}],
    'temperature': 0.8
    }

    response1 = requests.post(api_endpoint, json=payload1, headers=headers)
    l = response1.json()['choices'][0]['message']['content'].split(', ')
    return l


def homepage(request):
    # return HttpResponse('Hello World!')
    recommended_topics = recommendation_topics()
    return render(request, "search_game/homepage.html",{ 
            "form" : MakeAGridForm(), 'recommended_topics': recommended_topics 
            })
def making_the_game(grid_size, word_list):
    grid = []
    visited_grid = []
    printed_words = []
    placement = []
    size_of_grid = grid_size
    def _making_the_game(size_of_grid):
        alphabets = ['A', 'B', 'C', 'D', 'E', 
                'F', 'G', 'H', 'I', 'J', 
                'K', 'L', 'M', 'N', 'O', 
                'P', 'Q', 'R', 'S', 'T', 
                'U', 'V', 'W', 'X', 'Y', 'Z']
        orientation = ['ttd', 'dtt', 'diag', 'rdiag', 'ltor', 'rtol']

        grid_size = size_of_grid
        # placement = []
        for i in range(grid_size):
            grid.append([])
        for i in range(grid_size):
            for i in range(grid_size):
                grid[i].append( rand.choice(alphabets) + 'a')
        # visited_grid = []
        # printed_words = []
        def place_word(word, row, col, direction):
            # global grid
            # global visited_grid
            # global placement
            # global printed_words

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
                
            if check_word_limits(word, row, col-1, direction) and [row, col-1] not in visited_grid:
                valid_pos = place_word(word, row, col-1, direction)
                if valid_pos:
                    return True
            if check_word_limits(word, row-1, col, direction) and [row-1, col] not in visited_grid:
                valid_pos = place_word(word, row-1, col, direction)
                if valid_pos:
                    return True
            if check_word_limits(word, row, col+1, direction) and [row, col+1] not in visited_grid:
                valid_pos = place_word(word, row, col+1, direction)
                if valid_pos:
                    return True
            if check_word_limits(word, row+1, col, direction) and [row+1, col] not in visited_grid:
                valid_pos = place_word(word, row+1, col, direction)
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

        for word in word_list:
            if len(word) <= grid_size:
                direction = rand.choice(orientation)
                k = word_limits(word,grid_size,direction)
                check_and_place(word, k[0], k[1], direction)

        for word in word_list:
            while word not in printed_words:
                direction = rand.choice(orientation)
                k = word_limits(word,grid_size,direction)
                check_and_place(word, k[0], k[1], direction)

        # printed_words = []
        for i in grid:
            for k in range(len(i)):
                if '.' in i[k]:
                    p = i[k]
                    i[k] = p.replace('.','')
                if 'a' in i[k]:
                    p = i[k]
                    i[k] = p.replace('a','')
    _making_the_game(size_of_grid)
    return grid, printed_words

def list_of_words(topic, grid_size):
    Topic = topic
    grid_size = grid_size
    num_of_words = grid_size

    # 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       <---------------- ChatGPT API key (DON'T REMOVE THIS FROM THIS LINE)

    # Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
    openai_api_key = 'YOUR_OPENAI_API_KEY'

    # OpenAI API endpoint
    api_endpoint = 'https://api.openai.com/v1/chat/completions'

    # Request headers
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {openai_api_key}'
    }

    # Request payload
    payload = {
        'model': 'gpt-4',
        'messages': [{'role': 'user', 'content': f'I am making a game of scrabble. Give me approximately {num_of_words} words (with no spaces in the words itself) in all capital letters in a comma separated list from the topic {Topic} which are strictly no longer than {grid_size-1} characters. {int(grid_size*0.3)} of them may be more uncommon than the rest.'}],
        'temperature': 0.8
    }

    # Make the API request
    response = requests.post(api_endpoint, json=payload, headers=headers)
    # Print the response
    k = response.json()['choices'][0]['message']['content'].split(', ')
    return k

def rendering_the_game(request):
    if request.method == "POST":
        form = MakeAGridForm(request.POST)
        if form.is_valid():
            grid_size = form.cleaned_data["grid_size"]
            topic_name = form.cleaned_data["topic_name"]
            GRID, PRINTED_WORDS = making_the_game(grid_size, list_of_words(topic_name, grid_size))
            return render(request, "search_game/gamepage.html", {"grid": GRID, 'printed_words': PRINTED_WORDS})
        else:
            return render(request, "search_game/homepage.html",{ 
            "form" : form 
            })
    return render(request, "search_game/homepage.html",{ 
            "form" : MakeAGridForm() 
            })
