class Lexicon:

    def __init__(self, lexicon):
        self.lexicon = lexicon

    def categorize_message(self, msg):
        data  = ClassifiedData()
        data.subcount = dict.fromkeys(self.lexicon.keys(), 0)
        for word in msg.word_list:
            word_added = False
            for subcategory, entries in self.lexicon.items():
                if word in entries.keys():
                    if not word_added:
                        data.count += 1
                        word_added = True
                    data.subcount[subcategory] += 1

        return data

class ClassifiedData:

    def __init__(self):
        self.count = 0
        self.subcount = dict()

