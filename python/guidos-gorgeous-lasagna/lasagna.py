EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(layers: int):
    """Calculate preparation time in minutes

    :param layers: int number of layers.
    :return: int preparation time for the number of layers.
    """
    return PREPARATION_TIME * layers


def elapsed_time_in_minutes(layers: int, elapsed_bake_time: int):
    """Calculate the elapsend time in minutes.

    :param layers: int the number of layers.
    :param elapsed_bake_time: int baking time already elapsed.
    :return: int elapsed time cumulating the preparation of the layers and the baking time'.

    """
    return elapsed_bake_time + (PREPARATION_TIME * layers)
