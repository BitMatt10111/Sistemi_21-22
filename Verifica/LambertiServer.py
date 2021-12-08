import socket as sck
import threading as thr 
import sqlite3 #libreria per sqlite

class Client_Manager(thr.Thread):
    def __init__(self,connection,address):
        thr.Thread.__init__(self) #super di Java
        self.connection=connection
        self.address=address
        self.running=True
    
    def run(self):
        while self.running:
            msg=self.connection.recv(4096).decode() #aspetta di ricevere un messaggio (nome del comando) dal client
            msg = msg.split("§") # il messaggio è formattato nuemroDiOperazione§nomeFile§numeroFrammento(eventuale)
            nf=str(msg[1])
            nfr=str(msg[2])
            query={"1":"SELECT nome FROM files", #dizionario che contiene tutte le query
            "2":f"SELECT count(*) FROM files,frammenti WHERE files.id_file=frammenti.id_file and nome='{nf}' group by nome",
            "3":f"SELECT host FROM files,frammenti WHERE files.id_file=frammenti.id_file and nome='{nf}' and frammenti.n_frammento='{nfr}'",
            "4":f"SELECT host FROM files,frammenti WHERE files.id_file=frammenti.id_file and nome='{nf}'"}
            conn = sqlite3.connect("file.db") #crea una "connessione" col database
            cur = conn.cursor()  
            cur.execute(query[msg[0]]) #a seconda dell'operazione selezionata fa una determinata query
            if msg[0]=="1":
                dati = cur.fetchall()[0][0]
                if nf == dati:
                    risposta="Il file è presente"
            elif msg[0]=="2":
                dati = cur.fetchall()[0][0]
                risposta=str(dati)
            elif msg[0]=="3":
                #creazione messaggio risposta
                pass
            elif msg[0]=="4":
                #creazione messaggio risposta
                pass
            print(dati)
            self.connection.sendall(risposta.encode()) #invia la risposta al client
            cur.close()

def main():
    
    s=sck.socket(sck.AF_INET,sck.SOCK_STREAM) #prepara il socket per la trasmissione tcp 
    s.bind(("localhost",2223))
    s.listen() #si mette in ascolto per un client che si connette

    while True:
        
        connection, address=s.accept() #accetta la connessione
        client=Client_Manager(connection,address) #crea il thread per gestire il client
        client.start() #avvia il thread client

if __name__=="__main__":
    main()