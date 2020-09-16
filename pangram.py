import string
def is_pangram(sentence):
    alphabets_lower = string.ascii_lowercase
    sentence = sentence.lower()
    for x in alphabets_lower:
        if x not in sentence:
            return False
    return True
