from pathlib import Path
import shutil,zipfile,hashlib
from .tools import safe,ROOT
def write(path,data): p=safe(path);p.parent.mkdir(parents=True,exist_ok=True);p.write_text(data,encoding="utf-8");return {"path":path,"bytes":p.stat().st_size}
def edit(path,old,new): p=safe(path);s=p.read_text();p.write_text(s.replace(old,new),encoding="utf-8");return {"path":path}
def copy(src,dst): s,d=safe(src),safe(dst);d.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(s,d);return {"path":dst}
def move(src,dst): s,d=safe(src),safe(dst);d.parent.mkdir(parents=True,exist_ok=True);shutil.move(s,d);return {"path":dst}
def listdir(path="."): return [str(x.relative_to(ROOT)) for x in safe(path).iterdir()]
def info(path): p=safe(path);return {"path":path,"bytes":p.stat().st_size,"file":p.is_file(),"dir":p.is_dir()}
def compress(src,dst): 
 s,d=safe(src),safe(dst);d.parent.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(d,"w",zipfile.ZIP_DEFLATED) as z:
  items=s.rglob("*") if s.is_dir() else [s]
  for p in items:
   if p.is_file(): z.write(p,p.relative_to(s.parent))
 return {"path":dst}
