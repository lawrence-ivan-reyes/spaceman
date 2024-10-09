# apologies - i could not find any spaceman ascii art that was simple to use so opted for a simple stick man!

def draw_spaceman(incorrect_guesses):
    stages = [  
        '''
           ------
           |
           |
           |
           |
           |
           -
        ''', 
        '''
           ------
           |    |
           |
           |
           |
           |
           -
        ''',
        '''
           ------
           |    |
           |    O
           |
           |
           |
           -
        ''',
        '''
           ------
           |    |
           |    O
           |    |
           |
           |
           -
        ''',
        '''
           ------
           |    |
           |    O
           |   /|
           |
           |
           -
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |
           -
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   /
           -
        ''',
        '''
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |     
           -
        '''
    ]

    # ensure we don't exceed the length of the stages list
    index = min(incorrect_guesses, len(stages) - 1)
    print(stages[index])
