from pathlib import Path
from .tools import ROOT
def search_project(project,query,limit=20):
 base=(ROOT/project).resolve()
 if base!=ROOT and ROOT not in base.parents: raise PermissionError("outside workspace")
 hits=[]
 for p in base.rglob("*"):
  if p.is_file() and p.stat().st_size<1_000_000:
   try:
    t=p.read_text(encoding="utf-8")
    if query.lower() in t.lower(): hits.append({"file":str(p.relative_to(base)),"excerpt":t[:1200]})
   except (UnicodeDecodeError,OSError): pass
   if len(hits)>=limit: break
 return hits
