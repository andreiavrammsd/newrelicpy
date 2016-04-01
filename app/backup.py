from shutil import copy
from app import config


def save():
    src = config.get('db_file')
    dst = config.get('db_file_bkp')
    copy(src, dst)
