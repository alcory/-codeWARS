def disemvowel(string_):
    vowels = {"a": '',"e": '', "i": '', "o": '', "u": ''}
    new_string = ""
    for letter in string_:
        if letter.lower() in vowels:
            new_string += ''.join('')
        else:
            new_string += ''.join(letter)
    return(new_string)


print(disemvowel('This is a comment'))
