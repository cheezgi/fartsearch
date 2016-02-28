#spider class object: handles queue stuff and whatnot
from urllib.request import urlopen
from link_finder import LinkFinder
from main import *

#spider class
class Spider:
	#class variables - multithreading purposes
	project_name = ''
	base_url = ''
	domain_name = ''
	queue_file = ''
	crawled_file = ''
	queue = set()
	crawled = set()
	def __init__(self):

