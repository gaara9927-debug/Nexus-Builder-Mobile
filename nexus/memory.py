import sqlite3
from pathlib import Path
DB=Path('.nexus/memory.db')
def init():
 DB.parent.mkdir(exist_ok=True)
 with sqlite3.connect(DB) as c: c.execute('CREATE TABLE IF NOT EXISTS memory(id INTEGER PRIMARY KEY,scope TEXT,key TEXT,value TEXT,UNIQUE(scope,key))')
def put(scope,key,value):
 init()
 with sqlite3.connect(DB) as c: c.execute('INSERT INTO memory(scope,key,value) VALUES(?,?,?) ON CONFLICT(scope,key) DO UPDATE SET value=excluded.value',(scope,key,value))
def get(scope,key):
 init()
 with sqlite3.connect(DB) as c: r=c.execute('SELECT value FROM memory WHERE scope=? AND key=?',(scope,key)).fetchone()
 return r[0] if r else None
