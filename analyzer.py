from messages import *
from message_data import *
from tokenizer import *
from behavior import *
from domain import *
from sentiment import *

def analyze_messages(): # pragma: no cover
    '''
    Process each message and print the analyzed results
    '''

    behavior = Behavior()
    domain = Domain()
    sentiment = Sentiment()

    for message in messages:
        message_data = MessageData()
        message_data.author = message['author']
        message_data.message = message['message']

        message_data.token_data = tokenize(message_data.message)

        message_data.add_classified_data(behavior.categorize_message(message_data.token_data))
        message_data.add_classified_data(domain.categorize_message(message_data.token_data))
        message_data.add_classified_data(sentiment.categorize_message(message_data.token_data))

        sentiment.modify_sentiment_from_behavior(message_data)

        score_data = message_data.calc_final_scores()

        print(create_message_output(score_data))
    print(u'\U0001F913' + '  ' + u'\U00002764' + ' ' + u'\U0001F40D')

def create_message_output(score_data):
    '''
    Build an output string for a message

    Args:
        A dictionary containg message info and score values

    Returns:
        A formatted string to print
    '''
    symbols = {
        'positive': u'\U0001F600',
        'negative': u'\U0001F612',
        'neutral': u'\U0001F636',
        'aggressive': u'\U0001F621',
        'passive': u'\U0001F910',
        'mentoring': u'\U0001F913',
        'inquisitive': u'\U0001F914',
        'transaction': u'\U0001F4B8',
        'financial': u'\U0001F4B0',
        'behavioral': u'\U0001F607',
        'scientific': u'\U0001F52C',
        'educational': u'\U0001f4DA',
        'politics': u'\U0001F5FD',
        'relationships': u'\U0001F48F'
    }

    output = ''
    output += 'Author:   {}\n'.format(score_data['author'])
    output += 'Message:  {}\n'.format(score_data['message'])
    output += '\n'

    for category, subcategories in sorted(score_data['scores'].items()):
        output += '# {} #\n'.format(category)
        for sub, score in sorted(subcategories.items()):
            bars = '[' + '| ' * int(score * 10) + '- ' * int(10 - score * 10) + ']'
            output += '- {}{}{}  {}\n'.format(sub, ' ' * (15 - len(sub)), bars, score)
        output += '\n'

    return output

if __name__ == '__main__': # pragma: no cover
    analyze_messages()
