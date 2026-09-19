#!/usr/bin/env python3
from __future__ import annotations
import argparse, itertools, json
from collections import deque
from pathlib import Path

VERSION='1.1.0'
N=6

def edges_for(n):
    return [(i,j) for i in range(n) for j in range(i+1,n)]

def triangles_for(n):
    return list(itertools.combinations(range(n),3))

def masks(n):
    idx={e:k for k,e in enumerate(edges_for(n))}
    out=[]
    for a,b,c in triangles_for(n):
        out.append((1<<idx[(a,b)])|(1<<idx[(a,c)])|(1<<idx[(b,c)]))
    return out

def endpoint_masks(n):
    return [(1<<a)^(1<<b) for a,b in edges_for(n)]

def key_of(x,n):
    p=0
    for e,vm in enumerate(endpoint_masks(n)):
        if (x>>e)&1:
            p^=vm
    return p,x.bit_count()%3

def generate():
    M=masks(N)
    total=1<<(N*(N-1)//2)
    seen=bytearray(total)
    parent=[-2]*total
    move=[-2]*total
    depth=[-1]*total
    fibers=[]

    for root in range(total):
        if seen[root]:
            continue
        seen[root]=1
        parent[root]=-1
        move[root]=-1
        depth[root]=0
        q=deque([root])
        states=[]
        max_depth=0
        while q:
            x=q.popleft()
            states.append(x)
            max_depth=max(max_depth,depth[x])
            for tid,mask in enumerate(M):
                z=x&mask
                if z!=0 and z!=mask:
                    continue
                y=x^mask
                if seen[y]:
                    continue
                seen[y]=1
                parent[y]=x
                move[y]=tid
                depth[y]=depth[x]+1
                q.append(y)
        p,r=key_of(root,N)
        assert all(key_of(x,N)==(p,r) for x in states)
        fibers.append({
            'parity_mask':p,
            'residue':r,
            'root':root,
            'size':len(states),
            'max_depth':max_depth,
        })

    fibers.sort(key=lambda f:(f['parity_mask'],f['residue']))
    assert len(fibers)==96
    assert all(x!=-2 for x in parent)
    assert all(x!=-2 for x in move)
    roots=[i for i,p in enumerate(parent) if p==-1]
    assert len(roots)==96

    return {
        'format':'SOST-K6-spanning-forest-certificate-v1',
        'version':VERSION,
        'n':N,
        'state_count':total,
        'orbit_count':96,
        'edge_order':[list(e) for e in edges_for(N)],
        'triangle_order':[list(t) for t in triangles_for(N)],
        'fibers':fibers,
        'parent':parent,
        'move_triangle_index':move,
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',required=True)
    a=ap.parse_args()
    out=Path(a.output)
    out.parent.mkdir(parents=True,exist_ok=True)
    data=generate()
    out.write_text(json.dumps(data,separators=(',',':'))+'\n',encoding='utf-8')
    max_depth=max(f['max_depth'] for f in data['fibers'])
    print('SOST K6 certificate generator v1.1.0')
    print(f'states:{data["state_count"]}')
    print(f'fibers:{data["orbit_count"]}')
    print(f'parent_edges:{data["state_count"]-data["orbit_count"]}')
    print(f'max_depth:{max_depth}')
    print('status:PASS')

if __name__=='__main__':
    main()
