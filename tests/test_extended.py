import unittest,uuid
from nexus.code_tools import generate_template,validate_python
from nexus.db import create as dbcreate,query
from nexus.robotics import project
class Extended(unittest.TestCase):
 def test_code(self):
  n="code-"+uuid.uuid4().hex[:6]; generate_template("python",n); self.assertTrue(validate_python(n+"/main.py")["valid"])
 def test_db(self):
  p="db-"+uuid.uuid4().hex[:6]+".sqlite"; dbcreate(p); self.assertEqual(query(p,"pragma user_version")["rows"][0][0],0)
 def test_robot_blocked(self): self.assertEqual(project("esp32")["physical_test"],"BLOCKED")
if __name__=="__main__": unittest.main()
