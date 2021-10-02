

def preprocess(R1, R2):
    """
    Args:
        R1 (list): user R1
        R2 (list): user R2

    Returns (lists):
        returns R1 and R2, but only where both R1 and R2 have rated the movie

    Example:
        >>> preprocess([1,2,3,"ø",3], ["ø", 5, 5, 2, 1])
        ([2, 3, 3], [5, 5, 1])
    """

    idx = []
    for i, elem in enumerate(R1):
        if elem == "ø" or elem == "Ø":
            idx.append(i)
            
    for i, elem in enumerate(R2):
        if elem == "ø" or elem == "Ø":
            idx.append(i)
    
    ret_R1, ret_R2 = [], []
    for i, (r1, r2) in enumerate(zip(R1, R2)):
        if not i in idx:
            ret_R1.append(r1)
            ret_R2.append(r2)
            
    return ret_R1, ret_R2

