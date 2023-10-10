def tokenize(sentence):
    words = ''.join([c if c.isalnum() or c.isspace() else ' ' for c in sentence])
    words = words.split()

    words = [word.lower() for word in words]

    return words