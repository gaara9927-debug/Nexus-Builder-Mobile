from dataclasses import dataclass
from .tools import execute,manifest
@dataclass
class Permission:
 level:str
TOOL_POLICY={"file.create":Permission("SAFE"),"file.read":Permission("SAFE"),"file.hash":Permission("SAFE")}
def route(name,args,confirmed=False):
 p=TOOL_POLICY.get(name,Permission("BLOCKED"))
 if p.level=="BLOCKED": raise PermissionError("tool not permitted")
 if p.level=="CONFIRM" and not confirmed: raise PermissionError("confirmation required")
 return execute(name,args)
def registry(): return [{**x,"permission":TOOL_POLICY.get(x["name"],Permission("BLOCKED")).level} for x in manifest()]
