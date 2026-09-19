#!/usr/bin/env python3
from __future__ import annotations
import argparse, itertools, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
CERT=ROOT/'certificates/SOST_K6_Orbit_Certificate_v1_1_0.json'
N=6

def edges_for(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]

def triangles_for(n):
    return list(itertools.combinations(range(n),3))

def triangle_masks(n):
    idx={e:k for k,e in enumerate(edges_for(n))}
    return [(1<<idx[(a,b)])|(1<<idx[(a,c)])|(1<<idx[(b,c)]) for a,b,c in triangles_for(n)]

def endpoint_masks(n):
    return [(1<<a)^(1<<b) for a,b in edges_for(n)]

def key_of(x,n):
    p=0
    for e,vm in enumerate(endpoint_masks(n)):
        if (x>>e)&1:
            p^=vm
    return p,x.bit_count()%3

def degree_neighbors(x,n,v):
    out=[]
    for e,(a,b) in enumerate(edges_for(n)):
        if not ((x>>e)&1):
            continue
        if a==v: out.append(b)
        elif b==v: out.append(a)
    return tuple(out)

def verify_certificate(full=True):
    d=json.loads(CERT.read_text(encoding='utf-8'))
    assert d['format']=='SOST-K6-spanning-forest-certificate-v1'
    assert d['version']=='1.1.0'
    assert d['n']==6 and d['state_count']==32768 and d['orbit_count']==96
    assert d['edge_order']==[list(e) for e in edges_for(6)]
    assert d['triangle_order']==[list(t) for t in triangles_for(6)]
    parent=d['parent']; moves=d['move_triangle_index']
    assert len(parent)==32768 and len(moves)==32768
    masks=triangle_masks(6)

    roots=[]
    parent_edges=0
    for x in range(32768):
        p=parent[x]; tid=moves[x]
        if p==-1:
            assert tid==-1
            roots.append(x)
            continue
        assert 0<=p<32768 and 0<=tid<len(masks)
        mask=masks[tid]
        z=x&mask
        assert z==0 or z==mask
        assert (x^mask)==p
        assert key_of(x,6)==key_of(p,6)
        parent_edges+=1
    assert len(roots)==96 and parent_edges==32672

    # Resolve every parent chain and certify acyclicity / unique root.
    root_cache={r:r for r in roots}
    for start in range(32768):
        if start in root_cache:
            continue
        trail=[]; seen=set(); x=start
        while x not in root_cache:
            assert x not in seen
            seen.add(x); trail.append(x)
            x=parent[x]
            assert x>=0
        r=root_cache[x]
        for y in trail:
            root_cache[y]=r
    assert len(root_cache)==32768

    root_keys={r:key_of(r,6) for r in roots}
    assert len(set(root_keys.values()))==96
    admissible={(p,r) for p in range(64) if p.bit_count()%2==0 for r in range(3)}
    assert set(root_keys.values())==admissible

    counts={r:0 for r in roots}
    for x in range(32768):
        r=root_cache[x]
        counts[r]+=1
        assert key_of(x,6)==root_keys[r]

    fibers=d['fibers']
    assert len(fibers)==96
    declared={f['root']:f for f in fibers}
    assert set(declared)==set(roots)
    for r in roots:
        f=declared[r]
        assert (f['parity_mask'],f['residue'])==root_keys[r]
        assert f['size']==counts[r]

    # Compression targets used by the theorem.
    isolated=set(); anchored=set()
    scan=range(32768) if full else range(0,32768,2)
    for x in scan:
        key=root_keys[root_cache[x]]
        for v in range(6):
            ngh=degree_neighbors(x,6,v)
            if len(ngh)==0:
                isolated.add((key,v))
            if len(ngh)==1:
                anchored.add((key,v,ngh[0]))

    if full:
        iso=anc=0
        for key in admissible:
            p,_=key
            for v in range(6):
                if ((p>>v)&1)==0:
                    assert (key,v) in isolated; iso+=1
                else:
                    for a in range(6):
                        if a==v: continue
                        assert (key,v,a) in anchored; anc+=1
        assert iso==288 and anc==1440
    else:
        iso=anc=-1

    return {
        'states':32768,
        'fibers':96,
        'parent_edges':32672,
        'max_depth':max(f['max_depth'] for f in fibers),
        'isolation_targets':iso,
        'anchored_targets':anc,
    }

def main():
    ap=argparse.ArgumentParser(); g=ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--self-test',action='store_true'); g.add_argument('--verify',action='store_true')
    a=ap.parse_args()
    r=verify_certificate(full=a.verify)
    print('SOST K6 standalone certificate verifier v1.1.0')
    print(f'legal_parent_forest:PASS:states={r["states"]}:roots={r["fibers"]}:parent_edges={r["parent_edges"]}')
    print('invariant_fibers:PASS:admissible_labels=96:unique_roots=96')
    print(f'parent_termination:PASS:max_declared_depth={r["max_depth"]}')
    if a.verify:
        print(f'compression_targets:PASS:isolation={r["isolation_targets"]}:anchored={r["anchored_targets"]}')
        print('TOTAL 4/4 PASS')
    else:
        print('TOTAL 3/3 PASS')

if __name__=='__main__':
    main()
