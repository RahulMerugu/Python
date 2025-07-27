import random

def get_choices():
    options = ['Rock' , 'Paper' , 'Scissors']
    p1 = input('Enter a choice (Rock, Paper, Scissors):')
    p2 = random.choice(options)
    choices = {'Player' : p1, 'Computer' : p2}
    return choices

def check_win(p1 , p2):
    print (f"You chose: {p1}, Computer chose:{p2}")
    if p1 == p2:
        return "It's a tie!"
    elif p1 == 'Rock':
        if p2 == 'Scissors':
            return 'Rock smashes Scissors! You Win!'
        else:
            return 'Paper covers Rock! You Lose.'
    elif p1 == 'Paper':
        if p2 == 'Scissors':
            return 'Scissors cuts Paper! You Lose.'
        else:
            return 'Paper covers Rock! You Win!'
    elif p1 == 'Scissors':
        if p2 == 'Paper':
            return 'Scissors cuts Paper! You Win!'
        else:
            return 'Rock smashes Scissors! You Lose.'
    else:
        return 'Error!'
    
choices = get_choices()
result = check_win(choices['Player'], choices['Computer'])
print (result)




