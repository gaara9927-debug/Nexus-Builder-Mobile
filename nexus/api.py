from fastapi import FastAPI,Header,HTTPException
from pydantic import BaseModel
from .core import NexusCore
from .security import get_key,masked
from .tools import execute,manifest
from .testgate import smoke
app=FastAPI(title='Nexus Local API',version='0.1.0'); core=NexusCore()
class ToolCall(BaseModel): tool:str; arguments:dict={}
def auth(k):
 if k!=get_key(): raise HTTPException(401,'Invalid Nexus key')
@app.get('/health')
def health(): return {**core.health(),'host':'127.0.0.1','port':8765}
@app.get('/v1/tools')
def tools(): return {'tools':manifest()}
@app.post('/v1/tools/execute')
def run(c:ToolCall,x_nexus_key:str|None=Header(default=None)):
 auth(x_nexus_key)
 try: return {'ok':True,'result':execute(c.tool,c.arguments)}
 except Exception as e: raise HTTPException(400,str(e))
@app.get('/v1/system')
def system(): return {'api_key':masked(),'lan':False,'remote':False}
@app.get('/v1/test/smoke')
def test(x_nexus_key:str|None=Header(default=None)): auth(x_nexus_key); return smoke()
