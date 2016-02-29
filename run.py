#fartsearch - crawl the web for farts. 2016 cheezgi
#Thanks to buckyroberts for the framework and hilarious videos outlining this project.
import sys
import re
import argparse
from spider import *

#get website from command line
parser = argparse.ArgumentParser(description = 'Crawl the web for farts')
parser.add_argument('project_name', metavar = 'project_name', type = str, help = 'Project name. Must be valid filename.')
parser.add_argument('base_url', metavar = 'base_url', type = str, help = 'Target website URL')
args = parser.parse_args()

try:
	print('\nsearching for farts in ' + args.base_url)
	print  ('~~~~~~~~~~~~~~~~~~~~~~~' + '~'*len(args.base_url))
	spid = Spider(args.project_name, args.base_url, (re.split('/', args.base_url, 0, 0))[2])
except IndexError:
	print('\nfartsearch: search the web for farts')
	print('\nusage:')
	print('python main.py target')
	sys.exit()
