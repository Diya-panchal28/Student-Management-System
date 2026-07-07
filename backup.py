import shutil
import sqlite3


def backup_database(source, destination):
    """
    Create a backup of the database.
    """

    shutil.copy(source, destination)


def restore_database(source, destination):
    """
    Restore database from a backup file.
    """

    shutil.copy(source, destination)


def reconnect_database(database_name):
    """
    Reconnect to the restored database.
    """

    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    return conn, cursor


import os


def backup_exists(path):

    return os.path.exists(path)
