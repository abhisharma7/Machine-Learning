#!/usr/local/bin/python3.6

import nltk
from nltk.corpus import brown


def best_word_prob(word_selected,probability_selected_word):

	print(100 * float((prob_brown_2gram[word_selected].prob(probability_selected_word))))

def best_possible_words(word_entered,print_count):

	print(freq_brown_2gram[str(word_entered)].most_common(int(print_count)))

word = str(input("Enter Word: "))
enter_count = str(input("Count: "))
freq_brown_2gram = nltk.ConditionalFreqDist(nltk.bigrams(brown.words()))
prob_brown_2gram = nltk.ConditionalProbDist(freq_brown_2gram, nltk.MLEProbDist)

best_possible_words(word,enter_count)
selected_word = input("Choose word: ")
best_word_prob(word,selected_word)
