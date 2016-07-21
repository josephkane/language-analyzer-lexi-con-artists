from lexicon import *

class Sentiment(Lexicon):
    '''
    Classify a message into Sentiment subcategories
    '''

    def __init__(self):
        '''
        Call the Lexicon constructor with this lexicon's data
        '''

        super().__init__('sentiment', sentiment_lexicon)


    def categorize_message(self, token_data):
        classified_data = super().categorize_message(token_data)

        if '!' in token_data.punctuation.keys():
            if classified_data.subcount['positive'] > classified_data.subcount['negative']:
                classified_data.subcount['positive'] += token_data.punctuation['!']
            elif classified_data.subcount['negative'] > classified_data.subcount['positive']:
                classified_data.subcount['negative'] += token_data.punctuation['!']


        return classified_data

    def modify_sentiment_from_behavior(self, message_data):
        classified_data = message_data.classified_data

        behavior = classified_data['behavior']
        sentiment = classified_data['sentiment']

        aggressive_count = behavior.subcount['aggressive'] / behavior.count
        passive_count = behavior.subcount['passive'] / behavior.count
        mentoring_count = behavior.subcount['mentoring'] / behavior.count
        positive_count = sentiment.subcount['positive'] / sentiment.count
        negative_count = sentiment.subcount['negative'] / sentiment.count

        sentiment_value = None

        if positive_count > negative_count:
            sentiment_value = 'positive'
        elif negative_count > positive_count:
            sentiment_value = 'negative'

        def modify_from_subcount(score):
            if score >= 0.5:
                count_value = 1
                if score >= 0.75:
                    count_value = 2
                sentiment.count += count_value
                sentiment.subcount[sentiment_value] += count_value

        if sentiment_value:
            modify_from_subcount(aggressive_count)
            modify_from_subcount(mentoring_count)

        count_value = 0
        if passive_count >= 0.75:
            count_value = 2
        elif passive_count >= 0.5:
            count_value = 1
        sentiment.count += count_value
        sentiment.subcount['neutral'] += count_value


