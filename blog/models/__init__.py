import sqlite3

def connect_db():
    """Connects to local sqlite database"""
    return sqlite3.connect("blog.db", detect_types=sqlite3.PARSE_DECLTYPES)

from . import Description
from .Article import Article
