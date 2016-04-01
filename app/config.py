config = {
    'db_file': 'newrelic.csv'
}


def get(param: str):
    return config[param]
