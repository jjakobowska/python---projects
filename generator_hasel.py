import sys
pasword = []
characters_left = -1

def update_characters_left(number_of_characters):
    if number_of_characters < 0 or number_of_characters > characters_left:
        print('liczba znaków spoza przedziału 0,', characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_characters
        
        

password_lenght = int(input('jak długie ma być hasło?'))

if password_lenght <5:
    print('Hasło jest za krótkie. Musi mieć minimum 5 znaków. Spróbuj jeszcze raz')
    sys.exit(0)
else:
    characters_left = password_lenght

lowercase_letters = int(input('ile małych liter ma mieć hasło?'))

if lowercase_letters < 0 or lowercase_letters > characters_left:
    print('liczba znaków spoza przedziału 0,', characters_left)
    sys.exit(0)
else:
    characters_left -= lowercase_letters
    
uppercase_letters = int(input('ile dużych liter ma mieć hasło?'))

if uppercase_letters < 0 or uppercase_letters > characters_left:
    print('liczba znaków spoza przedziału 0,', characters_left)
    sys.exit(0)
    
special_characters = int(input('ile znaków specjalnych ma mieć hasło?'))
digits = int(input('ile cyfr ma mieć hasło?'))


