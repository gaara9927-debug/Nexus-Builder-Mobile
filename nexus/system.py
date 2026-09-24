import os,platform,shutil
def snapshot():
    total,used,free=shutil.disk_usage(".")
    return {"platform":platform.system(),"machine":platform.machine(),"cpu_cores":os.cpu_count(),
            "storage_total":total,"storage_free":free}
