"""
	Topic classification - 
	
	On given set of test data which is present in Testing directory,
	the program first trains it's naive bayes model to calculate 
	likelihood of each word for a given topic. 
	After calculating likelihood, the program tests it's accuracy
	of testing data present in test directory.
	For each file in the test directory, it uses max appriori method
	to determine the topic of the file.
	
	Run program py ruuning command - 
	python doc_claasification.py
"""

import os
from training_module import train
from testing_module import test

if __name__ == "__main__":
	#Save root path in a avriable
	org_path = str(os.getcwd())
	
	#Calculate likelihood of each word for given topic
	#Train your model for bayes net
	likelihood = train()
	
	#Test the model on test data
	test(org_path, likelihood)
				

