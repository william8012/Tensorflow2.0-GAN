def normalize_inputs(data):
    """
    Normalizes the inputs to [-1, 1]

    :param data: input data array
    :return: normalized data to [-1, 1]
    """
    data = (data - 127.5) / 127.5
    return data


def get_noise(batch_size,n_noise):
    return tf.random.normal([batch_size,n_noise])