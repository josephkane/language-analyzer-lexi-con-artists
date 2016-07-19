from tokenizer import *

def analyze_messages():
    pass

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

    for category, subcategories in score_data['scores'].items():
        output += '# {} #\n'.format(category)
        for sub, score in subcategories.items():
            bars = '[' + '|' * int(score * 10) + '-' * int(10 - score * 10) + ']'
            output += '- {}{}{}  {}\n'.format(sub, ' ' * (15 - len(sub)), bars, score)
        output += '\n'

    return output

if __name__ == '__main__':
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

    print(create_message_output(score_data))
