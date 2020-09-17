Mulitthreaded Web Crawler

I created this web crawler for the website https://salon074.com but it can also work for most 
other websites with some specific configuring.
With this web crawler you have the options to: 
1. Create a sitemap for your main site page
2. Create a custom search engine for your website 
3. Locate and manipulate any information (collect or anaylze data) you find on webpages

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

What is the difference between a web scraper and a web crawler?
Crawling, by definition, always implies the web. 
A crawler’s purpose is to follow links to reach numerous pages and analyze their meta data and content. 
Scraping is possible out of the web. For example you can retrieve some information from a database. 
Scraping is pulling data from the web or a database.

BFS Algorithm
I implemented this web crawler using a BFS (breadth-first search) algorithm because of the relative shallow
depth of the links on the website. If I were to a much larger crawl, then I may consider using a DFS algorithm,
especially if I am looking for a singular website to scrape, and implement a depth limit to avoid infinite loops.
