#!/usr/bin/python

"""
Script to process stdin and return a modified stream
"""
#Import areas
import sys

if __name__ == '__main__':

	#Variable area
	line_count = 0
	page_count = 1
	the_end = False

	#main process
	for line in sys.stdin:
		# first page, one form
		if page_count == 1 and line_count == 0:
			sys.stdout.write("ACC200" + '\r\n')
		#continuation pages different forms
		if ((line_count > 59) and (page_count == 1)) or ((line_count > 59) and (page_count > 1)):
			sys.stdout.write('\f' + "ACC200C" + '\r\n')
			line_count = 0
			page_count += 1
		#check if total of accumulated invoices of statement
		#if "TOTAL ACCOUNT BALANCE" in line:
		#	sys.stdout.write("$$1" + line + "$$0" + '\r')
		#	line_count += 1
		# check if final age summary is in the page and parse a command to draw a box around it
		#$$S width, height, size of border/
		#elif "Aged Summary" in line:
			#line_count += 1
			#sys.stdout.write("$$S7.5,0.85,3/" + '\r\n')
			#sys.stdout.write("$$01" + '\t\t\t\t\t\t' + line)
		#elif "and over" in line:
			#sys.stdout.write("$$02" + line)
			#line_count += 1
			#the_end = True
		else:
			#if the_end:
				#sys.stdout.write("$$03" + line)
				#line_count += 1
			#else:
			line_count += 1
			sys.stdout.write(line)
    
	exit()

