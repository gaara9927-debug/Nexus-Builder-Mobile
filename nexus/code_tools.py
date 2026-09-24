import ast,json
from .tools import create,read
def generate_template(kind,name):
 if kind=="python":
  return create(name+"/main.py","def main():\n    print('Hello from Nexus')\n\nif __name__ == '__main__':\n    main()\n")
 if kind=="web":
  return create(name+"/index.html","<!doctype html><meta name='viewport' content='width=device-width'><title>Nexus App</title><h1>Hello from Nexus</h1>")
 raise ValueError("unsupported template")
def validate_python(path):
 src=read(path); ast.parse(src); return {"valid":True}
def validate_json(path):
 json.loads(read(path)); return {"valid":True}
