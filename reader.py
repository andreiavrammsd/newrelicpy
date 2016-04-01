import re


def read(arg: str) -> list:
    return re.findall(r'([\d\.]+)', arg)
