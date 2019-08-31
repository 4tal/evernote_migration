import hashlib
import binascii
import evernote.edam.userstore.constants as UserStoreConstants
import evernote.edam.type.ttypes as Types
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec
from evernote.edam.type.ttypes import NoteSortOrder
import os
import io
import xml.dom.minidom as xml_parser

import hashlib

import os
from time import strptime
from evernote.api.client import EvernoteClient
from dotenv import load_dotenv

load_dotenv(dotenv_path=f'{os.environ.get("PWD")}/.env')

class Note:
    def __init__(self, guid):
        self.guid = guid


client = EvernoteClient(token=os.environ.get('EVERNOTE_TOKEN'))
userStore = client.get_user_store()
user = userStore.getUser()

filter_note = NoteFilter()
note_store = client.get_note_store()
notebooks = note_store.listNotebooks()

tag_by_guid = {}
tags = note_store.listTags()
for tag in tags:
    tag_by_guid[tag.guid] = tag.name

notes_meta = note_store.findNotes(filter_note, 0, 10)
for note_meta in notes_meta.notes:
    note = note_store.getNote(note_meta.guid, True, True, True, True)

    parsed_note = Note(note_meta.guid)
    parsed_note.title = note.title
    parsed_note.content = note.content
    parsed_note.tags = []
    for tag_guid in note.tagGuids:
        parsed_note.tags.append(tag_by_guid[tag.guid])

    print('End')









