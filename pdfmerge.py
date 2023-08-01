#!/usr/bin/python
# version 7.1.01
"""
Script to process pdf files and merge into one
Call it from a script
"""
#Import areas
from PyPDF2 import PdfFileMerger, PdfFileReader
import sys
import os
import math

# function calls
def main():
	if (len(sys.argv) != 4):
		print("usage: python pdfmerge.py input_file1 input_file2 output_file")
		sys.exit(1)
	
	#print ("pdfmerge input " + sys.argv[1] + " " + sys.argv[2])
	merger = PdfFileMerger()
	
	input1 = PdfFileReader(open(sys.argv[1], "rb"))
	input2 = PdfFileReader(open(sys.argv[2], "rb"))
	outputfile = sys.argv[3]
	merger.append(input1)
	merger.append(input2)
	
	merger.write(outputfile)
	#print("done.")

#main call
if __name__ == "__main__":
	main()

