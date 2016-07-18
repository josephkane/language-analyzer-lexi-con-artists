import unittest
from behavior import *
from tokenizer import *

class test_behavior(unittest.TestCase):
    '''docstring for behavior'''
    def test_behavior_returns_correct_values(self):
        token_data = TokenData()
        token_data.message_dict = {'p':2, 'r':2, 's':3, 't':2, 'y':1, 'a':3, 'd':2, 'e':7, 'f':1, 'h':2, 'i':5, 'k':2, 'l':1, 'm':2, 'n':3, 'o':1}
        token_data.word_list = ['Friendship', 'is', 'like', 'money', 'easier', 'made', 'than', 'kept']
        token_data.word_list_lower = ['friendship', 'is', 'like', 'money', 'easier', 'made', 'than', 'kept']
        token_data.punctuation = {',':1, '.':1}
        classified_data = ClassifiedData()
        classified_data.count = 4
        classified_data.subCount = {'mentoring':1, 'transaction':3, 'aggressive':0, 'passive':0, 'inquisitive':0}
        behavior = Behavior()
        classified_message = behavior.categorize_message(token_data)
        self.assertEqual(classified_message.count, classified_data.count)
        self.assertEqual(classified_message.subCount, classified_data.subCount)

