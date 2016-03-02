import sys
import threading
import argparse
from queue import Queue
from spider import Spider
#from domain import
from general import *

parser = argparse.ArgumentParser(description = 'Crawl the web for farts')
parser.add_argument('project_name', metavar = 'project_name', type = str, help = 'Project name, must be valid filename')
parser.add_argument('base_url', metavar = 'base_url', type = str, help = 'Target website URL')
parser.add_argument('-t', '--threads', metavar = 'threads', type=int, help='Number of threads to use')
args = parser.parse_args()

#constants
PROJECT_NAME = args.project_name
HOMEPAGE = args.base_url
try:
	DOMAIN_NAME = args.base_url.split('/')[2]
except IndexError:
	print('Invalid URL: must contain trailing / e.g.')
	print('http://www.example.com/')
	sys.exit()
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
if args.threads != 4:
	NUMBER_OF_THREADS = args.threads
	print('Using ' + str(NUMBER_OF_THREADS) + ' threads')
else:
	NUMBER_OF_THREADS = 4
queue = Queue()

print('\nsearching for farts in ' + args.base_url)
print('~~~~~~~~~~~~~~~~~~~~~~~' + '~'*len(args.base_url))

Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME) #spider 1

#create worker threads (dead on exit main)
def create_workers():
	a = 0
	for a in range(NUMBER_OF_THREADS):
		t = threading.Thread(target=work)
		t.daemon = True
		t.start()

#next job in queue
def work():
	while True:
		url = queue.get()
		Spider.crawl_page(threading.current_thread().name, url)
		queue.task_done()

#every queued link is a new job
def create_jobs():
	for link in file_to_set(QUEUE_FILE):
		queue.put(link)
	queue.join()
	crawl()

#check for items in queue
def crawl():
	queued_links = file_to_set(QUEUE_FILE)
	if len(queued_links) > 0:
		print(str(len(queued_links)) + ' remaining')
		create_jobs()

create_workers()
crawl()
