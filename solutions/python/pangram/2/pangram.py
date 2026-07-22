''' strings '''
def is_pangram(sentence):
    ''' is pangram '''
    used_letters = {char for char in sentence.lower() if char.isalpha()}
    return len(used_letters) == 26
    
