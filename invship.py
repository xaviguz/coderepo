#!/usr/bin/python
# version 7.1.01
"""
Script to process stdin and return a modified stream
This script will modify the shipping attachment of an invoice
will incorporate the call to the form and paginate the file
"""
#Import areas
import sys,getopt

#function definition areas
#function to process incoming arguments
def main(argv):
	inputfile = ''
	outputfile = ''
	filetype = ''
	try:
		#print "get arguments"
		opts, args = getopt.getopt(argv,"hi:o:t:",["ifile=","ofile=", "otype="])
		#print "opts", opts
		#print "args"
	except getopt.GetoptError:
		print 'invship.py -i <inputfile> -o <outputfile> -t <doc type>'
		sys.exit(2)
	for opt, arg in opts:
		#print "arguments found"
		if opt == '-h':
			print 'invship.py -i <inputfile> -o <outputfile> -t<doc type>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
		elif opt in ("-t", "--otype"):
			filetype = arg
	
	if filetype == "ship":
		gen_ship(inputfile, outputfile, "ACC300S", "", False)
	elif filetype == "pay":
		gen_ship(inputfile, outputfile, "ACC300P", "", False)
	else:
		gen_ship(inputfile, outputfile, "ACC300", "ACC300C", True)

def gen_ship(ifile, ofile, overlay, contover, invoice):
	"""
	function to filter and paginate incoming file, into output file
	to concatenate to invoice.
	"""
	
	#Variable area
	line_count = 0
	page_count = 1
	#main process
	#Open incoming file
	data_file =  open(ifile, 'r')
	data = data_file.read()
	filter_file = open(ofile, 'w')
	data_lines = data.split('\n')
	data_file.close()
	for line in data_lines:
		#print "line information", line
		# first page, one form
		if page_count == 1 and line_count == 0:
			if invoice:
				filter_file.write(overlay + '\r\n')
			else:
				filter_file.write('\f' + overlay + '\r\n')
		#continuation pages different forms
		if ((line_count > 57) and (page_count == 1)) or ((line_count > 57) and (page_count > 1)):
			if invoice:
				filter_file.write('\f' + contover + '\r\n')
			else:
				filter_file.write('\f' + '\r\n') 
			line_count = 0
			page_count += 1
		else:
			line_count += 1
			if not (line == ""):
				filter_file.write(line + '\n')
	filter_file.close()

# end of function definition areas

if __name__ == '__main__':
	"""
	Main call to script
	"""
	#print "argv len is", len(sys.argv)
	if len(sys.argv) > 1:
		main(sys.argv[1:])
		exit()
	else:
		print 'invship.py -i <inputfile> -o <outputfile> -t <doc type>'
		exit(2)


