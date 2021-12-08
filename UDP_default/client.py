import socket as sck

def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    nick=input()
    n=f"NICKNAME:{nick}".encode()
    s.sendto(n,("localhost",8000))
    data,addr=s.recvfrom(4096)
    if data.decode() == "OK":
        print("T'apposto")
        s.close()
    

if __name__=="__main__":
    main()