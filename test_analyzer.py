import unittest

from analyzer import *

class TestAnalyzer(unittest.TestCase):

    def test_create_message_output(self):
        score_data = {
            'author': 'Françoise Sagan',
            'message': 'Class is an aura of confidence that is being sure without being cocky. Class has nothing to do with money. Class never runs scared. It is self-discipline and self-knowledge. It\'s the sure-footedness that comes with having proved you can meet life.',
            'scores': {
                'sentiment': {
                    'positive': 0.5,
                    'negative': 0.2,
                    'neutral': 0.3
                },
                'domain': {
                    'financial': 0.1,
                    'behavioral': 0.2,
                    'scientific': 0.7,
                    'educational': 0.4,
                    'politics': 0.1,
                    'relationships': 0.1
                },
                'behavior': {
                    'aggressive': 0.1,
                    'passive': 0.4,
                    'mentoring': 0.6,
                    'inquisitive': 0.8,
                    'transaction': 0.3
                }
            }
        }

        expected = '''
        Author:   Françoise Sagan
        Message:  Class is an aura of confidence that is being sure without being cocky. Class has nothing to do with money. Class never runs scared. It is self-discipline and self-knowledge. It's the sure-footedness that comes with having proved you can meet life.

        # sentiment #
        - positive       [|||||-----]  0.5
        - neutral        [||--------]  0.2
        - negative       [|||-------]  0.3

        # domain #
        - financial      [|---------]  0.1
        - behavioral     [||--------]  0.2
        - scientific     [|||||||---]  0.7
        - educational    [||||------]  0.4
        - politics       [|---------]  0.1
        - relationships  [|---------]  0.1

        # behavior #
        - aggressive     [|---------]  0.1
        - passive        [||||------]  0.4
        - mentoring      [||||||----]  0.6
        - inquisitive    [||||||||--]  0.8
        - transaction    [|||-------]  0.3
        '''

        self.assertEqual(create_message_output(score_data), expected)

if __name__ == '__main__':
    unittest.main()
