import socket as sck
import threading as thr
nick_ip_dict={}

class Client_Manager(thr.Thread):
    def __init__(self,connection,address):
        thr.Thread.__init__(self) #super di Java
        self.connection=connection
        self.address=address
        self.running=True
    def run(self):
        while self.running:
            data=self.connection.recv(4096)
            msg=data.decode()
            
            if msg=="!list":
                self.connection.sendall(str(nick_ip_dict.keys()).encode())
            else:
                specs=msg.split(":")
                if specs[0].lower()=="nickname" and specs[1]!="":
                    nick_ip_dict[specs[1]]=self
                    self.connection.sendall("ok".encode())
                if len(specs)==3:
                    for user in nick_ip_dict.keys():
                        if user==specs[1]:
                            print(f"{specs[0]} manda a {specs[1]}: {specs[2]}")
                            nick_ip_dict[user].connection.sendall(data)

def main():
    s = sck.socket(sck.AF_INET,sck.SOCK_STREAM)
    s.bind(("127.0.0.1",1123))
    s.listen()

    while True:
        connection, address=s.accept()
        client=Client_Manager(connection,address)
        client.start()

if __name__=="__main__":
    main()