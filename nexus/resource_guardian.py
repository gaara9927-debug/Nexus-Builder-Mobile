import os
def policy(available_ram=None):
 if available_ram is None: return {"parallel_heavy":1,"mode":"SAFE"}
 gb=available_ram/(1024**3)
 return {"parallel_heavy":1 if gb<4 else 2,"mode":"LOW" if gb<2 else "MEDIUM" if gb<6 else "HIGH"}
