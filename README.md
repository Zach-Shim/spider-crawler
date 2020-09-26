# Overview

> This is a simple, multi-threaded website crawler written in Python that is part of an open source search engine.
Currently, the main functionality of the crawler is to only gather links.
<!-- toc -->

- [What is a Web Crawler?](#heading-1)
- [How does this web crawler work?](#heading-2)
- [How you can contribute](#heading-3)
- [Notes](#heading-4)

## What is a Web Crawler?
A crawler, or spider, is an internet bot indexing and visiting every URLs it encounters. Its goal 
is to visit a website from end to end, know what is on every webpage and be able to find the location 
of any information. 
When a website is online, those crawlers will visit it and read its content to display it in the relevant 
search result pages. 

## How does this crawler work?
Starting from the root URL or a set of entries, the crawler will create a directory and fetch the 
webpages and find other URLs to visit, called seeds, on this page. All the seeds found on this page 
will be added onto a list (queue) of URLs to be visited. This list is called the horizon. The 
crawler organises the links in two threads: ones to visit (in the queue), and already visited ones (crawled). 
It will keep visiting the links until the horizon (queue) is empty. 

![alt text](https://github.com/Zach-Shim/spider-crawler/blob/master/multi-thread-spiders.png)

## Multithreading
Multithreading is a way of achieving a program that can multitask.

In computing, a process is an instance of a computer program that is being executed. Any process has 3 basic components:
1. An executable program.
2. The associated data needed by the program (variables, work space, buffers, etc.)
3. The execution context of the program (State of process)
A thread is an entity within a process that can be scheduled for execution. Also, it is the smallest unit of processing that can be performed in an OS (Operating System).

Python provides built-in support for Multithreaded programming.
Multithreading is defined as the ability of a processor to execute multiple threads concurrently.

## How can you get started?
1. I still need to implement a user interface since I am hard coding a website for the crawler to run in main.py
2. Currently, the main functionality of the crawler is to only gather links. Any analytic processing, data harvesting, and search algorithms must be created as separate programs. I am planning on implementing either a custom search engine for the salon website or a search algorithm for web scraping

## Notes
Note 1: This is part of an open source search engine. The purpose of this tool is to gather links only. The analytics, data harvesting, and search algorithms are being created as separate programs.

Note 2: This code was heavily influenced by thenewboston's online tutorial series on creating a web crawler which can be found on:  
https://www.youtube.com/watch?v=nRW90GASSXE&list=PL6gx4Cwl9DGA8Vys-f48mAH9OKSUyav0qand 
as well as his open source code found on his github.
Please support him by visiting his github and website: https://thenewboston.com/

Note 3: I created this web crawler as a side project with the intention of creating a sitemap and/or search engine for the business https://salon074.com 
