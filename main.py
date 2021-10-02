import numpy as np
from tabulate import tabulate
# Matrices
from matrices.similarity_matrix import similarity_matrix
from matrices.prediction_matrix import prediction_matrix

# Read a CSV file or maybe just hardcode the data if there isn't that much of it
# Note that if data is missing - use either an 'ø' or an 'Ø' as placeholder

rate_mat = [["Ø",4,1,4], [5,3,4,2], [2,4,1,5], 
            [3,5,3,5], [4,3,5,1], [5,2,3,3],
            [2,1,1,2], [3,3,1,5]]

sim_mat = similarity_matrix(rate_mat)
pred_mat = prediction_matrix(rate_mat, 3)

print(f"Similarity matrix:\n", tabulate(sim_mat))
print(f"\n\nPrediction matrix:\n", tabulate(pred_mat,))


