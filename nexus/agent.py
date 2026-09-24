from enum import Enum
from .tools import execute
class AgentState(str,Enum):
 WAITING="WAITING"; PLANNING="PLANNING"; RUNNING="RUNNING"; TESTING="TESTING"; VERIFYING="VERIFYING"; FAILED="FAILED"; COMPLETED="COMPLETED"
class Agent:
 def __init__(self): self.state=AgentState.WAITING; self.history=[]
 def run_tool(self,name,args):
  self.state=AgentState.RUNNING
  try:
   result=execute(name,args); self.history.append({"tool":name,"ok":True}); self.state=AgentState.COMPLETED; return result
  except Exception as e:
   self.history.append({"tool":name,"ok":False,"error":str(e)}); self.state=AgentState.FAILED; raise
