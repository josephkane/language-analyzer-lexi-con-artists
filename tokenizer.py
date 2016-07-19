import re

def tokenize(string):
    '''
    Split a string into its component parts

    Args:
        A string to be tokenized

    Returns:
        A token_data object containing:
            - Alpha-numeric characters present
            - Word count
            - Sentence count
            - Punctuation present
            - List of all words, lowercased
    '''

    token_data = TokenData()

    token_data.sentence_count = len(re.split(r'[.!?] ', string))

    lower_case = string.lower()
    no_punc = re.sub(r'[^a-z ]', '', lower_case)
    token_data.word_list = no_punc.split(' ')

    token_data.punctuation = get_punctuation(string)
    token_data.alphanum_char = get_alphanum(string)

    token_data.word_count = len(token_data.word_list)

    return token_data

def get_alphanum(string):
    '''
    Get the alphanumeric characters and their counts from a string

    Args:
        A string to deconstruct

    Returns:
        A dictionary of alphanumeric characters and their number of occurences
    '''

    no_punc = re.sub(r'[^a-z]', '', string.lower())
    characters = set(no_punc)

    return {char: no_punc.count(char) for char in characters}

def get_punctuation(string):
    '''
    Get the punctuation and their counts from a string

    Args:
        A string to deconstruct

    Returns:
        A dictionary of punctuation and their number of occurences
    '''

    no_char = re.sub(r'[a-z ]', '', string.lower())
    punctuation = set(no_char)

    return {punc: no_char.count(punc) for punc in punctuation}


class TokenData:

    def __init__(self):
        self.alphanum_char = dict()
        self.word_count = 0
        self.sentence_count = 0
        self.punctuation = dict()
        self.word_list = list()
