""" This module using max apriori method classifies the document into a topic."""

import os
import time
import math
from collections import OrderedDict
from clean_data import cleandata, convert_to_lower


def readTestFile(filename):
	""" For words from file
	Args:
		filename (string) : Name of the file to be read
	Return:
		words[list] 	  : List of words in the file
	"""
	f = open(filename, 'r')
	linetext = f.readlines()
	words=[]
	for line in linetext:
		line = line.rstrip('\n').rstrip('\t')
		words.append(line.split(' '))
	f.close()
	return [item for w in words for item in w]


def test(root_path, likelihood):
	"""
		For each file in test directory, detremines probabilty of each word
		from calculated by naive bayes model in training phase and by using
		max apriori method, estimates the topic to which the file belongs to.
		Args:
			root_path (string) 		: Root directory
			likelihood (dictionary) : Likelihood from training model
	"""
	os.chdir(root_path+'/test')
	path = str(os.getcwd())
	topics = os.listdir(path)
	no_of_files = 0
	for each_topic in topics:
		filepath = path+'/'+each_topic
		os.chdir(filepath)
		filenames = os.listdir(filepath)
		
		for eachFile in filenames:
			no_of_files+=1
			words = list(OrderedDict.fromkeys(cleandata(convert_to_lower(readTestFile(eachFile)))))
			posterior =  dict((key,sum(value[everyWord] if everyWord in value else math.log(0.0000001)\
						 for everyWord in words)) for key,value in likelihood.iteritems())

			deducted_topic = max(posterior, key=posterior.get)
			print no_of_files,"For file ",eachFile," Deducted topic:",deducted_topic.upper()," Actual topic: ",each_topic.upper()