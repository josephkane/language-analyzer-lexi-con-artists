class MessageData:
    def __init__(self):
        self.author = ''
        self.message = ''
        self.token_data = None
        self.classified_data = dict()

    def calc_final_scores(self):
        output = dict()

        output['author'] = self.author
        output['message'] = self.message

        output['scores'] = dict()
        scores = output['scores']

        # for each classified_data

        return output
