# Description: A program that analyzes any number of corpi into any number of n-grams to create sentences.
#
# Author: Austin Goddamn Gordon
#
# Date: I wish ...

import sys
import nltk

# TODO:
# 2: Split input file/s into sentences and write to a file
# 3: read from sentence file and find n-grams
# 4: get probability of n-grams
# 5: use rng to construct sentence based on n-gram probabilities

# correct number of cmd line args?
if len(sys.argv) < 4:
	sys.exit("USAGE: ngram.py <ngram> <sentences> <input file> <input file> ...")

# first arg must be an int 1 - 3
if not str(sys.argv[1]).isdigit() or int(sys.argv[1]) < 1 or int(sys.argv[1]) > 3:
	sys.exit("ERROR: ngram must be an integer 1 - 3")

# second arg must be an int
if not str(sys.argv[2]).isdigit():
	sys.exit("ERROR: sentences must be an integer")

# remaining args are files to open
i = 3	# file list starts at the third parameter, continue looping till end of file list
while i < len(sys.argv):
	try:
		file_content = open(str(sys.argv[i])).read()	# open the input file and read it
		# write each sentence to a separate file
	except IOError:
		print ("Error opening file ", str(sys.argv[i]))
		sys.exit(1)
	i += 1

tokens = nltk.word_tokenize(file_content)	# break the file into tokens
print (tokens)	# output said tokens
