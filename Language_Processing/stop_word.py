#!/usr/local/bin/python3.5

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence="This is an example showing of Stop word filteration"


stop_words =  set (stopwords.words("english"))

words = word_tokenize(example_sentence)

filter_sentence = []

for w in words:

	if w not in stop_words:
		filter_sentence.append(w)

print (filter_sentence)
	
