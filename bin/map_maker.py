import sqlite3
import db_tasks
import img_tasks


def initialize():
    db_tasks.create_table()
    db_tasks.index_files()


def find_recent_changes():
    """
    Find files that have been updated since
    the last image merge. Don't repeat merges
    """