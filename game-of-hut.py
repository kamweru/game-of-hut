#################################################
# 			Game of hut (game-of-hut) 			#
# 				  Done in python                #
#			   Created by notrexbias 			#
#	 			  www.kamweru.com 				#
#			  notrexbias@outlook.com 			#
#	 											#
# 			##########################			#
#	 											#
#	This program is free for copying and use. 	#
#	I take no responsibility for any harm or  	#
#	damage that this program can cause on use. 	#
#################################################

import random, os, sys, json # importing libraries to be used
# A list of lines from one point to another
hutline = [
	["A", "B"],
	["B", "C"],
	["C", "D"],
	["D", "E"],
	["E", "A"],	
	["E", "B"],	
	["A", "D"],	
	["D", "B"]
]

hutpath = [] # Holds the temporary path 
points = [0, 1] # A list of two points indices that can be chosen randomly

# Takes a point and searches for lines with the point as part of them 
# and puts all those lines in an list and returns one line chosen randomly
def getnextline(startpoint):
	pathlist = []
	for x in range(0, len(hutline)):
		if startpoint in hutline[x]:
			if hutline[x] not in hutpath:
				pathlist.append(hutline[x])
	if pathlist:
		return random.choice(pathlist)
	else:
		os.execl(sys.executable, sys.executable, *sys.argv) # restarts the execution of code

# Takes two lists and returns a list of the matching elements 
def match(s, t):
	return list(set(s) & set(t))

# Takes a filename and returns true if file is empty, false otherwise
def fileisempty(filename):
	return os.stat(filename).st_size == 0

# a loop to create a list of lines that make up a whole path
for x in range(0,len(hutline)):
	if not hutpath:	
		firstline = random.choice(hutline)
		hutpath.append(firstline)
	else:
		if len(hutpath) == 1:
			randpoint = random.choice(points)
			newline = getnextline(hutpath[0][randpoint])
			hutpath.append(newline)
		else:
			lastpoint = match(hutpath[-2], hutpath[-1])[0]
			nextpathindex = hutpath[-1].index(lastpoint)
			if nextpathindex == 1:
				nextpointindex = 0
			else:
				nextpointindex = 1
			newline = getnextline(hutpath[-1][nextpointindex])
			hutpath.append(newline)
	# print(hutpath) # This shows paths as they are being created, 
					 # both the complete ones (successes) and non-complete ones (fails)

if fileisempty('paths.json'):
	data = {"paths" : []}
	with open('paths.json', 'w') as outfile:
		data['paths'].append(hutpath)
		json.dump(data, outfile) # dumps data into json file as a dictionary
	os.execl(sys.executable, sys.executable, *sys.argv) # restarts the execution of code
else:
	with open('paths.json') as json_file:
		file_data = json.load(json_file) # reads data from json file and loads it into a variable
		if hutpath not in file_data['paths']: # if the hutpath is not in the file_data, 
			file_data['paths'].append(hutpath) # append it to file_data
			with open('paths.json', 'w') as outfile:
				file_data['paths'].sort() # sort the lists
				json.dump(file_data, outfile) # dump the data into the file
				print(len(file_data['paths'])) # Prints the current size of the list that holds the paths 
				# hence displaying how many paths have been found				
	os.execl(sys.executable, sys.executable, *sys.argv)