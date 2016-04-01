config = {
    'db_file': 'data/newrelic.csv',
    'db_file_bkp': 'data/newrelic.bkp.csv'
}


def get(param: str):
    return config[param]
