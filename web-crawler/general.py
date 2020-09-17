# spider.py
import os allows us to make directories(folder)
import os


# Description:    each website you crawl is a separate project(folder)
# Preconditions:  directory is a user given name for a project/folder
# Postconditions: a new directory is created
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)

        
# Description:    create queue and crawled files (if not yet created); keeps track of the currently queued and crawled links as to not repeat reading over pages
# Preconditions:  project_name is a user given name for a project/folder (usually same as domain)
#                 base_url is the url of page that we start crawling on (usually home page)
# Postconditions: queue.txt and crawled.txt have been created on your local harddrive
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, 'crawled.txt')
    if not os.path.isfile(queue):        # does this file exist
        write_file(queue, base_url)      # create file with file path and data
    if not os.path.isfile(crawled):
        write_file(crawled, '')

        
# Description:    create a new file and write to it
# Preconditions:  path is a local path to a txt file
#                 data is the text you want to write in a file
# Postconditions: the path txt file has had data written to it
def write_file(path, data):
   with open(path, 'w') as f:
       f.write(data)

        
# Description:    add data onto an existing file
# Preconditions:  path is a local path to a txt file
#                 data is the text you want to append to a file
# Postconditions: the path txt file has had data appended to it
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')

        
# Description:    delete the contents of a file
# Preconditions:  path is a local path to a txt file
# Postconditions: the txt file path is deleted
def delete_file_contents(path):
    open(path, 'w').close()

    
# Description:    read a file and convert each line to set items to avoid duplication of websites
# Preconditions:  file_name is the name of the file you are conerting links to (either queue.txt or crawled.txt)
# Postconditions: return a set of links from a file (queue.txt)
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

# Description:    iterate through a set, each item in set will be a new line in file
# Preconditions:  links is a set containing zero or more website urls
#                 file_name is the name of the file you are conerting links to (either queue.txt or crawled.txt)
# Postconditions: either queue.txt or crawled.txt has been updated with new links
def set_to_file(links, file_name):
    with open(file_name, 'w') as f:
        for l in sorted(links):
            f.write(l + '\n')

