#!/usr/bin/env python3
"""Core utilities for the SOST monochromatic-triangle toggle system."""
from itertools import combinations

def edges_for(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]

def edge_index(n):
    return {e:k for k,e in enumerate(edges_for(n))}

def triangle_masks(n):
    idx=edge_index(n)
    return [
        (1<<idx[(a,b)]) | (1<<idx[(a,c)]) | (1<<idx[(b,c)])
        for a,b,c in combinations(range(n),3)
    ]

def endpoint_masks(n):
    return [(1<<a)^(1<<b) for a,b in edges_for(n)]

def invariant_key(state,n):
    parity=0
    for e,vmask in enumerate(endpoint_masks(n)):
        if (state>>e)&1:
            parity ^= vmask
    return parity, state.bit_count()%3

def legal_moves(state,n):
    for mask in triangle_masks(n):
        bits=state&mask
        if bits==0 or bits==mask:
            yield state^mask

def state_from_edges(n,edges):
    idx=edge_index(n)
    x=0
    for a,b in edges:
        if a>b: a,b=b,a
        if a==b or (a,b) not in idx:
            raise ValueError('invalid edge')
        x |= 1<<idx[(a,b)]
    return x

def edges_from_state(n,state):
    E=edges_for(n)
    return [list(E[k]) for k in range(len(E)) if (state>>k)&1]

def parity_vector_bits(parity,n):
    return [(parity>>i)&1 for i in range(n)]
