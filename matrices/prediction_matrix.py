import numpy as np

from tools.preprocesser import preprocess
from tools.pred_methods import avg, weighted_avg, adjusted_avg
from matrices.similarity_matrix import similarity_matrix

# GLOBAL VARIABLES
# Haha pred_dict ~ predict
pred_dict = {"avg": avg, "w_avg": weighted_avg, "adj_avg": adjusted_avg}

def prediction_matrix(rating_matrix, K, similarity_measure="pearson", n=2, predict_method="adj_avg", humanify=True):
    """
    Args:
        rating_matrix (list) - a list of size (users * movies)
        K (int) - what K should be in KNN
        
    returns:
        prediction matrix
    """
    
    sim_mat = similarity_matrix(rating_matrix, similarity_measure, n)    
    pred_matrix = np.zeros_like(rating_matrix)
    
    
    for i, user1 in enumerate(rating_matrix):
        
        KNN_idx = np.argpartition(sim_mat[i], -K-1)[-K-1:-1]
        KNN_sim = [sim_mat[i][k] for k in KNN_idx]
        KNN = [rating_matrix[k] for k in KNN_idx]
        
        for j in range(len(user1)):
            user2 = [u[j] for u in KNN]
            user2_avg = [sum([r for r in v if not r in ["ø", "Ø"]])/len([r for r in v if not r in ["ø", "Ø"]]) for v in KNN]
            u1, u2 = preprocess(user1, user2)
            pred_i_j = pred_dict[predict_method](u2, KNN_sim, user2_avg, u1)
            pred_matrix[i][j] = pred_i_j if not humanify else max(min(round(pred_i_j), 5), 0) # let the predictions be in the set {0, 1, 2, 3, 4, 5}

    return pred_matrix



