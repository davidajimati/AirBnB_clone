#!/usr/bin/python3

'''
Init file to link the modules together
'''

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
