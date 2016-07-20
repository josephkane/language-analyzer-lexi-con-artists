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

        types = {'behavior', 'domain', 'sentiment'}

        for t in types:
            data = self.classified_data[t]
            scores[t] = dict()
            for sub, score in data.subcount.items():
                scores[t][sub] = round(score / data.count, 1)

        return output
