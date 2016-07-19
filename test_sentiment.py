import unittest
from sentiment import *
from tokenizer import *

class test_sentiment(unittest.TestCase):
    '''docstring for sentiment'''
    def test_sentiment_returns_correct_values(self):
        token_data = TokenData()
        token_data.message_dict = {'p':2, 'r':2, 's':3, 't':2, 'y':1, 'a':3, 'd':2, 'e':7, 'f':1, 'h':2, 'i':5, 'k':2, 'l':1, 'm':2, 'n':3, 'o':1}
        token_data.word_list = ['Friendship', 'is', 'like', 'money', 'easier', 'made', 'than', 'kept']
        token_data.word_list_lower = ['friendship', 'is', 'like', 'money', 'easier', 'made', 'than', 'kept']
        token_data.punctuation = {',':1, '.':1}
        classified_data = ClassifiedData()
        classified_data.count = 4
        classified_data.subCount = {'positive':3, 'neutral':1, 'negative':0}
        sentiment = Sentiment()
        classified_message = sentiment.categorize_message(token_data)
        self.assertEqual(classified_message.count, classified_data.count)
        self.assertEqual(classified_message.subCount, classified_data.subCount)
