import numpy as np

def align_function(embedding_to_be_align, target_embedding):
    intersection_keys = list(set(embedding_to_be_align.keys()).intersection(set(target_embedding)))
    
    A = np.array([embedding_to_be_align[key] for key in intersection_keys]).T
    B = np.array([target_embedding[key] for key in intersection_keys]).T
    M = B.dot(A.T)
    u,sigma,v_t = np.linalg.svd(M)
    rotation_matrix = u.dot(v_t)
    aligned_embedding = {k: rotation_matrix.dot(v) for k,v in embedding_to_be_align.items()}
    
    return aligned_embedding