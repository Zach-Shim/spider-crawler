# this class parses data from an html page

from html.parser import HTMLParser
from urllib import parse

# inhertied from HTMLParser
# HTMLParser allows us to not make custom parser code
class LinkFinder(HTMLParser):

    # overloaded method
    # (constructor) initializes base url, page url, and makes links an empty set
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()
    
    # overloaded method
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    # abstract method
    def error(self, message):
        pass

