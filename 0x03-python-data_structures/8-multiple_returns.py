#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Finds the length and first character of
    a sentence
    :pamam sentence: The sentence
    :Return: Tuple containing the first character
    and length of the sentence
    """
    sentence_len = len(sentence)
    if (sentence_len == 0):
        return (sentence_len, None)

    return (sentence_len, sentence[0])
