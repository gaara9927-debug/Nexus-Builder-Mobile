import unittest
from nexus.tools import safe
from nexus.local_ai import LocalAIRuntime
class Security(unittest.TestCase):
 def test_traversal_blocked(self):
  with self.assertRaises(PermissionError): safe("../../etc/passwd")
 def test_missing_model_blocked(self):
  self.assertEqual(LocalAIRuntime().inspect("definitely-missing.gguf")["status"],"BLOCKED")
if __name__=="__main__": unittest.main()
