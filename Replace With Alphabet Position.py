def alphabet_position(text):
    alphabet = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12, 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
    new_text = text
    for letter in text:
        if letter in alphabet or letter.lower() in alphabet:
            replacement = alphabet.get(letter.lower())
            new_text = new_text.replace(letter,(str(replacement) + ' '))
        elif letter == ' ':
            letter = ''
        else:
            new_text = new_text.replace(letter, '')
    new_text = new_text.replace('  ', ' ')
    new_text = new_text.strip()
    print(new_text, end='')

alphabet_position("The sunset sets at twelve o' clock.")
