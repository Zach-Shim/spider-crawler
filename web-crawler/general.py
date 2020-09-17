# import os allows us to make directories(folder)
import os

# each website you crawl is a separate project(folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)

# create queue and crawled files (if not created)
# keeps track of the currently queued links as to not repeat reading over pages
# every time the crawler finds a link, it will add it to the queue list
# once it goes to the page and crawls it, it will be added to the crawled list
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, 'crawled.txt')
    if not os.path.isfile(queue):        # does this file exist
        write_file(queue, base_url)      # create file with file path and data
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# create a new file
def write_file(path, data):
   with open(path, 'w') as f:
       f.write(data)

# add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

# delete the contents of a file
def delete_file_contents(path):
    open(path, 'w').close()

# read a file and convert each line to set items to avoid duplication of websites
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

# iterate through a set, each item in set will be a new line in file
def set_to_file(links, file_name):
    with open(file_name, 'w') as f:
        for l in sorted(links):
            f.write(l + '\n')

