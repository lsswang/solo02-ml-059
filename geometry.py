"""Ordinary linear transportation, without quadratic relational costs."""
import numpy as np
from scipy.optimize import linprog


def transport(cost, source_mass, target_mass):
    cost=np.asarray(cost,dtype=float)
    a=np.asarray(source_mass,dtype=float);b=np.asarray(target_mass,dtype=float)
    n,m=cost.shape
    rows=[];right=[]
    for r in range(n):
        row=np.zeros((n,m));row[r,:]=1;rows.append(row.ravel());right.append(a[r])
    for c in range(m-1):
        row=np.zeros((n,m));row[:,c]=1;rows.append(row.ravel());right.append(b[c])
    result=linprog(cost.ravel(),A_eq=np.asarray(rows),b_eq=np.asarray(right),bounds=(0,None),method='highs')
    if not result.success: raise RuntimeError(result.message)
    return {'transport':result.x.reshape(n,m).tolist(),'linear_cost':float(result.fun)}
