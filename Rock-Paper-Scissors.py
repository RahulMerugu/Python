import random

def get_choices():
    options = ['Rock', 'Paper', 'Scissors']
    p1 = input('Enter a choice (Rock, Paper, Scissors): ').lower()


    if p1 in ['paper', 'p']:
        p1 = 'Paper'
    elif p1 in ['rock', 'r']:
        p1 = 'Rock'
    elif p1 in ['scissors', 's']:
        p1 = 'Scissors'
    else:
        return {'Player': 'Invalid', 'Computer': random.choice(options)}
    
    p2 = random.choice(options)
    return {'Player': p1, 'Computer': p2}

def check_win(p1, p2):
    print(f"You chose: {p1}, Computer chose: {p2}")

    if p1 == 'Invalid':
        return "Invalid input. Please choose Rock, Paper, or Scissors."

    if p1 == p2:
        return "It's a tie!"

    # Game logic
    if p1 == 'Rock':
        if p2 == 'Scissors':
            return 'Rock smashes Scissors! You Win!'
        else:
            return 'Paper covers Rock! You Lose.'
    elif p1 == 'Paper':
        if p2 == 'Rock':
            return 'Paper covers Rock! You Win!'
        else:
            return 'Scissors cuts Paper! You Lose.'
    elif p1 == 'Scissors':
        if p2 == 'Paper':
            return 'Scissors cuts Paper! You Win!'
        else:
            return 'Rock smashes Scissors! You Lose.'
    else:
        return 'Unexpected error!'

choices = get_choices()
result = check_win(choices['Player'], choices['Computer'])
print(result)
