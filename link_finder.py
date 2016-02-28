#find links
from html.parser import HTMLParser
from urllib import parse

#link finder class
class LinkFinder(HTMLParser):
	def __init__(self, base_url, page_url):
		super().__init__()
		self.base_url = base_url
		self.page_url = page_url
		self.links = set()
	
	#search for links <a>
	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			print('found link')
			for (attribute, value) in  attrs:
				if attribute == 'href':
					#handles relative urls
					url = parse.urljoin(self.base_url, value)
					self.links.add(url)

	def page_links(self):
		return self.links

	def error(self, message):
		pass

finder = LinkFinder()
