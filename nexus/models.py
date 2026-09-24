from pathlib import Path
MODELS=Path(".nexus/models")
def list_models():
 MODELS.mkdir(parents=True,exist_ok=True)
 return [{"name":p.name,"bytes":p.stat().st_size,"status":"AVAILABLE"} for p in MODELS.glob("*.gguf")]
def runtime_status():
 return {"backend":"GGUF","loaded":None,"status":"NOT_CONFIGURED","note":"No model is claimed loaded until a real runtime passes validation."}
