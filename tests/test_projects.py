import unittest,uuid
from nexus.projects import create,tree,backup
from nexus.tools import create as file_create
class ProjectTests(unittest.TestCase):
 def test_project_flow(self):
  n="p-"+uuid.uuid4().hex[:8]; create(n); file_create(n+"/main.js","console.log('ok')")
  self.assertIn("main.js",tree(n)); self.assertIn("backup",backup(n))
if __name__=="__main__": unittest.main()
