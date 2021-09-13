import importlib

import os


BUCKET = os.getenv('FILE_BUCKET')
AUTH_KEY = os.getenv('AUTH_KEY')
SESSION_TIMEOUT = int(os.getenv('SESSION_TIMEOUT_IN_MINUTES'))

# initialize extractors
for mod in os.listdir('src/extract'):
    importlib.import_module(f'src.extract.{mod.replace(".py", "")}')
