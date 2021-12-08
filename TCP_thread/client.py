#tcp
#f"!list" -> f"list:{dict.keys()}"

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
    s.connect(('localhost',1123))
    receiver=Recv_Manager(s)
    receiver.start()

    n= input("Inserisci il nickname: ")
    s.sendall(f"nickname:{n}".encode())

    while True:
        opz=int(input("Inserisci opz:\n"))
        if opz==0:
            m=input()
            d=input()
            msg=input()
            s.sendall(f"{m}:{d}:{msg}".encode())
        elif opz==1:
            s.sendall(f"!list".encode())

if __name__=="__main__":
    main()