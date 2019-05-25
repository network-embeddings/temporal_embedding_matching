import numpy as np


def align_two_embs(emb_to_align, emb_base):
    common_keys = list(set(emb_to_align.keys()).intersection(set(emb_base)))

    A = np.array([emb_to_align[key] for key in common_keys]).T
    B = np.array([emb_base[key] for key in common_keys]).T
    M = B.dot(A.T)
    u, sigma, v_t = np.linalg.svd(M)
    rotation_matrix = u.dot(v_t)
    aligned_embedding = {k: rotation_matrix.dot(v) for k, v in emb_to_align.items()}

    return aligned_embedding
