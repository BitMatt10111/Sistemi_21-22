import threading as thr
import socket as sck

class Recv_Manager(thr.Thread):
    def __init__(self,s):
        thr.Thread.__init__(self)
        self.s=s
        self.running=True
    def run(self):
        while self.running:
            msg, _= self.s.recvfrom(4096)
            print(msg.decode())

def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    n=input()
    s.sendto(f"nickname\n{n}".encode(),("192.168.0.126",5000))
    receiver=Recv_Manager(s)
    receiver.start()
    while True:
        m=input()
        d=input()
        msg=input()
        s.sendto(f"{m}\n{d}\n{msg}".encode(),("192.168.0.126",5000))
        

if __name__=="__main__":
    main()