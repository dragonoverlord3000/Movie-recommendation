def avg(Ru, *args):
    """
    Args:
        Ru (list): the K nearest neighbors rating of some movie
    
    Returns (float):
        The average of the values in Ru
    """
    return sum(Ru)/len(Ru)

def weighted_avg(Ru, weights, *args):
    """
    Args:
        Ru (list): the K nearest neighbors rating of some movie
        weights (list): list of similarities with the KNN, these are used as weights in the weighted average

    Returns (float):
        The weighted average og the elements in Ru
    """
    return sum([w * ru for w, ru in zip(weights, Ru)])/sum(weights)

def adjusted_avg(Ru, weights, Ru_avgs, Ra):
    """
    Args:
        Ru (list): the K nearest neighbors rating of some movie
        weights (list): list of similarities with the KNN, these are used as weights in the weighted average
        Ru_avgs (list): list of the average rating of each of the KNN
        Ra (list): all the ratings given by user 'a'

    Returns (float):
        The adjusted average og the elements in Ru
    """
    Ra_avg = sum(Ra)/len(Ra)
    return Ra_avg + sum([(ru - ru_avg) * w for ru,ru_avg, w in zip(Ru, Ru_avgs, weights)])/sum(weights)



