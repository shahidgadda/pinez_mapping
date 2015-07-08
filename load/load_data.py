# Full path and name to your csv file
csv_file="/home/shahid/workspace/projects/products/media/csv/gadget.csv"
# Full path to your django project directory
project_home="/home/shahid/workspace/projects/products/"
picture = "/home/shahid/workspace/projects/products/media/images"

import sys,os
sys.path.append(project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'products.settings'


file_names = []  # List which will store all of the full filepaths.


    # Walk through the directory.
for files in os.listdir(picture):
	file_names.append(files)

from django.db import models
from machine.models import Gadgets

import csv
#with open(csv_file, "rU") as f:
#    Reader = csv.reader( (line.replace('\0','') for line in f), delimiter='\t', dialect='excel-tab' )
#dataReader = csv.reader(open(csv_file), dialect='excel-tab')
dataReader = csv.reader(open(csv_file), delimiter=',', quotechar='"')

for row in dataReader:
	print row[4]
	count = 0
	i = 0
	while i < len(file_names):
		if file_names[i] == row[4]:
			count = count+1
		i = i+1
	if count > 0:
		if row[0] != 'TITLE': # Ignore the header row, import everything else
			gadgets = Gadgets()
			gadgets.title = row[0]
			gadgets.description = row[1]
			gadgets.category = row[2]
			gadgets.price = row[3]
			gadgets.image = "static/pictures/"+row[4]
			gadgets.save()
	else:
		print "Tuple can't be uploaded "