import unittest,uuid
from nexus.filesystem import write,edit,copy,move,listdir,info,compress
from nexus.image_tools import svg
from nexus.termux import status
from nexus.server import port_available
class Catalog(unittest.TestCase):
 def test_files(self):
  n="cat-"+uuid.uuid4().hex[:6];write(n+"/a.txt","a");edit(n+"/a.txt","a","b");copy(n+"/a.txt",n+"/b.txt");move(n+"/b.txt",n+"/c.txt");self.assertTrue(info(n+"/c.txt")["file"]);compress(n,n+".zip");self.assertTrue(info(n+".zip")["file"])
 def test_svg(self):
  p="img-"+uuid.uuid4().hex[:6]+".svg";self.assertGreater(svg(p)["bytes"],20)
 def test_system_tools(self): self.assertIsInstance(status(),dict);self.assertIsInstance(port_available(port=0),bool)
