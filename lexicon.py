class Lexicon:
    '''
    Abstract class
    Provide the base method to categorize a message

    Properties:
        lexicon - the data to be used to classify a message (from subclass)
        key - string to use as a dictionary key (class property from subclass)

    Methods:
        categorize_message - process the message to classify its attributes
    '''

    def __init__(self, key, lexicon):
        '''
        Set the lexicon to use

        Arguments:
            A dictionary to use as a lexicon
        '''

        self.key = key
        self.lexicon = lexicon

    def categorize_message(self, token_data):
        '''
        Count the category / subcategory classifications for a message

        Arguments:
            The token data for a message to be categorized

        Returns:
            A ClassifiedData for the message
        '''

        data = ClassifiedData()
        data.category_key = self.key
        data.subcount = dict.fromkeys(self.lexicon.keys(), 0)
        for word in token_data.word_list:
            word_added = False
            for subcategory, entries in self.lexicon.items():
                if word in entries.keys():
                    if not word_added:
                        data.count += entries[word]
                        word_added = True
                    data.subcount[subcategory] += entries[word]

        return data


class ClassifiedData:
    '''
    Contains the counts for a message's classification

    Properties:
        count - the number of times a word has been put into this category
        subcount - a dictionary of subcategories and their counts
    '''

    def __init__(self):
        '''
        Initialize default values
        '''

        self.category_key = ""
        self.count = 0
        self.subcount = dict()
