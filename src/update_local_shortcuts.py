#!/usr/bin/env python
#-*- coding: utf-8 -*-

""" Update local shortcuts to evernote.
"""

import os

from evernote_api import *

def update(root):
    """ Update shortcuts in root dir to evernote.
    """
    client = get_client()
    notebook = get_notebook(client, "DesktopShortcuts")
    # if not found, create a new one
    if not notebook:
        create_notebook(client, "DesktopShortcuts")
        notebook = get_notebook(client, "DesktopShortcuts")
    notelist = list_notes(client, notebook)
    print notelist
    rootlen = len(root)
    for root, dirs, files in os.walk(root):
        for file in files:
            filename = os.path.join(root, file)
            shortname = filename[rootlen:]
            shortname = os.path.splitext(shortname)[0]
            title = shortname.replace('/', ' ')
            title = title.replace('_', ' ')
            print title
            tags = title.split(" ")
            tags = list(set(tags))
            print tags
            create_note(client, notebook, filename, title, tags, notelist)


if __name__ == "__main__":
    update("/home/wolfking/shortcuts/")
    pass
