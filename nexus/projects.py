from pathlib import Path
import json, shutil, time
from .tools import ROOT, safe

META=".nexus-project.json"
def create(name):
    p=safe(name); p.mkdir(parents=True,exist_ok=False)
    (p/META).write_text(json.dumps({"name":name,"created":int(time.time())}),encoding="utf-8")
    return {"name":name,"path":str(p.relative_to(ROOT))}
def list_projects():
    return [{"name":p.name} for p in ROOT.iterdir() if p.is_dir() and (p/META).exists()]
def tree(name):
    p=safe(name)
    return [str(x.relative_to(p)) for x in p.rglob("*") if x.is_file()]
def backup(name):
    p=safe(name); dst=safe("_backups/"+name+"-"+str(int(time.time())))
    dst.parent.mkdir(parents=True,exist_ok=True); shutil.copytree(p,dst)
    return {"backup":str(dst.relative_to(ROOT))}
