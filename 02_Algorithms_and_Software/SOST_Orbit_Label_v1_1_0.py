#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from sost_core_v1_1_0 import state_from_edges, invariant_key, parity_vector_bits

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('graph'); a=ap.parse_args()
    obj=json.loads(Path(a.graph).read_text(encoding='utf-8'))
    n=int(obj['n']); x=state_from_edges(n,obj.get('edges',[]))
    p,r=invariant_key(x,n)
    print('order:'+str(n))
    print('degree_parity:'+''.join(map(str,parity_vector_bits(p,n))))
    print('edge_count_mod3:'+str(r))
    if n>=6:
        print('theorem_class_label:'+format(p,'0%db'%n)+':'+str(r))
    else:
        print('theorem_class_label:OUTSIDE_STABLE_RANGE')
if __name__=='__main__':main()
