#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from sost_core_v1_1_0 import state_from_edges, invariant_key, parity_vector_bits

def load_graph(path):
    obj=json.loads(Path(path).read_text(encoding='utf-8'))
    n=int(obj['n'])
    return n,state_from_edges(n,obj.get('edges',[]))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('graph_a')
    ap.add_argument('graph_b')
    a=ap.parse_args()
    n1,x=load_graph(a.graph_a)
    n2,y=load_graph(a.graph_b)
    if n1!=n2:
        raise SystemExit('orders differ')
    if n1<6:
        raise SystemExit('the theorem-based decision tool requires n>=6')
    kx=invariant_key(x,n1); ky=invariant_key(y,n1)
    print('order:'+str(n1))
    print('graph_a_parity:'+''.join(map(str,parity_vector_bits(kx[0],n1))))
    print('graph_a_edge_mod3:'+str(kx[1]))
    print('graph_b_parity:'+''.join(map(str,parity_vector_bits(ky[0],n1))))
    print('graph_b_edge_mod3:'+str(ky[1]))
    print('equivalence:'+('EQUIVALENT' if kx==ky else 'INEQUIVALENT'))
if __name__=='__main__':main()
