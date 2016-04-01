from time import strftime


def add_time(data: list) -> list:
    time = strftime('%Y-%m-%d %H:%M:%S')
    data.insert(0, time)
