import unittest

from analyzer import *

class TestAnalyzer(unittest.TestCase):

    def test_create_message_output(self):
        self.maxDiff = None

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

        expected = '''Author:   Françoise Sagan
Message:  Class is an aura of confidence that is being sure without being cocky. Class has nothing to do with money. Class never runs scared. It is self-discipline and self-knowledge. It's the sure-footedness that comes with having proved you can meet life.

# behavior #
- aggressive     [\U0001F621 - - - - - - - - - ]  0.1
- inquisitive    [\U0001F914 \U0001F914 \U0001F914 \U0001F914 \U0001F914 \U0001F914 \U0001F914 \U0001F914 - - ]  0.8
- mentoring      [\U0001F913 \U0001F913 \U0001F913 \U0001F913 \U0001F913 \U0001F913 - - - - ]  0.6
- passive        [\U0001F910 \U0001F910 \U0001F910 \U0001F910 - - - - - - ]  0.4
- transaction    [\U0001F4B8 \U0001F4B8 \U0001F4B8 - - - - - - - ]  0.3

# domain #
- behavioral     [\U0001F607 \U0001F607 - - - - - - - - ]  0.2
- educational    [\U0001f4DA \U0001f4DA \U0001f4DA \U0001f4DA - - - - - - ]  0.4
- financial      [\U0001F4B0 - - - - - - - - - ]  0.1
- politics       [\U0001F5FD - - - - - - - - - ]  0.1
- relationships  [\U0001F48F - - - - - - - - - ]  0.1
- scientific     [\U0001F52C \U0001F52C \U0001F52C \U0001F52C \U0001F52C \U0001F52C \U0001F52C - - - ]  0.7

# sentiment #
- negative       [\U0001F612 \U0001F612 - - - - - - - - ]  0.2
- neutral        [\U0001F636 \U0001F636 \U0001F636 - - - - - - - ]  0.3
- positive       [\U0001F600 \U0001F600 \U0001F600 \U0001F600 \U0001F600 - - - - - ]  0.5

'''

        self.assertEqual(create_message_output(score_data), expected)

if __name__ == '__main__':
    unittest.main()
