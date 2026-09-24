import os,shutil
def status(): return {"detected":bool(os.getenv("PREFIX","").find("com.termux")>=0 or shutil.which("termux-info")),"node":bool(shutil.which("node")),"python":bool(shutil.which("python")),"git":bool(shutil.which("git"))}
