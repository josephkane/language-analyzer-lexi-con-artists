import unittest

from lexicon import ClassifiedData
from message_data import *

class TestScoring(unittest.TestCase):
    def test_score_output(self):
        self.maxDiff = None
        
        score_data = {
            "author": "Françoise Sagan",
            "message": "Class is an aura of confidence that is being sure without being cocky. Class has nothing to do with money. Class never runs scared. It is self-discipline and self-knowledge. It's the sure-footedness that comes with having proved you can meet life.",
            "scores": {
                "sentiment": {
                    "positive": 0.5,
                    "negative": 0.2,
                    "neutral": 0.3
                },
                "domain": {
                    "financial": 0.1,
                    "behavioral": 0.2,
                    "scientific": 0.7,
                    "educational": 0.4,
                    "politics": 0.1,
                    "relationships": 0.1
                },
                "behavior": {
                    "aggressive": 0.1,
                    "passive": 0.4,
                    "mentoring": 0.6,
                    "inquisitive": 0.8,
                    "transaction": 0.3
                }
            }
        }
        message_data = MessageData()
        message_data.author = "Françoise Sagan"
        message_data.message = "Class is an aura of confidence that is being sure without being cocky. Class has nothing to do with money. Class never runs scared. It is self-discipline and self-knowledge. It's the sure-footedness that comes with having proved you can meet life."
        sentiment = ClassifiedData()
        sentiment.count = 6
        sentiment.subcount = {
            "positive": 3,
            "negative": 1,
            "neutral": 2
        }
        domain = ClassifiedData()
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

        self.assertEqual(message_data.calc_final_scores(), score_data)

if __name__ == '__main__':
    unittest.main()
