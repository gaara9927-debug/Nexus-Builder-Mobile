BOARDS={"esp32":{"language":"cpp"},"arduino":{"language":"cpp"},"pico":{"language":"cpp"}}
def project(board):
 if board not in BOARDS: raise ValueError("unsupported board")
 return {"board":board,"physical_test":"BLOCKED","reason":"hardware required","profile":BOARDS[board]}
