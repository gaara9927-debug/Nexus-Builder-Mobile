from pathlib import Path
import hashlib
ROOT=Path('workspace').resolve(); ROOT.mkdir(exist_ok=True)
def safe(path):
 p=(ROOT/path).resolve()
 if p!=ROOT and ROOT not in p.parents: raise PermissionError('outside workspace')
 return p
def create(path,content=''):
 p=safe(path); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(content,encoding='utf-8'); return {'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size}
def read(path): return safe(path).read_text(encoding='utf-8')
def hash_file(path): return hashlib.sha256(safe(path).read_bytes()).hexdigest()
TOOLS={'file.create':create,'file.read':read,'file.hash':hash_file}
def execute(name,args):
 if name not in TOOLS: raise KeyError('Tool unavailable')
 return TOOLS[name](**args)
def manifest(): return [{'name':n,'status':'AVAILABLE','local':True} for n in TOOLS]
