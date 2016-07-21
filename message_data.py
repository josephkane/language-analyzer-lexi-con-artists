class MessageData:
    '''
    Contain the details of an individual message

    Properties:
        author - a string of the message author
        message - a string of the message
        token_data - TokenData of the tokenized messsage
        classified_data - dictionary of ClassifiedData from lexicons

    Methods:
        add_classified_data - add data to the classified_data dictionary
        calc_final_scores - get the scores from the classified_data
    '''

    def __init__(self):
        '''
        Initialize default values
        '''

        self.author = ''
        self.message = ''
        self.token_data = None
        self.classified_data = dict()

    def add_classified_data(self, data):
        '''
        Add data to the classified_data dictionary based on category

        Arguments:
            The data to add
        '''
        self.classified_data[data.category_key] = data

    def calc_final_scores(self):
        '''
        Generate score values from the data

        Returns:
            A dictionary of score values
        '''

        output = dict()

        output['author'] = self.author
        output['message'] = self.message

        output['scores'] = dict()
        scores = output['scores']

        for t in self.classified_data.keys():
            data = self.classified_data[t]
            scores[t] = dict()
            for sub, score in data.subcount.items():
                scores[t][sub] = round(score / data.count, 1)

        return output
