#In this kata you are required to, given a string, replace every letter with its position in the alphabet.
#If anything in the text isn't a letter, ignore it and don't return it.
def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ' '.join([str(alphabet.find(symbol)+1) for symbol in text.lower() if symbol.isalpha()])