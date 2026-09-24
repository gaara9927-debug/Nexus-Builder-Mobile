from pathlib import Path
import hashlib
class LocalAIRuntime:
 def __init__(self): self.model=None
 def inspect(self,path):
  p=Path(path)
  if not p.exists(): return {"status":"BLOCKED","reason":"model file missing"}
  h=hashlib.sha256()
  with p.open("rb") as f:
   for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
  return {"status":"AVAILABLE","bytes":p.stat().st_size,"sha256":h.hexdigest()}
 def load(self,path):
  info=self.inspect(path)
  if info["status"]!="AVAILABLE": return info
  try:
   from llama_cpp import Llama
  except ImportError: return {"status":"BLOCKED","reason":"llama-cpp-python not installed"}
  self.model=Llama(model_path=str(path),n_ctx=2048,verbose=False)
  return {"status":"LOADED",**info}
 def chat(self,prompt,max_tokens=256):
  if self.model is None: raise RuntimeError("model not loaded")
  r=self.model.create_chat_completion(messages=[{"role":"user","content":prompt}],max_tokens=max_tokens)
  return r["choices"][0]["message"]["content"]
 def unload(self): self.model=None; return {"status":"UNLOADED"}
