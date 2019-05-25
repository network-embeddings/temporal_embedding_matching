# temporal_embedding_matching

Many embeddings alogorithms have randomness. Embedding results may be different even if actural similiarty over the embeddins are similar due to stochastic nature.

It can be big problem when we are dealing with temporal embeddings with incremental embedding. In order to compare embeddings from different time-periods, we must ensure that the vectors are aligned to the same coordinate axes.


![alt text](public/example.png)

For example, embeddings of 1940s and embeddings of 1950s may result in orthogonal transformantion. Pairswise consine-simarties within-years are same but embedding vectors can be totally diffrent due to effect of axis transformation.

In [histword](https://arxiv.org/abs/1605.09096), they use solution of [orthogonal Procrustes](https://en.wikipedia.org/wiki/Orthogonal_Procrustes_problem) to align the
learned low-dimensional embeddings.


This script matches given two sets of embeddings even when the sets do not exactly match. 
Input data struction of embedding is dict whose key is name of entity in data, value is embedding vector or entity.
```
{
key_1: embedding_vector_of_key_1,
key_2: embedding_vector_of_key_2,
key_3: embedding_vector_of_key_3,
key_4: embedding_vector_of_key_4,
}
 ```
If key's list of two embedding are not identical, function find overlapping keys. Aproximated rotation matrix
with overlapping keys will be caluclated, and algined embeddings will be returned.

Before align           |  After align
:-------------------------:|:-------------------------:
![](public/example_before.png)  |  ![](public/example_after.png)
