#inspired by that one paper, but trying to get a good function by hand
import itertools
import numpy as np


def complete(t1,t2):
    return tuple((-(np.array(t1,dtype=int)+np.array(t2,dtype=int)))%3)
def greedy_solve(n,f):
    #given a function f from n-tuples to R, generate a greedy solution
    candidates = set(itertools.product([0,1,2],repeat=n))
    scored_candidates = [(c,f(c)) for c in candidates]
    scored_candidates = sorted(scored_candidates, key = lambda x: -x[1])
    value_dict = {c: v for c,v in scored_candidates}
    seen = set()
    output = []
    while len(value_dict) > 0:
        c = next(iter(value_dict))
        output += [c]
        seen.add(c)
        value_dict.pop(c)
        for c2 in seen:
            c3 = complete(c,c2)
            if c3 in value_dict:
                value_dict.pop(c3)
    return output
        