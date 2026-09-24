import unittest
from nexus.tools import create,read,hash_file,safe
class Tests(unittest.TestCase):
 def test_roundtrip(self):
  create('unit/a.txt','abc'); self.assertEqual(read('unit/a.txt'),'abc'); self.assertEqual(len(hash_file('unit/a.txt')),64)
 def test_escape(self):
  with self.assertRaises(PermissionError): safe('../outside.txt')
if __name__=='__main__': unittest.main()
