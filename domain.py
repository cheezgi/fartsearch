from urllib.parse import urlparse

#domain name "arst.com"
def get_domain_name(url):
	try: #http://www.google.com/arst.html
		results = get_sub_domain_name(url).split('.')
		return results[-2] + '.' + results[-1]
	except:
		return ''

#full domain name "www.arst.com"
def get_sub_domain_name(url):
	try:
		return urlparse(url).netloc
	except:
		return ''
