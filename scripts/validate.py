import json,unittest
from pathlib import Path
suite=unittest.defaultTestLoader.discover("tests")
res=unittest.TextTestRunner(verbosity=2).run(suite)
report={"tests_run":res.testsRun,"failures":len(res.failures),"errors":len(res.errors),
        "status":"PASS" if res.wasSuccessful() else "FAIL","release_ready":False}
Path("NEXUS_VALIDATION_REPORT.json").write_text(json.dumps(report,indent=2),encoding="utf-8")
print(json.dumps(report,indent=2))
