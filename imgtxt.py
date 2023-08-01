#!/usr/bin/python
# version 1.0.00
"""
Script to change img tags to img ids
Call it as a script
"""
#Import areas

import os
import sys
import re
import fileinput

# Variables definition
NEWSFILE = "C:\\AXIAR\\formfont\\news\\default.html"
TMPNEWS = "C:\\AXIAR\\formfont\\news\\news.html"
NPATH = 'C:\\AXIAR\\formfont\\news\\images'
IMGPATH = []

# function calls
def main():
	f1 = open(NEWSFILE, 'r')
	f2 = open(TMPNEWS, 'w')

	id = 1
	for line in f1:
		if "<img " in line:
			words = line.split()
			#print words
			# get the word for img source
			ftext = ""
			for item in words:
				if "src=" in item:
					#print "item", item
					#replace image name with ID call
					#cid:imageId1
					txtid = "src=cid:imageId" + str(id)
					#print txtid
					lstImages(item)
					ftext = ftext + " " + txtid
				else:
					ftext = ftext + " " + item
			f2.write(ftext)
			id += 1
		else:
			f2.write(line)

	f1.close()
	f2.close()

	# print final list of documents as standard output
	fimages = ""
	for paths in IMGPATH:
		if fimages == "":
			fimages = paths + ","
		else:
			fimages = fimages + paths + ","

	#print "last character", fimages[len(fimages) - 1]     
	if fimages[len(fimages) - 1] == ",":
		fimages = fimages[:len(fimages) - 1]

	sys.stdout.write(fimages)

def lstImages(lfile):
	fname = lfile[lfile.find("/") + 1:]
	xpath = NPATH + "\\" + fname
	xpath = xpath.replace("\"", "")
	IMGPATH.append(xpath)
	#print "image path", IMGPATH

#main call
if __name__ == "__main__":
	main()
