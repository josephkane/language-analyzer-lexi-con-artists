import unittest
from tokenizer import *

class TestTokenizer(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.message = 'Friendship is like money, easier made than kept.'
        self.message_dict = {
            'p':2, 'r':2, 's':3, 't':2, 'y':1, 'a':3, 'd':2, 'e':7, 'f':1,
            'h':2, 'i':5, 'k':2, 'l':1, 'm':2, 'n':3, 'o':1}
        self.word_list_lower = [
            'friendship', 'is', 'like', 'money', 'easier', 'made', 'than', 'kept']
        self.punctuation = {',':1, '.':1}
        self.word_count = 8
        self.sentence_count = 1

    def test_tokenize(self):
        token_data = tokenize(self.message)

        self.assertEqual(token_data.alphanum_char, self.message_dict)
        self.assertEqual(token_data.word_count, self.word_count)
        self.assertEqual(token_data.sentence_count, self.sentence_count)
        self.assertEqual(token_data.punctuation, self.punctuation)
        self.assertEqual(token_data.word_list, self.word_list_lower)

    def test_get_alphanum_returns_number_of_chars(self):
        self.assertEqual(get_alphanum(self.message), self.message_dict)

    def test_get_punctuation_is_punctuation(self):
        self.assertEqual(get_punctuation(self.message), self.punctuation)

if __name__ == '__main__':
    unittest.main()
