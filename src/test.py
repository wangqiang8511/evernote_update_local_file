#!/usr/bin/env python
#-*- coding: utf-8 -*-

""" Test of evernote api.
"""

from evernote_api import *

def test_list_note():
    client = get_client()
    notebook = get_notebook(client, "MyShortcuts")
    notelist = list_notes(client, notebook)
    for note in notelist:
        print note.content


def test_list_notebook():
    client = get_client()
    list_notebook(client)


def test_get_notebook():
    client = get_client()
    notebook = get_notebook(client, "MyShortcuts")
    print notebook.name
    pass

def test_create_note():
    client = get_client()
    notebook = get_notebook(client, "MyShortcuts")
    notebook = get_notebook(client, "MyShortcuts")
    notelist = list_notes(client, notebook)
    create_note(client, notebook, "src/evernote_api.py", "evernote api script attachment", \
                ["test", "python"], notelist)

if __name__ == "__main__":
    #test_list_note()
    #test_list_notebook()
    test_create_note()
    #test_get_notebook()
    pass

