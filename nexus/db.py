import sqlite3
from .tools import safe
def create(path):
 p=safe(path); p.parent.mkdir(parents=True,exist_ok=True)
 with sqlite3.connect(p): pass
 return {"path":path}
def query(path,sql,params=()):
 if not sql.lstrip().lower().startswith(("select","pragma")): raise PermissionError("read-only query tool")
 with sqlite3.connect(safe(path)) as c:
  cur=c.execute(sql,params); return {"columns":[x[0] for x in cur.description or []],"rows":cur.fetchall()}
