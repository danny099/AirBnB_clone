#!/usr/bin/python3
"""instance for your application"""

from models.engine.file_storage import FileStorage


list_class = {'BaseModel': 'BaseModel', 'State': 'State', 'Amenity': 'Amenity',
              'Place': 'Place', 'Review': 'Review', 'User': 'User'}
storage = FileStorage()
storage.reload()
