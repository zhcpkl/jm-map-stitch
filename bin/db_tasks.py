import sqlite3
import os
import sys
import datetime

"""
This file handles all indexing of database information

TODO: directory information => make dictionary?
"""


def create_table():
    """
    Run create table script

    TODO: 1. check if table exists with python before running script? 
            (script auto-deletes existing table)
    """
    # set up directories
    db_folder = os.path.join(os.path.dirname(os.getcwd()),'db')
    schema_file = os.path.join(db_folder, 'schema.sql')
    db_file = os.path.join(db_folder, 'worldmap.db')

    # run schema file
    con = sqlite3.connect(db_file)
    with con:
        cur = con.cursor() 
        sql = open(schema_file, 'r').read()  
        cur.executescript(sql)
    con.close()


def index_files():
    """
    Find all images and update information for them in the database

    TODO => TEST to see if update/insert command is working correctly
    """
    # set up directories
    db_folder = os.path.join(os.path.dirname(os.getcwd()),'db') #path to db folder
    db_file = os.path.join(db_folder, 'worldmap.db')
    resources_folder = os.path.join(os.path.dirname(os.getcwd()),'resources') #path to resources folder

    # get list of folders with user journeymap information
    mappers_folders = os.listdir(resources_folder)
    
    # set up sql connection
    con = sqlite3.connect(db_file)
    with con:
        cur = con.cursor() 

        # look in each user's jm folder
        for folder in mappers_folders:
            full_path = os.path.join(resources_folder, folder)
            images = os.listdir(full_path)
            images = sorted(images, key=lambda im: os.path.getsize(os.path.join(full_path,im)))
            for im in images:
                file_path = os.path.join(full_path,im)
                bytes = os.path.getsize(file_path)
                date_modified = os.path.getmtime(file_path)
                info_tupe = (folder, im, full_path, bytes, date_modified)
                
                # insert or replace sql
                qry_template = """
                insert or replace into source_files 
                (username, filename, file_path, file_size_in_bytes, image_modified_date) 
                values (?, ?, ?, ?, ?);
                """
                cur.execute(qry_template, info_tupe)
    con.close()