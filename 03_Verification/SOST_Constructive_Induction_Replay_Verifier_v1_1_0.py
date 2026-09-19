#!/usr/bin/env python3
from __future__ import annotations
import argparse, itertools, json, random
from functools import lru_cache
from pathlib import Path

ROOT=Path(__file__).resolve().parent
CERT=ROOT/'certificates/SOST_K6_Orbit_Certificate_v1_1_0.json'

def edges_for(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]

def edge_index(n):
    return {e:k for k,e in enumerate(edges_for(n))}

def triangles_for(n):
    return list(itertools.combinations(range(n),3))

def endpoint_masks(n):
    return [(1<<a)^(1<<b) for a,b in edges_for(n)]

def key_of(x,n):
    p=0
    for e,vm in enumerate(endpoint_masks(n)):
        if (x>>e)&1:
            p^=vm
    return p,x.bit_count()%3

def neighbors(x,n,v):
    out=[]
    for e,(a,b) in enumerate(edges_for(n)):
        if not ((x>>e)&1): continue
        if a==v: out.append(b)
        elif b==v: out.append(a)
    return out

class K6Certificate:
    def __init__(self):
        d=json.loads(CERT.read_text(encoding='utf-8'))
        self.parent=d['parent']
        self.move=d['move_triangle_index']
        self.triangles=[tuple(t) for t in d['triangle_order']]
        self.edges=[tuple(e) for e in d['edge_order']]
        self.edge_idx={e:i for i,e in enumerate(self.edges)}
        self.root=[None]*32768
        for x in range(32768):
            self.root[x]=self._root_of(x)
        self.target_iso={}
        self.target_anchor={}
        for x in range(32768):
            r=self.root[x]
            for v in range(6):
                ng=self._neighbors6(x,v)
                if len(ng)==0:
                    self.target_iso.setdefault((r,v),x)
                elif len(ng)==1:
                    self.target_anchor.setdefault((r,v,ng[0]),x)

    @lru_cache(maxsize=None)
    def _root_of(self,x):
        p=self.parent[x]
        if p==-1: return x
        return self._root_of(p)

    def _neighbors6(self,x,v):
        out=[]
        for e,(a,b) in enumerate(self.edges):
            if not ((x>>e)&1): continue
            if a==v: out.append(b)
            elif b==v: out.append(a)
        return out

    def path_to_root(self,x):
        out=[]
        while self.parent[x]!=-1:
            out.append(self.move[x])
            x=self.parent[x]
        return out

    def path(self,src,dst):
        assert self.root[src]==self.root[dst]
        a=self.path_to_root(src)
        b=self.path_to_root(dst)
        return a+list(reversed(b))

CERT6=K6Certificate()

def induced_state(global_state,n,verts):
    idx=edge_index(n)
    x=0
    for le,(i,j) in enumerate(CERT6.edges):
        a,b=verts[i],verts[j]
        if a>b: a,b=b,a
        if (global_state>>idx[(a,b)])&1:
            x|=1<<le
    return x

def apply_triangle(global_state,n,tri):
    idx=edge_index(n)
    mask=0
    for a,b in ((tri[0],tri[1]),(tri[0],tri[2]),(tri[1],tri[2])):
        if a>b: a,b=b,a
        mask|=1<<idx[(a,b)]
    z=global_state&mask
    assert z==0 or z==mask
    return global_state^mask

def apply_local_path(global_state,n,verts,target_local):
    src=induced_state(global_state,n,verts)
    path=CERT6.path(src,target_local)
    for tid in path:
        lt=CERT6.triangles[tid]
        tri=(verts[lt[0]],verts[lt[1]],verts[lt[2]])
        global_state=apply_triangle(global_state,n,tri)
    assert induced_state(global_state,n,verts)==target_local
    return global_state,len(path)

def choose_fillers(current_vertices,required,count):
    req=list(dict.fromkeys(required))
    assert len(req)<=count
    for x in current_vertices:
        if x not in req:
            req.append(x)
            if len(req)==count: break
    assert len(req)==count
    return req

