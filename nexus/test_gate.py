import unittest,time,json
from pathlib import Path
def run():
 t=time.time(); suite=unittest.defaultTestLoader.discover("tests")
 result=unittest.TextTestRunner(verbosity=2).run(suite)
 report={"tests":result.testsRun,"failures":len(result.failures),"errors":len(result.errors),"skipped":len(result.skipped),"duration":round(time.time()-t,3),"status":"PASS" if result.wasSuccessful() else "FAIL"}
 Path("NEXUS_VALIDATION_REPORT.json").write_text(json.dumps(report,indent=2))
 return report
if __name__=="__main__":
 r=run(); raise SystemExit(0 if r["status"]=="PASS" else 1)
