# spider-crawler

This is an open source, multi-threaded website crawler written in Python.

Note 1: This is part of an open source search engine. The purpose of this tool is to gather links only. The analytics, data harvesting, and search algorithms are being created as separate programs.

I created this web crawler with the intention of creating a sitemap for the business https://salon074.com 

What is a Web Crawler?
A crawler, or spider, is an internet bot indexing and visiting every URLs it encounters. Its goal 
is to visit a website from end to end, know what is on every webpage and be able to find the location 
of any information. 
When a website is online, those crawlers will visit it and read its content to display it in the relevant 
search result pages. 

How does it work?
Starting from the root URL or a set of entries, the crawler will create a directory and fetch the 
webpages and find other URLs to visit, called seeds, on this page. All the seeds found on this page 
will be added onto a list (queue) of URLs to be visited. This list is called the horizon. The 
crawler organises the links in two threads: ones to visit (in the queue), and already visited ones (crawled). 
It will keep visiting the links until the horizon (queue) is empty. 

Because the list of seeds can be very long, the crawler has to organise those following several 
criterias, and prioritise which ones to visit first and revisit. To know which pages are more important 
to crawl, the bot will consider how many links go to this URL, how often it is visited by regular users.
