import asyncio
async def probe(url,timeout=5):
 try:
  import websockets
 except ImportError:return {"status":"BLOCKED","reason":"websockets package unavailable"}
 try:
  async with asyncio.timeout(timeout):
   async with websockets.connect(url) as ws:return {"status":"CONNECTED"}
 except Exception as e:return {"status":"FAIL","error":type(e).__name__}