sentiment_lexicon = {
    'positive': {
        'ability': 1,
        'able': 1,
        'achieve': 1,
        'action': 1,
        'advance': 1,
        'aimed': 1,
        'allowing': 1,
        'amazing': 1,
        'attainment': 1,
        'being': 1,
        'belief': 1,
        'believe': 1,
        'best': 1,
        'better': 1,
        'blessings': 1,
        'blooming': 1,
        'brothers': 1,
        'can': 1,
        'cares': 1,
        'celebrate': 1,
        'confidence': 1,
        'confident': 1,
        'considerable': 1,
        'continue': 1,
        'continuous': 1,
        'create': 1,
        'creation': 1,
        'credit': 1,
        'defending': 1,
        'definite': 1,
        'democracy': 1,
        'development': 1,
        'discover': 1,
        'discovers': 1,
        'disneyland': 1,
        'dispositions': 1,
        'eager': 1,
        'earned': 1,
        'easier': 1,
        'easily': 1,
        'embrace': 1,
        'encouraging': 1,
        'express': 1,
        'fact': 1,
        'finish': 1,
        'friendship': 1,
        'first': 1,
        'funny': 1,
        'gain': 1,
        'generous': 1,
        'get': 1,
        'give': 1,
        'goal': 1,
        'god': 1,
        'good': 1,
        'gotten': 1,
        'great': 1,
        'greatest': 1,
        'greatly': 1,
        'grow': 1,
        'happiness': 1,
        'happy': 1,
        'help': 1,
        'highly': 1,
        'honored': 1,
        'hopeful': 1,
        'ideas': 1,
        'imagination': 1,
        'imagine': 1,
        'impress': 1,
        'inspiring': 1,
        'intelligence': 1,
        'interest': 1,
        'interesting': 1,
        'its': 1,
        'journey': 1,
        'lead': 1,
        'likely': 1,
        'livelihoods': 1,
        'lives': 1,
        'live': 1,
        'lucky': 1,
        'made': 1,
        'make': 1,
        'making': 1,
        'many': 1,
        'might': 1,
        'mind': 1,
        'miracles': 1,
        'more': 1,
        'most': 1,
        'motivate': 1,
        'much': 1,
        'music': 1,
        'natasha': 1,
        'new': 1,
        'opportunity': 1,
        'own': 1,
        'parties': 1,
        'passions': 1,
        'permit': 1,
        'persistent': 1,
        'personal': 1,
        'positive': 1,
        'positivity': 1,
        'rekindle': 1,
        'relations': 1,
        'reputation': 1,
        'respect': 1,
        'rewarded': 1,
        'romanoff': 1,
        'satisfied': 1,
        'selfdiscipline': 1,
        'selfknowlege': 1,
        'spiritual': 1,
        'succeed': 1,
        'teachings': 1,
        'truth': 1,
        'validates': 1,
        'wealth': 1,
        'wish': 1,
        'worth': 1
    },
    'negative': {
        'absurd': 1,
        'against': 1,
        'anger': 1,
        'angry': 1,
        'aprehend': 1,
        'arduous': 1,
        'arguments': 1,
        'avengers': 1,
        'battle': 1,
        'behind': 1,
        'blind': 1,
        'bribe': 1,
        'cautious': 1,
        'challenge': 1,
        'chance': 1,
        'cocky': 1,
        'conflict': 1,
        'cruel': 1,
        'cruelty': 1,
        'dare': 1,
        'debate': 1,
        'defects': 1,
        'demand': 1,
        'depressed': 1,
        'desire': 1,
        'despite': 1,
        'didnt': 1,
        'different': 1,
        'disappointment': 1,
        'disemboweled': 1,
        'disfigured': 1,
        'dont': 1,
        'doubtful': 1,
        'drama': 1,
        'drug': 1,
        'emotional': 1,
        'emotions': 1,
        'encounter': 1,
        'endeaver': 1,
        'endure': 1,
        'endured': 1,
        'energy': 1,
        'enjoyed': 1,
        'enthusiasm': 1,
        'evil': 1,
        'extinguish': 1,
        'extreme': 1,
        'fear': 1,
        'fearful': 1,
        'fighting': 1,
        'foolish': 1,
        'government': 1,
        'hard': 1,
        'hostages': 1,
        'hydra': 1,
        'ignorance': 1,
        'isnt': 1,
        'judgmental': 1,
        'least': 1,
        'loki': 1,
        'manipulate': 1,
        'misdeeds': 1,
        'mistakes': 1,
        'morbid': 1,
        'need': 1,
        'negative': 1,
        'negativity': 1,
        'never': 1,
        'no': 1,
        'nonsense': 1,
        'not': 1,
        'nothing': 1,
        'pander': 1,
        'resistance': 1,
        'ruin': 1,
        'scared': 1,
        'sickened': 1,
        'sorry': 1,
        'terrorists': 1,
        'threatening': 1,
        'tortured': 1,
        'wasnt': 1,
        'without': 1
    },
    'neutral': {
        'a': 1,
        'about': 1,
        'afterwards': 1,
        'again': 1,
        'age': 1,
        'all': 1,
        'already': 1,
        'also': 1,
        'american': 1,
        'apache': 1,
        'appear': 1,
        'apple': 1,
        'assembly': 1,
        'assumptions': 1,
        'attitude': 1,
        'aura': 1,
        'banner': 1,
        'barton': 1,
        'be': 1,
        'because': 1,
        'been': 1,
        'before': 1,
        'beforehand': 1,
        'beginning': 1,
        'bodies': 1,
        'boot': 1,
        'bottom': 1,
        'buy': 1,
        'case': 1,
        'change': 1,
        'civilization': 1,
        'class': 1,
        'clear': 1,
        'entirely': 1,
        'evidence': 1,
        'exemption': 1,
        'experiment': 1,
        'find': 1,
        'fire': 1,
        'habit': 1,
        'has': 1,
        'have': 1,
        'havent': 1,
        'having': 1,
        'ignored': 1,
        'impact': 1,
        'kept': 1,
        'kindled': 1,
        'knives': 1,
        'know': 1,
        'known': 1,
        'laws': 1,
        'main': 1,
        'majority': 1,
        'mankind': 1,
        'men': 1,
        'meanings': 1,
        'meet': 1,
        'mental': 1,
        'military': 1,
        'money': 1,
        'must': 1,
        'my': 1,
        'myself': 1,
        'now': 1,
        'pass': 1,
        'politics': 1,
        'reputation': 1,
        'trend': 1,
        'unique': 1,
        'want': 1,
        'whole': 1,
        'wielded': 1,
        'worked': 1,
        'working': 1,
        'worth': 1,
        'would': 1,
        'year': 1,
        'you': 1,
        'your': 1,
        'yourself': 1
    }
}
