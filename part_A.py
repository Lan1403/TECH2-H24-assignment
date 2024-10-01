"""
TECH2 mandatory assignment - Part A

Write the implementation of part A of the exercise below.
"""
from math import sqrt
def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    N = len(x)
    sum_x = sum([i for i in x])
    mean_x = sum_x / N
    sum_x2 = sum([i**2 for i in x])
    mean_x2 = sum_x2 / N
    variance = mean_x2 - mean_x**2
    return sqrt(variance)


def std_builtin(x):
    """
    Compute standard deviation of x using the built-in functions sum()
    and len().

    Parameters
    ----------
    x: Sequence of numbers

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.
    """
    N = len(x)
    mean_x = sum(x) / N
    mean_x2 = sum([i**2 for i in x]) / N
    variance = mean_x2 - mean_x**2
    return sqrt(variance)

import numpy as np
def std_numpy(x):
    return np.std(x)

num_lst = [1, 2, 3, 4, 5]
assert std_loops(num_lst) == np.std(num_lst) , 'result from loop function is different than numpy'
assert std_builtin(num_lst)== np.std(num_lst) , 'result from built-in function is different than numpy'
