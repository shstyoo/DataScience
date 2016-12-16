import numpy as np

class imdb_data():
	
	# Get imdb data from file
	def getimdbdata(self, filename):
		# Open file given in filename and parse the csv file
		name = filename
		import csv
		csv_list = []
		with open(name, 'rb') as csvfile:
		    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
		    for row in reader:
		        csv_list.append(row)
		return(csv_list)

	# Set imdb values to discretizable lists, the list of indexes will grab those indexes only
	def setvalues(self, csv_list, indexlist):
		# Remove the initial list that contains the headers and put into their own value
		headers = csv_list.pop(0)
		# Get select indexes only
		biglist = []
		for item in csv_list:
			templist = []
			for i in indexlist:
				templist.append(item[int(i)])
			biglist.append(templist)
		return(biglist)
