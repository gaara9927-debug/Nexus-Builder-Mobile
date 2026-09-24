from pathlib import Path
import secrets
ROOT=Path('.nexus'); KEY=ROOT/'secret.key'
def get_key():
 ROOT.mkdir(exist_ok=True)
 if not KEY.exists(): KEY.write_text('nxs_'+secrets.token_urlsafe(32),encoding='utf-8')
 return KEY.read_text(encoding='utf-8').strip()
def masked(): return get_key()[:4]+'•'*16
