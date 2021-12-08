import socket as sck
import threading as thr
 
class Recv_Manager(thr.Thread): 
    def __init__(self,socket): 
        thr.Thread.__init__(self) #super di Java 
        self.socket=socket 
        self.running=True 
    def run(self): 
        while self.running: 
            received_msg=self.socket.recv(4096).decode()
            print(received_msg) #riceve il messaggio di risposta
            
def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.connect(('localhost',2223))
    receiver=Recv_Manager(s)
    receiver.start()

    print("Operazioni possibili:\n 1-Chiedere al server se un certo nome file è presente;\n 2-Chiedere al server il numero di frammenti di un file a partire dal suo nome file;\n 3-Chiedere al server l’IP dell’host che ospita un frammento a partire nome file e dal numero del frammento;\n 4-Chiedere al server tutti gli IP degli host sui quali sono salvati i frammenti di un file a partire dal nome file.")

    while True:
        ris=input("\nSeleziona un numero di operazione: ") #chido il numero dell'operazione sopra indicate
        nFram="NULL"
        if ris == "1" or ris == "2" or ris == "4":
            nomeFile=input("File da cercare: ")
        elif ris == "3": #se è l'operazione è la tre serve anche il numero del frammento
            nomeFile=input("File di appartenenza: ")
            nFram=input("Numero del frammento: ")
        s.sendall(f"{ris}§{nomeFile}§{nFram}".encode()) #manda il messaggio nel formato nuemroDiOperazione§nomeFile§numeroFrammento(eventuale)

if __name__=="__main__":
    main()