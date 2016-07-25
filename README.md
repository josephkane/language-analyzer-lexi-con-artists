# Language Analyzer

The language analyzer will use sentiment analysis, and behavior prediction to produce a report for each message.

## Overview

![python](https://img.shields.io/badge/python-3.3.6+-blue.svg)
![coverage](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)

Running `python analyzer.py` will produce an analysis report for each message stored in messages.py


##### Example output

```
Author:   Stephen Frank
Message:  Bottom line is, I didn't return to Apple to make a fortune. I've been                                                                                                                                                              very lucky in my life and already have one. When I was 25, my net worth was $100                                                                                                                                                              million or so. I decided then that I wasn't going to let it ruin my life. There                                                                                                                                                             's no way you could ever spend it all, and I don't view wealth as something that                                                                                                                                                              validates my intelligence.

# behavior #
-aggressive     [||--------]  0.2
-inquisitive    [----------]  0.0
-mentoring      [|---------]  0.1
-passive        [|---------]  0.1
-transaction    [||||||||--]  0.8

# domain #
-behavioral     [|---------]  0.1
-educational    [|---------]  0.1
-financial      [||||||----]  0.6
-politics       [|---------]  0.1
-relationships  [----------]  0.0
-scientific     [|---------]  0.1

# sentiment #
-negative       [||--------]  0.2
-neutral        [||||||----]  0.6
-positive       [|||-------]  0.3

```

## Tokenizer

The tokenizer module will produce the following results for each message.

1. Alphanumeric Characters
1. Word count
1. Word position
1. Sentence count
1. Punctuation

## Domain Identifier

The domain module will determine the subject matter of the message and will produce a domain value between 0 and 1 for each message, for each domain identified.

1. Words stored in the `domain_lexicon` dictionary.
1. Punctuation
1. Word count

## Behavior Predictor

This behavior module will determine what behavior is expressed in a message and will produce a behavior value between 0 and 1 for each message, for each behavior identified.

1. Words stored in the `behavior_lexicon` dictionary.
1. Punctuation (e.g. question marks may indicate inquisitiveness, exclamation point may indicate aggressiveness)

## Sentiment Analysis

The sentiment module will produce a sentiment value between 0 and 1 for each message, for each sentiment identified.

1. Words stored in the `sentiment_lexicon` dictionary.
1. Punctuation (e.g. exclamation points may increase the sentiment value)
1. Behavior value
