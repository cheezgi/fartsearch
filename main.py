#functions used for crawling websites
import os
import re
import sys

if 'spider' not in sys.modules:
	print('Due to a freak accident, this is not the entry point to fartsearch.')
	print('You are looking for teast.py: python run.py projectName URL')

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
		file.write(data + '\n')

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
