import re

class Tokenizer:
    """
    Accepts a string, calculates and returns:
        1. Alpha-numeric characters present
        2. Word count
        3. Word position
        4. Sentence count
        5. Punctuation present
        6. List of all words, lowercased

    """

    def tokenize(self, string):
        token_data = TokenData()

        token_data.sentence_count = len(re.split(r"[.!?] ", string))

        lower_case = string.lower()
        no_punc = re.sub(r"[^a-z ]", "", lower_case)
        token_data.word_list_lower_case = no_punc.split(" ")

        token_data.punctuation = self.get_punctuation(lower_case)
        token_data.alphanum_char = self.get_alphanum(no_punc)

        token_data.word_count = len(token_data.word_list_lower_case)

        return token_data

    def get_alphanum(self, string):
        no_space = string.replace(" ", "")
        characters = set(no_space)

        return {char: string.count(char) for char in characters}

    def get_punctuation(self, string):
        no_char = re.sub(r"[a-z ]", "", string)
        punctuation = set(no_char)

        return {punc: string.count(punc) for punc in punctuation}

class TokenData:

    def __init__(self):
        self.alphanum_char = dict()
        self.word_count = 0
        self.word_position = list()
        self.sentence_count = 0
        self.punctuation = dict()
        self.word_list_lower_case = list()