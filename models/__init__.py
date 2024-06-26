#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

# Determine the type of storage based on the value of the 
#environment variable HBNB_TYPE_STORAGE
storage_type = os.getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
