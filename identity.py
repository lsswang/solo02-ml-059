"""Independent bipartite matches; no all-graphs stable identity contract."""
import numpy as np
from scipy.optimize import linear_sum_assignment


def pairwise(affinities):
    output=[]
    for pair in affinities:
        table=np.asarray(pair['mass'],dtype=float)
        rows,columns=linear_sum_assignment(table,maximize=True)
        output.append({'a':pair['a'],'b':pair['b'],'map':columns.tolist(),
                       'agreement':float(table[rows,columns].sum())})
    return output
