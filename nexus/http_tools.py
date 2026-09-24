from urllib.request import Request,urlopen
from urllib.parse import urlparse
def _guard(url):
 u=urlparse(url)
 if u.scheme not in ("http","https"): raise ValueError("http/https only")
 if not u.hostname: raise ValueError("invalid host")
def get(url,timeout=10):
 _guard(url)
 with urlopen(Request(url,headers={"User-Agent":"Nexus/0.2"}),timeout=timeout) as r:
  data=r.read(1_000_000)
  return {"status":r.status,"content_type":r.headers.get("content-type"),"body":data.decode("utf-8","replace")}
