import string


def abbreviate(words):
    words = ''.join(
        [letter if letter not in string.punctuation or letter == "'" else ' ' for letter in words])
    return ''.join([word[0] for word in words.upper().split(' ') if word != ''])
