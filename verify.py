#!/usr/bin/env python3
import argparse,hashlib,json,py_compile,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parent
HASH=ROOT/'05_Reproduction_and_Verification/SOST_Computational_Integrity_SHA256_v1_1_0.txt'
EXCLUDED_PHRASES=(
    'publication'+' '+'candidate',
    'external'+' '+'release',
    'public'+' '+'release',
    'break'+'through',
    'internal'+' '+'commentary',
    'major'+' '+'field-level',
)

def hash_file(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()

def check_integrity():
    ok=True;count=0
    for line in HASH.read_text(encoding='utf-8').splitlines():
        line=line.strip()
        if not line or line.startswith('#'):continue
        sha,rel=line.split('  ',1);p=ROOT/rel;count+=1
        if not p.is_file() or hash_file(p)!=sha:
            print('integrity:'+rel+':FAIL');ok=False
        if p.suffix not in ('.py','.cpp','.json'):
            print('integrity_policy:'+rel+':FAIL');ok=False
    ok=ok and count>0
    print('integrity_manifest:'+('PASS' if ok else 'FAIL'));return ok

def compile_python():
    ok=True
    with tempfile.TemporaryDirectory() as td:
        for p in ROOT.rglob('*.py'):
            try:py_compile.compile(str(p),cfile=str(Path(td)/(p.name+'.pyc')),doraise=True)
            except Exception as e:print('python_compile:'+str(p.relative_to(ROOT))+':FAIL:'+str(e));ok=False
    print('python_sources_compile:'+('PASS' if ok else 'FAIL'));return ok

def parse_json():
    ok=True
    for p in ROOT.rglob('*.json'):
        try:json.load(open(p,encoding='utf-8'))
        except Exception as e:print('json_parse:'+str(p.relative_to(ROOT))+':FAIL:'+str(e));ok=False
    print('json_parse:'+('PASS' if ok else 'FAIL'));return ok

def hygiene():
    ok=True
    for p in ROOT.rglob('*'):
        if '__pycache__' in p.parts or p.suffix in ('.pyc','.pyo'):ok=False
        if p.is_file() and 'LICENSES' not in p.parts:
            low=(p.name+'\n'+p.read_text(encoding='utf-8',errors='ignore')).lower()
            for phrase in EXCLUDED_PHRASES:
                if phrase in low:
                    print('terminology:'+str(p.relative_to(ROOT))+':FAIL:'+phrase);ok=False
    print('artifact_hygiene:'+('PASS' if ok else 'FAIL'));return ok

def run(rel,mode,label):
    q=subprocess.run([sys.executable,'-B',rel,mode],cwd=ROOT,text=True,capture_output=True)
    if q.stdout:print(q.stdout.rstrip())
    if q.stderr:print(q.stderr.rstrip(),file=sys.stderr)
    print(label+':'+('PASS' if q.returncode==0 else 'FAIL'));return q.returncode==0

def main():
    ap=argparse.ArgumentParser();g=ap.add_mutually_exclusive_group(required=True);g.add_argument('--self-test',action='store_true');g.add_argument('--verify',action='store_true');a=ap.parse_args();mode='--self-test' if a.self_test else '--verify'
    checks=[check_integrity(),compile_python(),parse_json(),hygiene()]
    checks.append(run('03_Verification/SOST_Theorem_Core_Verifier_v1_1_0.py',mode,'theorem_core_verifier'))
    checks.append(run('03_Verification/SOST_K6_Standalone_Certificate_Verifier_v1_1_0.py',mode,'k6_standalone_certificate_verifier'))
    checks.append(run('03_Verification/SOST_Constructive_Induction_Replay_Verifier_v1_1_0.py',mode,'constructive_induction_replay_verifier'))
    checks.append(run('03_Verification/SOST_Proof_Rigor_Audit_Verifier_v1_1_0.py',mode,'proof_rigor_audit_verifier'))
    checks.append(run('03_Verification/SOST_Independent_Classification_Verifier_v1_1_0.py',mode,'independent_classification_verifier'))
    print('status:'+('PASS' if all(checks) else 'FAIL'))
    print('checks_passed:%d/%d'%(sum(checks),len(checks)))
    raise SystemExit(0 if all(checks) else 1)
if __name__=='__main__':main()
