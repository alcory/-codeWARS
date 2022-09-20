def spin_words(sentence):
    new_words = []
    for word in sentence.split():
        if len(word) >= 5:
            new_words.append(word[::-1])
        else:
            new_words.append(word)
    return ' '.join(new_words)
