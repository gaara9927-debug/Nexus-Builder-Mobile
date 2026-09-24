from .tools import execute
def smoke():
 out=[]
 try:
  execute('file.create',{'path':'tests/smoke.txt','content':'nexus'})
  out.append({'test':'file roundtrip','status':'PASS' if execute('file.read',{'path':'tests/smoke.txt'})=='nexus' else 'FAIL'})
  out.append({'test':'sha256','status':'PASS' if len(execute('file.hash',{'path':'tests/smoke.txt'}))==64 else 'FAIL'})
 except Exception as e: out.append({'test':'tool smoke','status':'FAIL','error':str(e)})
 return {'results':out,'release_ready':all(x['status']=='PASS' for x in out)}
