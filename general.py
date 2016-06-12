import os


# each website you craw is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating project " + directory)
        os.makedirs(directory)

# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = project_name+"/queue.txt"
    crawled = project_name+"/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, "")

# Create a new file
def write_file(path, data):
        with open(path, "wb") as f:
            f.write(data.encode("utf-8"))

# Add data onto an existing file
def append_to_file(path, data):
    # u'ä, Δ, Й, ק, ‎ م, ๗, あ, 叶, 葉, and 말.'
    with open(path, "ab") as file:
        file.write((data+"\n").encode("utf-8"))

# Delete the contents of a file
def delete_file_contents(path):
    with open(path, "wb"):
        pass

# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    with open(file_name,"rt") as f:
        for line in f:
            results.add(line.replace("\n", ""))
    return results

# Iterate through a set, each item will be a new line in the file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file, link)

