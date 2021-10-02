import numpy as np
from distance_measures import Ln_distance

def Ln_similarity(Ra, Rm, n=2):
    """
    Args:
        Ra (list): user 'a'
        Rm (list): user 'm'
        n (int): the distance measure to use

    Returns (float):
        The L'n' similarity

    Example:
        >>> Ln_similarity([1,2,3,4,5], [5,1,2,2,2], 2)
        0.15225881209433406
    """
    return 1/(1 + Ln_distance(Ra, Rm, n))

def pearson(Ra, Rm, *args):
    """
    Args:
        Ra (list): user 'a'
        Rm (list): user 'm'
        
    Returns (float):
        The pearson correlation between Ra and Rm

    Example:
        >>> pearson([1,2,3,4,5], [5,1,2,2,2])
        -0.5212860351426869
        >>> pearson([1,2,3,4], [1,2,3,4])
        1.0
    """
    Ra_avg = sum(Ra)/len(Ra)
    Rm_avg = sum(Rm)/len(Rm)
    
    t = sum([(ra - Ra_avg) * (rm - Rm_avg) for ra, rm in zip(Ra,Rm)])
    b = np.sqrt(sum([(ra - Ra_avg)**2 for ra in Ra]) * sum([(rm - Rm_avg)**2 for rm in Rm]))
    return t/b

