""" This module cleans, and removes any special characters,
	brackets, and tags from the dataset """
import re

def convert_to_lower(data):
    lower = []
    for d in data:
        lower.append(d.lower())
    return lower

	
def cleandata(file_folder):
	clean_files = []
	# Cleaner_1 removes HTML Tags
	for f in file_folder:
		cleaner_1 = re.compile('<[^<]+?>')
		clean_text_1 = re.sub(cleaner_1, '', f)
		
	# Cleaner_2 removes special characters
		cleaner_2 = re.compile('[!&@:;]')
		clean_text_2 = re.sub(cleaner_2, '', clean_text_1)
		
	# Cleaner_3 removes all types of brackets
		clean_text_3 = re.sub('[[]]', '', clean_text_2)
		clean_text_4 = re.sub('[()]', '', clean_text_3)
		clean_text_5 = re.sub('[<>]', '', clean_text_4)
		clean_text_6 = re.sub('[{}]', '', clean_text_5)
		clean_text_7 = re.sub('[_-]', '', clean_text_6)
		clean_text_8 = re.sub('["]', '', clean_text_7)
		clean_text_9 = re.sub("[']", '', clean_text_8)
		clean_text_10 = re.sub('[.,]', '', clean_text_9)
		clean_text_11 = re.sub('[*=]', '', clean_text_10)
		clean_text_12 = re.sub('[/]', '', clean_text_11)
		clean_text_13 = re.sub('#', '', clean_text_12)
		clean_text_14 = re.sub('%', '', clean_text_13)
		clean_text_15 = re.sub('[?]', '', clean_text_14)
		clean_text_16 = re.sub('[~]', '', clean_text_15)
		clean_text_17 = re.sub('[|]', '', clean_text_16)
		clean_text_18 = re.sub('[\t]', ' ', clean_text_17)
		clean_text_19 = re.sub('[^a-zA-Z]','',clean_text_18)
		clean_files.append(clean_text_19)
	words =  [value for value in clean_files if value != '']
	stopwords = [u'i', u'me', u'my', u'myself', u'we', u'our', u'ours', u'ourselves',\
				u'you', u'your', u'yours', u'yourself', u'yourselves', u'he', u'him', \
				u'his', u'himself', u'she', u'her', u'hers', u'herself', u'it', u'its',\
				u'itself', u'they', u'them', u'their', u'theirs', u'themselves', u'what',\
				u'which', u'who', u'whom', u'this', u'that', u'these', u'those', u'am',\
				u'is', u'are', u'was', u'were', u'be', u'been', u'being', u'have', u'has',\
				u'had', u'having', u'do', u'does', u'did', u'doing', u'a', u'an',  u'the',\
				u'and', u'but', u'if', u'or', u'because', u'as', u'until', u'while', u'of',\
				u'at', u'by', u'for', u'with', u'about', u'against', u'between', u'into',\
				u'through', u'during', u'before', u'after', u'above', u'below', u'to', u'from',\
				u'up', u'down', u'in', u'out', u'on', u'off', u'over', u'under', u'again',\
				u'further', u'then', u'once', u'here', u'there', u'when', u'where', u'why',\
				u'how', u'all', u'any', u'both', u'each', u'few', u'more', u'most', u'other',\
				u'some', u'such', u'no', u'nor', u'not', u'only', u'own', u'same', u'so',\
				u'than', u'too', u'very', u's', u't', u'can', u'will', u'just', u'don',\
				u'should', u'now', u'd', u'll',	u'm', u'o', u're', u've', u'y', u'ain', u'aren',\
				u'couldn', u'didn', u'doesn', u'hadn', u'hasn', u'haven', u'isn', u'ma', u'mightn',\
				u'mustn', u'needn', u'shan', u'shouldn', u'wasn', u'weren', u'won', u'wouldn']
	return [w for w in words if not w in stopwords]