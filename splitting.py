import glob
import csv

whichone = "comments"

files = glob.glob('Databases/*' + whichone + '.csv')

print(files)

allthings = []

for f in files:
	with open(f, 'rt', encoding = 'utf-8') as fin:
		fin = csv.reader(fin)
		headers = next(fin)
		data = [d for d in fin]
		allthings += data


# this writes out a CSV of all the submittions

with open('all' + whichone + '.csv', 'wt', encoding = 'utf-8') as fout:
	fout = csv.writer(fout)
	fout.writerow(headers)
	fout.writerows(allthings)

with open('all' + whichone + '.csv', 'rt', encoding = 'utf-8') as fin:
	fin = csv.reader(fin)
	headers = next(fin)
	data = [r for r in fin]



base = whichone + '/'
if whichone == "submissions":
	uniqueid = headers.index('postID')
	text_index = headers.index('postBody')
	for d in data:
		fname = d[uniqueid]
		text = d[text_index]
		with open(base + fname + '.txt', 'wt', encoding = 'utf-8') as fout:
			fout.write(text)
elif whichone == "comments":
	uniqueid = headers.index('postID')
	dateid = headers.index('date')
	text_index = headers.index('body')
	for d in data:
		post_id = d[uniqueid]
		date = d[dateid]
		fname = post_id + date
		text = d[text_index]
		with open(base + fname + '.txt', 'wt', encoding = 'utf-8') as fout:
			fout.write(text)
else:
	print("I don't know what that one is")

