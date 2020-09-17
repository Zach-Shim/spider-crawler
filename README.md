- [Heading](#heading)
  * [Sub-heading](#sub-heading)
    + [Sub-sub-heading](#sub-sub-heading)
- [Heading](#heading-1)
  * [Sub-heading](#sub-heading-1)
    + [Sub-sub-heading](#sub-sub-heading-1)
- [Heading](#heading-2)
  * [Sub-heading](#sub-heading-2)
    + [Sub-sub-heading](#sub-sub-heading-2)


# Heading levels

> This is a fixture to test heading levels
<!-- toc -->

## Heading

This is an h1 heading

### Sub-heading

This is an h2 heading

#### Sub-sub-heading

This is an h3 heading

## Heading

This is an h1 heading

### Sub-heading

This is an h2 heading

#### Sub-sub-heading

This is an h3 heading

## Heading

This is an h1 heading

### Sub-heading

This is an h2 heading

#### Sub-sub-heading

This is an h3 heading

This is a simple, multi-threaded website crawler written in Python that is part of an open source search engine.
Currently, the main functionaly of the crawler is to only gather links. Any analytic processing, data harvesting, and search algorithms must be created as separate programs.

What is a Web Crawler?
A crawler, or spider, is an internet bot indexing and visiting every URLs it encounters. Its goal 
is to visit a website from end to end, know what is on every webpage and be able to find the location 
of any information. 
When a website is online, those crawlers will visit it and read its content to display it in the relevant 
search result pages. 

How does this crawler work?
Starting from the root URL or a set of entries, the crawler will create a directory and fetch the 
webpages and find other URLs to visit, called seeds, on this page. All the seeds found on this page 
will be added onto a list (queue) of URLs to be visited. This list is called the horizon. The 
crawler organises the links in two threads: ones to visit (in the queue), and already visited ones (crawled). 
It will keep visiting the links until the horizon (queue) is empty. 

How can you get started?
I still need to implement a user interface since I am hard coding a website for the crawler to run in main.py


Because the list of seeds can be very long, the crawler has to organise those following several 
criterias, and prioritise which ones to visit first and revisit. To know which pages are more important 
to crawl, the bot will consider how many links go to this URL, how often it is visited by regular users.

Note 1: This is part of an open source search engine. The purpose of this tool is to gather links only. The analytics, data harvesting, and search algorithms are being created as separate programs.

Note 2: This code was heavily influenced by thenewboston's online tutotial series which can be found on:  
https://www.youtube.com/watch?v=nRW90GASSXE&list=PL6gx4Cwl9DGA8Vys-f48mAH9OKSUyav0qand 
as well as his open source code for website crawlers.
Please support him by visiting his github and website: https://thenewboston.com/

Note 3: I created this web crawler with the intention of creating a sitemap and/or search engine for the business https://salon074.com 
