#!/usr/bin/python

import nltk
from nltk.corpus import names
import random


def gender_features(word):
	return {'last_letter': word}


labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
		[(name, 'female') for name in names.words('female.txt')])

featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)

while True:
	inserted_value = raw_input("Enter Name: ")
	if inserted_value == "Done":
		break

	else:
		print classifier.classify(gender_features(inserted_value))
		

print(nltk.classify.accuracy(classifier, test_set))
classifier.show_most_informative_features(5)
