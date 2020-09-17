# spider.py
# we have links in a waiting list (queue), the spider will grab one link at a time and then connect to that page
# Once its connected, it will grab the html souce code and it will put it into a LinkFinder object which will return all the links in a set
# Once the links are returned, it will add the links to the waiting list
# Once the page is crawled, the current url is moved from the waiting page (queue) file to the crawled file

from urllib.request import urlopen      # module that allows us to connect web pages from python
from link_finder import LinkFinder      
from general import *                   
from domain import *

class Spider:

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

    # Description:   Creates directory and files for project on first run and starts the spider
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    # Description:   Updates user display, fills queue and updates files
    @staticmethod
    def crawl_page(thread_name, page_url):
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

    # Description:   converts raw response data into readable information and checks for proper html formatting
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

    # Description:   adds new found links that are not in the queue and have not been crawled
    @staticmethod
    def add_links_to_queue(links):
        for url in links:
            if (url in Spider.queue) or (url in Spider.crawled):
                continue
            if Spider.domain_name != get_domain_name(url):       # limit crawling to domain and not the rest of the internet
                continue
            Spider.queue.add(url)

    # Description:   update project files (queue.txt and crawled.txt)
    @staticmethod
    def update_files():
        set_to_file(Spider.queue, Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
