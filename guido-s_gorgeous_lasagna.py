EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2



def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the time remaining after the time elapsed.
    """
    if EXPECTED_BAKE_TIME >= elapsed_bake_time:
        return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    Calculates how many minutes we spend preparing the layers.
    """
    return number_of_layers * PREPARATION_TIME

    
def elapsed_time_in_minutes(number_of_layers , elapsed_bake_time):
    """
    Return elapsed cooking time.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
