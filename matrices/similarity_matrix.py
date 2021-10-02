import numpy as np

from tools.preprocesser import preprocess
from tools.similarity_measures import pearson, Ln_similarity

# GLOBAL VARIABLE
sim_dict = {"pearson": pearson, "Ln": Ln_similarity}

# Could be implemented in a smarter way that would require way less computing power
# by incoorporating the fact that the rating matrix is symmetric - i.e. equal
# to it's own transpose and the fact that the diagonal is made up of ones always

def similarity_matrix(rating_matrix, similarity_measure="pearson", n=2):   
    """
    Args:
        rating_matrix (list): list of lists - a (user * movies) matrix
        similarity_measure (str): the similarity measure to use, the following are implemented at the moment
            - pearson correlation: "pearson"
            - Ln similarity: "Ln"
        n (int): the n in Ln, so it decides the Ln distance to use

    Returns (np.array):
        The similarity matrix corresponding to the rating matrix
    """

    n_users = len(rating_matrix)
    sim_matrix = np.zeros(shape=(n_users, n_users))
    
    for i, user1 in enumerate(rating_matrix):
        for j, user2 in enumerate(rating_matrix):
            u1, u2 = preprocess(user1, user2)
            sim_i_j = sim_dict[similarity_measure](u1, u2, n)
            sim_matrix[i][j] = sim_i_j
            
    return sim_matrix