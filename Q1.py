def reverse_string(a_string):
    return a_string[::-1]

def reverse_string_by_word(a_sentence):
    rev = []
    for word in a_sentence.split(" "):
        rev.append(reverse_string(word))
    return ' '.join(rev)


