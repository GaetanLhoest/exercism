def count_words(sentence):
    sentence = split_sentence(sentence.lower())
    words = [clean_word(i) for i in sentence if i != '']
    words_count = {}
    words_count = dict.fromkeys(words, 0)
    for i in words:
        words_count[i] += 1
    return words_count


def split_sentence(sentence):
    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789'"
    return ''.join([i if (i in allowed_chars) else ' ' for i in sentence]).split(' ')


def clean_word(word):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    return ''.join([str(i) for index, i in enumerate(word) if (word[index] in allowed_chars) or (0 < index < len(word) - 1 and word[index-1] in allowed_chars and word[index + 1] in allowed_chars)])
