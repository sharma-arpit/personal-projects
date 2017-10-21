import nltk
import re

class Analyze():
	
	def __init__(self, positives, negatives, diction):
		self.positive = set()
		self.negative = set()
		self.dictionary = set()
		
		'''load positive words'''
		
		file = open(positives, "r")
		for line in file:
			if not line.startswith(';') and not line.startswith(' '):
				self.positive.add(line.rstrip('\n'))
		file.close()
		
		'''load negative words'''
		
		file = open(negatives, "r")
		for line in file:
			if not line.startswith(';') and not line.startswith(' '):
				self.negative.add(line.rstrip('\n'))
		file.close()
		
		'''load dictionary'''
		
		file = open(diction, "r")
		for line in file:
			self.dictionary.add(line.rstrip('\n'))
		file.close()
		
		
	def analyzer(self, text):
		score=0
		misspelled = []
		tokenizer = nltk.tokenize.TweetTokenizer()
		tokens = tokenizer.tokenize(text)
		for token in tokens:
			if token.lower() not in self.dictionary:
				misspelled.append(token)
			if token.lower() in self.negative:
				score-=1
			if token.lower() in self.positive:
				score+=1
		return misspelled, score
