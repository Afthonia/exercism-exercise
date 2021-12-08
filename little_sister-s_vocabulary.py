def add_prefix_un(word):
    return "un" + word
def make_word_groups(vocab_words):
    words = [vocab_words[0]]
    for word in range(1,len(vocab_words)):
        words.append(vocab_words[0] + vocab_words[word])
    return ' :: '.join(words)
def remove_suffix_ness(word):
    if word[-5] == "i":
        return word[:-5] + "y"
    return word[:-4]
def noun_to_verb(sentence, index):
    if sentence[index][-1] == ".":
        return sentence.split()[index][:-1] + "en"
    return sentence.split()[index] + "en"
