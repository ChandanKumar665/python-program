import urllib
from zipfile import *
import csv
import os
zipurl=input('Please enter url to download file: ')
testfile = urllib.URLopener()
testfile.retrieve(zipurl, ".")
f_name=zipurl.split('/')[-1]
f=ZipFile(f_name,'r',ZIP_STORED)
f.extractall()
filename=f.namelist()
field=[]
row=[]
# print(len(l))
if len(filename)==1:
	with open(filename[0],'r') as csvfile:
		csvreader=csv.reader(csvfile)
		for r in csvreader:
			row.append(r)
		print(csvreader.line_num)
		# print(row)
	# field.append(row[0])
	# print(row[0])
	print(' '.join(x for x in row[0]))	
	for x in row[1:5]:
		for col in x:
			print(col,end=' ')
		print('\n')	
