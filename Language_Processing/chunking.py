#!/usr/local/bin/python3.5

import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
import re


train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():

	try:
		for i in tokenized:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
		
			chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
			#chunkGram = r"""Chunk: {<NNP.?>*}"""
			chunkParser = nltk.RegexpParser(chunkGram)
			chunked = chunkParser.parse(tagged)
			#if re.search('^(Chunk.+ )?',str(chunked)):		
			print(chunked)

			#if chunked.find("Chunk:"):
		#		print(chunked)

	except Exception as e:
		print(str(e))


process_content() 