def compress_vertex(state,n,current_n,v,anchor=0):
    assert v<current_n and anchor<current_n and v!=anchor
    total_moves=0
    special=False
    current=list(range(current_n))

    while len(neighbors(state,n,v))>5:
        ng=neighbors(state,n,v)
        five=ng[:5]
        verts=[v]+five
        src=induced_state(state,n,verts)
        r=CERT6.root[src]
        target=CERT6.target_anchor[(r,0,1)]
        state,m=apply_local_path(state,n,verts,target)
        total_moves+=m

    d=len(neighbors(state,n,v))
    ng=neighbors(state,n,v)

    if d%2==0:
        verts=choose_fillers(current,[v]+ng,6)
        lv=verts.index(v)
        src=induced_state(state,n,verts); r=CERT6.root[src]
        target=CERT6.target_iso[(r,lv)]
        state,m=apply_local_path(state,n,verts,target); total_moves+=m
        assert len(neighbors(state,n,v))==0
        return state,total_moves,special

    if d in (1,3):
        req=[v]+ng+([anchor] if anchor not in ng else [])
        verts=choose_fillers(current,req,6)
        lv=verts.index(v); la=verts.index(anchor)
        src=induced_state(state,n,verts); r=CERT6.root[src]
        target=CERT6.target_anchor[(r,lv,la)]
        state,m=apply_local_path(state,n,verts,target); total_moves+=m
        assert neighbors(state,n,v)==[anchor]
        return state,total_moves,special

    assert d==5
    if anchor in ng:
        verts=[v]+ng
        lv=0; la=verts.index(anchor)
        src=induced_state(state,n,verts); r=CERT6.root[src]
        target=CERT6.target_anchor[(r,lv,la)]
        state,m=apply_local_path(state,n,verts,target); total_moves+=m
        assert neighbors(state,n,v)==[anchor]
        return state,total_moves,special

    # Explicit exceptional branch: degree five and fixed anchor absent.
    special=True
    chosen=ng[:4]
    verts=[v]+chosen+[anchor]
    src=induced_state(state,n,verts); r=CERT6.root[src]
    target=CERT6.target_iso[(r,0)]
    state,m=apply_local_path(state,n,verts,target); total_moves+=m
    rem=neighbors(state,n,v)
    assert len(rem)==1 and rem[0]!=anchor

    req=[v,rem[0],anchor]
    verts=choose_fillers(current,req,6)
    lv=verts.index(v); la=verts.index(anchor)
    src=induced_state(state,n,verts); r=CERT6.root[src]
    target=CERT6.target_anchor[(r,lv,la)]
    state,m=apply_local_path(state,n,verts,target); total_moves+=m
    assert neighbors(state,n,v)==[anchor]
    return state,total_moves,special

def canonicalize(state,n):
    before=key_of(state,n)
    moves=0; specials=0
    for current_n in range(n,6,-1):
        v=current_n-1
        state,m,s=compress_vertex(state,n,current_n,v,0)
        moves+=m; specials+=int(s)
        ng=neighbors(state,n,v)
        assert ng in ([],[0])
    verts=list(range(6))
    src=induced_state(state,n,verts)
    root=CERT6.root[src]
    state,m=apply_local_path(state,n,verts,root)
    moves+=m
    assert key_of(state,n)==before
    return state,moves,specials

def targeted_exception():
    n=7; v=6; anchor=0
    idx=edge_index(n); x=0
    for u in (1,2,3,4,5):
        a,b=sorted((u,v)); x|=1<<idx[(a,b)]
    y,m,s=compress_vertex(x,n,7,v,anchor)
    assert s and neighbors(y,n,v)==[0]
    return m

def deterministic_corpus(samples_per_order):
    total=0; groups=0; specials=0; moves=0
    for n in (8,9,10):
        rng=random.Random(91000+n)
        max_state=1<<(n*(n-1)//2)
        seen={}
        for _ in range(samples_per_order):
            x=rng.randrange(max_state)
            k=key_of(x,n)
            c,m,s=canonicalize(x,n)
            moves+=m; specials+=s; total+=1
            if k in seen:
                assert seen[k]==c
                groups+=1
            else:
                seen[k]=c
        # Distinct invariant labels must not collapse to one canonical state.
        assert len(set(seen.values()))==len(seen)
    return {'states':total,'same_key_comparisons':groups,'special_branches':specials,'legal_moves':moves}

def main():
    ap=argparse.ArgumentParser(); g=ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--self-test',action='store_true'); g.add_argument('--verify',action='store_true')
    a=ap.parse_args()
    exc=targeted_exception()
    samples=96 if a.self_test else 256
    r=deterministic_corpus(samples)
    print('SOST constructive induction replay verifier v1.1.0')
    print(f'degree5_anchor_absent:PASS:legal_moves={exc}')
    print(f'constructive_orders:PASS:orders=8,9,10:states={r["states"]}:same_key_comparisons={r["same_key_comparisons"]}')
    print(f'legal_move_replay:PASS:moves={r["legal_moves"]}:special_branches={r["special_branches"]}')
    print('canonical_invariant_separation:PASS')
    print('TOTAL 4/4 PASS')

if __name__=='__main__':
    main()
