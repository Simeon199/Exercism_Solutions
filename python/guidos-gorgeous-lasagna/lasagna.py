"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(layers):
    """Calculate the preparation time needed.

    :param layers: int - number with layers necessary to prepare the lasagne.
    :return: array - time (in minutes) necessary to prepare a given number of lasagne layers.

    Function that takes the arrays the lasagna needs to have 
    and returns how many minutes the lasagna needs to be prepared
    based on the number of layers.
    """
    layers = layers*2
    return layers
    
def elapsed_time_in_minutes(layers, time):
    """Calculate the elapsed time since the lasagne has been started to be prepared.

    :param layers: array - array with layers necessary to prepare the lasagne.
    :param time: time - time that the lasagne has spent in the oven.
    :return: int - time (in minutes) elapsed since the lasagne has been started to be prepared.

    Function that takes the number of layers and the time that the lasagne has been in the 
    oven and adds them to calculate the total elapsed time in minutes.
    """
    preparation_time = preparation_time_in_minutes(layers)
    return time + preparation_time