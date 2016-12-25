config = {
    'db_file': 'data/newrelic.csv',
    'db_file_bkp': 'data/newrelic.bkp.csv',
    'db_file_template': 'data/newrelic_template.csv'
}


def get(param: str):
    return config[param]
