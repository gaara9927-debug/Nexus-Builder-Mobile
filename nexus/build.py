import shutil,subprocess
from .tools import safe
ALLOWED={"python":["python","-m","py_compile"],"node":["node","--check"]}
def detect():
 return {k:bool(shutil.which(v[0])) for k,v in ALLOWED.items()}
def check(kind,path,timeout=30):
 if kind not in ALLOWED: raise ValueError("unsupported build checker")
 p=safe(path)
 cp=subprocess.run(ALLOWED[kind]+[str(p)],capture_output=True,text=True,timeout=timeout)
 return {"exit_code":cp.returncode,"stdout":cp.stdout[-4000:],"stderr":cp.stderr[-4000:]}
