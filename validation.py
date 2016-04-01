input_data_length = 5


def validate(data: list):
    if len(data) != input_data_length:
        raise Exception('Invalid input data')
