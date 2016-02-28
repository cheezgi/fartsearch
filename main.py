#search the web for farts (other keywords?)
#python 3.5.1
#thanks to bucky for the tutorial
#multithreaded(?) web development in the future?
#thanks to bucky roberts for framework
import os
import argparse
import re
import sys

#todo - move to entry point
#current target is a raspberry pi on my network for testing purposes
#get target from command line
#parser = argparse.ArgumentParser(description = 'Crawl the web for farts')
#parser.add_argument('target', metavar = 'target', type = str, help = 'Target website')
#args = parser.parse_args()
#try:
#target = (re.split('/', args.target, 0, 0))[2]
#except IndexError:
#	print('\nfartsearch: search the web for farts')
#	print('\nusage:')
#	print('python main.py target')
#	sys.exit()

target = '192.168.1.241'
class KillMe:
	def __init__(self, target):
		self.target = target
args = KillMe('http://192.168.1.241/')

print('')
print('searching for farts in ' + target)
print('~~~~~~~~~~~~~~~~~~~~~~~' + '~'*len(target))

#each crawled website (page?) is a seperate folder
def create_project_dir(directory):
	if not os.path.exists(directory):
		print('new directory for ' + directory)
		os.makedirs(directory)

#crawler queue
def create_data_files(project_name, base_url):
	print('new project files for ' + project_name)
	queue = project_name + '/queue.txt' #file paths in a new directory
	crawled = project_name + '/crawled.txt'
	if not os.path.isfile(queue): #check for files exist
		write_file(queue, base_url)
	if not os.path.isfile(crawled):
		write_file(crawled, '')

#create a new file
def write_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()

#add data to existing file
def append_to_file(path, data):
	with open(path, 'a') as file:
		file.write(data, '\n')

#delete contents of a file
def delete_file_contents(path):
	with open(path, 'w'):
		pass

#convert a file to a set
def file_to_set(file_name):
	results = set()
	with open(file_name, 'rt') as f:
		for line in f:
			results.add(line.replace('\n', ''))
	return results

#convert set to file with newlines
def set_to_file(links, filea):
	delete_file_contents(filea)
	for link in sorted(links):
		append_to_file(filea, link)

#initialize project if not exists
create_project_dir(target)
create_data_files(target, args.target)
