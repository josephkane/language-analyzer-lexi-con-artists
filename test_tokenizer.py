import unittest
from tokenizer import *

class TestTokenizer(unittest.TestCase):
    """docstring for test_analyzer"""
    def test_tokenize(self):
        message = 'Friendship is like money, easier made than kept'
        token_data = tokenize(message)
        message_dict = {'p':2, 'r':2, 's':3, 't':2, 'y':1, 'a':3, 'd':2, 'e':7, 'f':1, 'h':2, 'i':5, 'k':2, 'l':1, 'm':2, 'n':3, 'o':1}
        word_list = ['Friendship', 'is', 'like', 'money', 'easier', 'made', 'than', 'kept']
        word_list_lower = ['friendship', 'is', 'like', 'money', 'easier', 'made', 'than', 'kept']
        punctuation = {',':1, '.':1}
        self.assertEqual(token_data.alphanum_char, message_dict)
        self.assertEqual(token_data.word_count, 8)
        self.assertEqual(token_data.word_positions, word_list)
        self.assertEqual(token_data.sentence_count, 1)
        self.assertEqual(token_data.punctuation, punctuation)
        self.assertEqual(token_data.word_list_lower_case, word_list_lower)

    def test_alphanum_char_returns_number_of_chars(self):
        '''docstring for test_alpha_num_chars'''
        message = 'Friendship is like money, easier made than kept'
        message_dict = {'p':2, 'r':2, 's':3, 't':2, 'y':1, 'a':3, 'd':2, 'e':7, 'f':1, 'h':2, 'i':5, 'k':2, 'l':1, 'm':2, 'n':3, 'o':1}
        self.assertEqual(alphanum_char(message), message_dict)

    def test_punctuation_is_punctuation(self):
        punctuation = {',':1, '.':1}
        self.assertEqual(punctuation, punctuation)
