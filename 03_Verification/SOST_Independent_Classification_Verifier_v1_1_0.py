#!/usr/bin/env python3
import argparse,itertools,json,os,shutil,subprocess,tempfile
from pathlib import Path

def edges_for(n):return [(i,j) for i in range(n) for j in range(i+1,n)]
def masks(n):
    idx={e:k for k,e in enumerate(edges_for(n))}
    return [(1<<idx[(a,b)])|(1<<idx[(a,c)])|(1<<idx[(b,c)]) for a,b,c in itertools.combinations(range(n),3)]
def endpoint_masks(n):return [(1<<a)^(1<<b) for a,b in edges_for(n)]
def key(x,n):
    p=0
    for e,vm in enumerate(endpoint_masks(n)):
        if (x>>e)&1:p^=vm
    return p,x.bit_count()%3

def flood(n):
    N=1<<(n*(n-1)//2); seen=bytearray(N); ms=masks(n); comps=[]
    for s in range(N):
        if seen[s]:continue
        q=[s];seen[s]=1;head=0;states=[]
        while head<len(q):
            x=q[head];head+=1;states.append(x)
            for m in ms:
                z=x&m
                if z==0 or z==m:
                    y=x^m
                    if not seen[y]:seen[y]=1;q.append(y)
        comps.append(states)
    return comps

def boundary():
    exp={3:7,4:32,5:59,6:96};total=0
    for n in range(3,7):
        comps=flood(n);assert len(comps)==exp[n];total+=1<<(n*(n-1)//2)
        kt={};coll=0
        for cid,states in enumerate(comps):
            ks={key(x,n) for x in states};assert len(ks)==1;k=next(iter(ks))
            if k in kt and kt[k]!=cid:coll+=1
            else:kt[k]=cid
        if n==3:assert coll==0
        elif n in (4,5):assert coll>0
        else:assert coll==0 and len(kt)==96
    assert total==33864
    return total

def run_cpp():
    c=shutil.which('g++')
    if not c:raise RuntimeError('complete verification requires g++ on PATH')
    src=Path(__file__).with_name('SOST_Independent_Holdout_n7_v1_1_0.cpp')
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/('sost_holdout.exe' if os.name=='nt' else 'sost_holdout')
        subprocess.run([c,'-O3','-std=c++17',str(src),'-o',str(exe)],check=True,capture_output=True,text=True)
        q=subprocess.run([str(exe)],check=True,capture_output=True,text=True)
    d=json.loads(q.stdout.strip());assert d['states']==2097152 and d['components']==192 and d['invariant_keys']==192 and d['mismatches']==0 and d['legal_state_triangle_checks']==18350080
    return d

def main():
    ap=argparse.ArgumentParser();g=ap.add_mutually_exclusive_group(required=True);g.add_argument('--self-test',action='store_true');g.add_argument('--verify',action='store_true');a=ap.parse_args()
    total=boundary();print('SOST v1.1.0 independent partition verifier');print(f'boundary_floodfill:PASS:states={total}:counts=3:7,4:32,5:59,6:96')
    if a.verify:
        d=run_cpp();print(f'n7_independent_floodfill:PASS:states={d["states"]}:components={d["components"]}:labels={d["invariant_keys"]}');print(f'n7_transition_audit:PASS:legal_state_triangle_checks={d["legal_state_triangle_checks"]}');print('TOTAL 3/3 PASS')
    else:print('TOTAL 1/1 PASS')
if __name__=='__main__':main()
