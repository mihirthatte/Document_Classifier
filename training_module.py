''' This module calculates likelihood of each topic based on naive bayes model'''

import os
import time
import math
from collections import Counter
from clean_data import cleandata, convert_to_lower

def readFiles(path):
	""" Returns list of all words present in all files inside the path directory
	Args:
		path (string) : directory path
	Return:
		list : list of words
	"""
	os.chdir(path)
	file_content = []
	file_name_list = os.listdir(path)
	print "no of iles - ",len(file_name_list)
	for filename in file_name_list:
		f = open(filename, 'r')
		linetext=f.readlines()
		words=[]
		for line in linetext:
			line = line.rstrip('\n').rstrip('\t')
			words.append(line.split(' '))
		file_content.append([everyWord for everyLine in words for everyWord in everyLine])
		f.close()
	return [item for sublist in file_content for item in sublist]


def train():
	""" Returns dictionary as representing likelihood of each topic
		The probability of word given a topic is calculated as frequency
		of word in that topic over total number of words in that topic
	Args:
		None
	Return:
		dictionary 
	"""	
	likelihood = {}
	topics=[]
	words=[]
	
	# changind directory to train
	path = (str(os.getcwd())+'/'+'train') 
	os.chdir(path)
	
	# topics list contains name of all the topics which are present in train directory
	topics = os.listdir(path) 
	
	#Calculate likelihood  probability of word given topic
	#For a given topic, count the frequency of each words
	#Probability of a word in a given topic is - 
	#frequency of word over total number of words appeared in that topic
	
	print "learning started ..."
	print "number of topics -- ",len(topics)
	s = time.time()
	for each_topic in topics:
		print "learning %s topic"%(each_topic.upper())
		s1=time.time()
		word_prob ={}
		words = cleandata(convert_to_lower(readFiles(path+'/'+each_topic)))
		word_prob = dict(Counter(words))
		word_prob = dict((key,math.log(float(value)/len(words),2))for key,value in word_prob.items())
		likelihood[each_topic] = word_prob
		print "learning %s got completed in"%(each_topic.upper()),(time.time()-s1),"secs"
		print "*********"*20
	print "learning all topics completed in ",(time.time()-s),"secs"
	return likelihood