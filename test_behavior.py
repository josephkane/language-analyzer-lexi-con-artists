import unittest

from behavior import *
from tokenizer import *

class TestBehavior(unittest.TestCase):

    def test_behavior_returns_correct_values(self):
        token_data = TokenData()
        token_data.message_dict = {'p':2, 'r':2, 's':3, 't':2, 'y':1, 'a':3, 'd':2, 'e':7, 'f':1, 'h':2, 'i':5, 'k':2, 'l':1, 'm':2, 'n':3, 'o':1}
        token_data.word_list = ['friendship', 'is', 'like', 'money', 'easier', 'made', 'than', 'kept']
        token_data.punctuation = {',':1, '.':1, '!':1, '?':1}

        classified_data = ClassifiedData()
        classified_data.category_key = 'behavior'
        classified_data.count = 6
        classified_data.subcount = {'mentoring':1, 'transaction':3, 'aggressive':1, 'passive':0, 'inquisitive':1}

        behavior = Behavior()
        classified_message = behavior.categorize_message(token_data)

        self.assertEqual(classified_message.category_key, classified_data.category_key)
        self.assertEqual(classified_message.count, classified_data.count)
        self.assertEqual(classified_message.subcount, classified_data.subcount)

if __name__ == '__main__': # pragma: no cover
    unittest.main()
