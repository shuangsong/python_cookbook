#get the word count page 66
sentence = "Peter piper picked a peck of pickled peppers A peck of pickled"
word_dict = {} #initialize a dictionary object
for word in sentence.split():
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1
    print word_dict

