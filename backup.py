from shutil import copy


def save(file: str):
    copy(file, file.replace('.csv', '.bkp.csv'))
