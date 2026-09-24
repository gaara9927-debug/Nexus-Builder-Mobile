from pathlib import Path
from .tools import safe
def svg(path,width=512,height=512,title="Nexus"):
 p=safe(path);p.parent.mkdir(parents=True,exist_ok=True)
 data=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><rect width="100%" height="100%" fill="#071020"/><circle cx="50%" cy="45%" r="30%" fill="#152c5b"/><text x="50%" y="88%" text-anchor="middle" fill="white" font-family="sans-serif" font-size="32">{title}</text></svg>'''
 p.write_text(data,encoding="utf-8");return {"path":path,"bytes":p.stat().st_size}
