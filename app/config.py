config = {
    'db_file': 'data/newrelic.csv'
}


def get(param: str):
    return config[param]
