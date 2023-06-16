# -*- coding: utf-8 -*-
#!/usr/bin/env python3

""" File that generates the assets file """

import argparse
import json
import os
from urllib.parse import quote, urljoin

__author__ = "Marco Espinosa"
__email__ = "marco@marcoespinosa.es"
__date__ = "16/06/2023"
__version__ = "1.2"
__development__ = False

__application_name__ = "Assets builder"

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

def get_arguments():  # pragma: no cover
    """ Method to retrieve application arguments """
    # Configure arguments
    parser = argparse.ArgumentParser(description=__application_name__)
    parser.add_argument('-v',
                        '--verbose',
                        help="Set verbose option",
                        dest="verbose",
                        required=False,
                        action='store_true')
    parser.add_argument('-p',
                        '--path',
                        help="Path to images folder",
                        dest='path',
                        metavar='STRING',
                        required=True)

    return parser

def main():
    """ Main method """

    # Only png images are allowed
    extensions = ['png']

    # Get application arguments
    parser = get_arguments()
    args = parser.parse_args()

    filenames = walk(args.path)

    base_url = "https://raw.githubusercontent.com/maekind/tux-avatar-project/main/images/"
    json_files = []

    for filename in sorted(filenames):
        if [ extension for extension in extensions if extension in filename]:
            json_files.append({ 'name': filename, 'url': urljoin(base_url, quote(filename)) })

    json_file = 'urls.json'
    with open(json_file, 'w') as f:
        f.write(json.dumps(json_files))

if __name__ == "__main__":
    main()
