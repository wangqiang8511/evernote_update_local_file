#!/usr/bin/env python
#-*- coding: utf-8 -*-

""" Working arround evernote
"""

import os
import binascii
import settings
from xml.sax.saxutils import escape
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types
import evernote.edam.notestore.ttypes as NoteStoreTypes
from evernote.api.client import EvernoteClient

# User your own token
auth_token = settings.auth_token
print auth_token

def get_client():
    return EvernoteClient(token=auth_token, sandbox=False)


def get_notebook(client, name):
    note_store = client.get_note_store()
    notebooks = note_store.listNotebooks()
    for n in notebooks:
        if n.name == name:
            return n
    return None

def list_notebook(client):
    note_store = client.get_note_store()
    notebooks = note_store.listNotebooks()
    for n in notebooks:
        print n.name

def create_notebook(client, name):
    noteStore = client.get_note_store()
    notebook = Types.Notebook()
    notebook.name = name
    notebook = noteStore.createNotebook(notebook)
    return notebook

def list_notes(client, notebook):
    filter = NoteStoreTypes.NoteFilter()
    filter.notebookGuid = notebook.guid
    noteStore = client.get_note_store()
    noteList = noteStore.findNotes(filter, 0, 1000)
    return noteList.notes

def get_note(noteList, title):
    for note in noteList:
        if note.title == title:
            return note
    return None

def create_note(client, notebook, filename, title, tags, noteList):
    """ Create a note from local file.
        If the title exists, do an update.
    """
    with open(filename, 'r') as f:
        file_content = f.read()
        noteBody = file_content
        noteBody = escape(noteBody)
        #noteBody = noteBody.replace("\n", "<br />")
        nBody = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        nBody += "<!DOCTYPE en-note SYSTEM \"http://xml.evernote.com/pub/enml2.dtd\">"
        nBody += "<en-note><pre>%s</pre></en-note>" % noteBody
        # Create note object
    note = get_note(noteList, title)
    noteStore = client.get_note_store()
    if note:
        note.content = nBody
        note.resources = []
        note = noteStore.updateNote(note)
    else:
        note = Types.Note()
        note.title = title
        note.content = nBody
        note.tagNames = tags
        note.notebookGuid = notebook.guid
        note.resources = []
        note = noteStore.createNote(note)
    pass


if __name__ == "__main__":
    main()
    pass
