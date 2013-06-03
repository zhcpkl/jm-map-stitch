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

    TODO: Find all images that aren't blank.
    See if they have been compiled. 
    If they haven't been compiled. Compile them
    for the first time. Otherwise, add file to the
    aggregated image.
    """
    # set up directories
    # db_folder = os.path.join(os.path.dirname(os.getcwd()),'db')
    # db_file = os.path.join(db_folder, 'worldmap.db')
    # con = sqlite3.connect(db_file)

    # with con:
    #     cur = con.cursor() 
    #     cur.execute(sql)
    # con.close()

    return None