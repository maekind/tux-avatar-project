# -*- coding: utf-8 -*-
#!/usr/bin/env python3

""" File that generates the assets file """

import json
import os

def walk(root):
    """ Method to walk throught the given folder """
    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        # yield every filename to updload
        for filename in filenames:
            #print(os.path.join(dirpath, filename))
            files.append(filename)
        # call the method recursively for the subfolders
        for dirname in dirnames:
            walk(os.path.join(dirpath, dirname))

    return files

def main():
    """ Main method """

    extensions = ['png', 'jpg']

    filenames = walk('.')

    base_url = "https://img.tux-avatar.com/"
    json_files = []

    for filename in sorted(filenames):
        if [ extension for extension in extensions if extension in filename]:
            json_files.append({ 'name': filename, 'url': base_url + filename })

    json_file = 'urls.json'
    with open(json_file, 'w') as f:
        f.write(json.dumps(json_files))

if __name__ == "__main__":
    main()
