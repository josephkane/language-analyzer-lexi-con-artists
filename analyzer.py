from messages import *
from message_data import *
from tokenizer import *
from behavior import *
from domain import *
from sentiment import *

def analyze_messages():
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

        message_data.classified_data['behavior'] = behavior.categorize_message(message_data.token_data)
        message_data.classified_data['domain'] = domain.categorize_message(message_data.token_data)
        message_data.classified_data['sentiment'] = sentiment.categorize_message(message_data.token_data)

        score_data = message_data.calc_final_scores()

        print(create_message_output(score_data))

def create_message_output(score_data):
    '''
    Build an output string for a message

    Args:
        A dictionary containg message info and score values

    Returns:
        A formatted string to print
    '''

    output = ''
    output += 'Author:   {}\n'.format(score_data['author'])
    output += 'Message:  {}\n'.format(score_data['message'])
    output += '\n'

    for category, subcategories in sorted(score_data['scores'].items()):
        output += '# {} #\n'.format(category)
        for sub, score in sorted(subcategories.items()):
            bars = '[' + '|' * int(score * 10) + '-' * int(10 - score * 10) + ']'
            output += '- {}{}{}  {}\n'.format(sub, ' ' * (15 - len(sub)), bars, score)
        output += '\n'

    return output

if __name__ == '__main__':
    analyze_messages()
