game_data = {
    'start': {'description': 'Welcome to the game!', 'options': ['play', 'quit']},
    'play': {'description': 'You are playing the game!', 'options': ['win', 'lose', 'quit']},
    'win': {'description': 'You won! Congratulations!', 'options': ['play', 'quit']},
    'lose': {'description': 'You lost. Better luck next time!', 'options': ['play', 'quit']},
    'quit': {'description': 'Goodbye!', 'options': []}
}

# Initialize the current state
current_state = 'start'

# Game loop
while True:
    # Print the current description
    print(game_data[current_state]['description'])

    # Get the user's input
    user_input = input('> ')

    # Handle the user's input
    if user_input in game_data[current_state]['options']:
        current_state = user_input
    else:
        print("Invalid input. Try again")