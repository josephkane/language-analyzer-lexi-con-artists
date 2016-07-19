class Lexicon:

    def __init__(self, lexicon):
        self.lexicon = lexicon

    def categorize_message(self, msg):
        data  = ClassifiedData()
        for key, value in self.lexicon.items():
         data.subcount[key] = 0
         for k, v in value.items():
             for word in msg.word_list:
                 if k == word:
                    data.count += v
                    data.subcount[key] += v

        return data

class ClassifiedData:

    def __init__(self):
        self.count = 0
        self.subcount = dict()

