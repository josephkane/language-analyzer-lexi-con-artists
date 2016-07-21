import unittest

from sentiment import *
from tokenizer import *
from message_data import *

class TestSentiment(unittest.TestCase):
    def message_data_set_up():
        message_data = MessageData()
        message_data.author = "Françoise Sagan"
        message_data.message = "Class is an aura of confidence that is being sure without being cocky. Class has nothing to do with money. Class never runs scared. It is self-discipline and self-knowledge. It's the sure-footedness that comes with having proved you can meet life!"
        sentiment = ClassifiedData()
        sentiment.category_key = 'sentiment'
        sentiment.count = 6
        sentiment.subcount = {
            "positive": 3,
            "negative": 1,
            "neutral": 2
        }
        domain = ClassifiedData()
        domain.category_key = 'domain'
        domain.count = 21
        domain.subcount = {
            "financial": 3,
            "behavioral": 5,
            "scientific": 15,
            "educational": 8,
            "politics": 3,
            "relationships": 2
        }
        behavior = ClassifiedData()
        behavior.category_key = 'behavior'
        behavior.count = 10
        behavior.subcount = {
            "aggressive": 1,
            "passive": 4,
            "mentoring": 6,
            "inquisitive": 8,
            "transaction": 3
        }
        message_data.classified_data = {
            "sentiment": sentiment,
            "domain": domain,
            "behavior": behavior
        }

        return message_data

    def test_sentiment_returns_correct_values(self):
        token_data = TokenData()
        token_data.message_dict = {'p':2, 'r':2, 's':3, 't':2, 'y':1, 'a':3, 'd':2, 'e':7, 'f':1, 'h':2, 'i':5, 'k':2, 'l':1, 'm':2, 'n':3, 'o':1}
        token_data.word_list = ['friendship', 'is', 'like', 'money', 'easier', 'made', 'than', 'kept']
        token_data.punctuation = {',':1, '.':1, '!':1}

        classified_data = ClassifiedData()
        classified_data.category_key = 'sentiment'
        classified_data.count = 5
        classified_data.subcount = {'positive':4, 'neutral':2, 'negative':0}

        sentiment = Sentiment()
        classified_message = sentiment.categorize_message(token_data)

        self.assertEqual(classified_message.category_key, classified_data.category_key)
        self.assertEqual(classified_message.count, classified_data.count)
        self.assertEqual(classified_message.subcount, classified_data.subcount)

    def test_modify_sentiment_from_behavior(self):
        message_data = TestSentiment.message_data_set_up()

        sentiment_class = Sentiment()
        sentiment_original = {
            "positive": 3,
            "negative": 1,
            "neutral": 2
        }

        sentiment_class.modify_sentiment_from_behavior(message_data)
        self.assertNotEqual(message_data.classified_data['sentiment'].subcount, sentiment_original)

    def test_greater(self):
        message_data = TestSentiment.message_data_set_up()

        message_data.classified_data['behavior'].count = 14
        message_data.classified_data['behavior'].subcount = {
            "aggressive": 1,
            "passive": 300,
            "mentoring": 1,
            "inquisitive": 1,
            "transaction": 1
        }
        sentiment_class = Sentiment()
        sentiment_original = {
            "positive": 3,
            "negative": 1,
            "neutral": 2
        }

        sentiment_class.modify_sentiment_from_behavior(message_data)
        self.assertNotEqual(message_data.classified_data['sentiment'].subcount, sentiment_original)

    def test_equal(self):
        message_data = TestSentiment.message_data_set_up()

        message_data.classified_data['behavior'].count = 14
        message_data.classified_data['behavior'].subcount = {
            "aggressive": 1,
            "passive": 7,
            "mentoring": 1,
            "inquisitive": 1,
            "transaction": 1
        }
        sentiment_class = Sentiment()
        sentiment_original = {
            "positive": 3,
            "negative": 1,
            "neutral": 2
        }

        sentiment_class.modify_sentiment_from_behavior(message_data)
        self.assertNotEqual(message_data.classified_data['sentiment'].subcount, sentiment_original)

    def test_aggressive(self):
        message_data = TestSentiment.message_data_set_up()

        message_data.classified_data['behavior'].count = 14
        message_data.classified_data['behavior'].subcount = {
            "aggressive": 7,
            "passive": 1,
            "mentoring": 1,
            "inquisitive": 1,
            "transaction": 1
        }
        sentiment_class = Sentiment()
        sentiment_original = {
            "positive": 3,
            "negative": 1,
            "neutral": 2
        }

        sentiment_class.modify_sentiment_from_behavior(message_data)
        self.assertNotEqual(message_data.classified_data['sentiment'].subcount, sentiment_original)


    def test_no_change(self):
        message_data = TestSentiment.message_data_set_up()

        message_data.classified_data['behavior'].count = 10
        message_data.classified_data['behavior'].subcount = {
            "aggressive": 1,
            "passive": 1,
            "mentoring": 1,
            "inquisitive": 1,
            "transaction": 1
        }
        sentiment_class = Sentiment()
        sentiment_original = {
            "positive": 3,
            "negative": 1,
            "neutral": 2
        }

        sentiment_class.modify_sentiment_from_behavior(message_data)
        self.assertEqual(message_data.classified_data['sentiment'].subcount, sentiment_original)



if __name__ == '__main__':
    unittest.main()
