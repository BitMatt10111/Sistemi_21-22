import socket as sck
import threading as thr

class Recv_Manager(thr.Thread):
    def __init__(self,socket):
        thr.Thread.__init__(self) #super di Java
        self.socket=socket
        self.running=True
    def run(self):
        while self.running:
            received_msg=self.socket.recv(4096)
            print(f"{received_msg.decode()}")

def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.connect(('127.0.0.1',1123))
    receiver=Recv_Manager(s)
    receiver.start()

    s.sendall(f"OK".encode())

    while True:
        comando = input("inserisci comando")
        s.sendall(comando.encode())
        
            

if __name__=="__main__":
    main()