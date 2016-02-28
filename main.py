#search the web for farts
import os
import sys

#each crawled website is a seperate folder
def create_project_dir(directory):
	if not os.path.exists(directory):
		print('new directory for ' + directory)
		os.makedirs(directory)

#teast I guess iunno
