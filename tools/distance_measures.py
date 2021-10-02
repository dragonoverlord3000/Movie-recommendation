import numpy as np

def Ln_distance(Ra, Rm, n):
    """
    Args:
        Ra (list): user 'a'
        Rm (list): user 'm'
        n (int): the distance measure to use

    Returns (float):
        The L'n' distance

    Example:
        >>> Ln_distance([1,2,3,4,5], [5,1,2,2,2], 2)
        5.5677643628300215

    Explanation:
        n = 1, returns the mean absolute error
        n = 2, returns the euclidian distance
        n = k, returns the 'Lk distance'
        n = infinity, doesn't return anything, but should return the maximum value in the vector Ra - Rm
    """
    return (sum([np.abs(ra - rm)**n for ra, rm in zip(Ra, Rm)]))**(1/n)

