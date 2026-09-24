import socket
def port_available(host="127.0.0.1",port=8765):
 s=socket.socket(); 
 try:s.bind((host,port));return True
 except OSError:return False
 finally:s.close()
