# spider.py
# we have links in a waiting list (queue), the spider will grab one link at a time and then connect
# to that page. ONce its connected, it will grab the html souce code and it will put it into a 
# LinkFinder object which will return all the links in a set
# Once the links are returned, it will add the links to the waiting list
# Once the page is crawled, the current url is moved from the waiting page (queue) file to the crawled file

from urllib.request import urlopen      # module that allows us to connect web pages from python
from link_finder import LinkFinder      # from the link_finder.py file
from general import *                   # from the link_finder.py file, import all housecleaning methods
from domain import *

class Spider:
    # a class variable is a special type of variable that is shared across all instances
    # all spiders will share these class variables to know what is being crawled and what is queued
    # any spider across all instances of spider objects can access or change these variables
    project_name = ''       # user defined
    base_url = ''           # the url of the home page we want to crawl
    domain_name = ''
    queue_file = ''         # in case the program shuts down or some unkonwn error causes the web crawl to stop, the queued links will all be stored in this queue text file
    crawled_file = ''       # ^ same case as queue file except for crawled links ^
    queue = set()           # stores a set of links to crawl
    crawled = set()         # stores crawled links

    def __init__(self, project_name, base_url, domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('First Spider', Spider.base_url)       # connect to a webpage and gather links/crawl

    # the first spider is a special case because it has to create a directory and the queue and crawled files
    # the queue file should have one url, and the crawled file should be empty
    # creates directory and files for project on first run and starts spider
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    # takes in a url and will connect to that page and collect all links
    # if the page has not been crawled, once it has the all the links, it will add them to a waiting list (queue)
    # once all the links are in the waiting list, the page has been crawled and will be added to the crawled set
    # once this process is done, update the data files to have an up to date copy of links
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
            # returns a set of all univisited links to put in the queue; add links to the queue
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            # update queue and crawled sets
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            # update data files; converts both sets to files
            Spider.update_files()

    # connects to a site, takes html, converts it to a readable format, passes it to linkfinder to find all 
    # the urls on the page, return a set of all urls on page
    @staticmethod
    def gather_links(page_url):
        html_string = ''
        try:        
            response = urlopen(page_url)                             # open web page
            if 'text/html' in response.getheader('Content-Type'):    # double check it is an html site
                html_bytes = response.read()                         # byte data, need to convert to html strings ('human')
                html_string = html_bytes.decode("utf-8")
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except Exception as e:
            print(str(e))
            return set()
        return finder.page_links()


    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            if Spider.domain_name != get_domain_name(url):       # will keep the crawling grounded to the domain and not the rest of the internet
                continue
            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
