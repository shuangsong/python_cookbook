#page 66: get the word count 
sentence = "Peter piper picked a peck of pickled peppers A peck of pickled"
word_dict = {} #initialize a dictionary object
for word in sentence.split():
    if word not in word_dict:
        word_dict[word] = 1
    else:
        word_dict[word] += 1
    print word_dict



#page 73: effective use of a dictionary of dictionaries
from collections import defaultdict
user_movie_rating = defaultdict(lambda : defaultdict(int))

user_movie_rating["Alice"]["LOR1"] = 4
user_movie_rating["Alice"]["LOR2"] = 5
user_movie_rating["Alice"]["LOR3"] = 3
user_movie_rating["Alice"]["SW1"] = 5
user_movie_rating["Alice"]["SW2"] = 3

print user_movie_rating