import socket as sck

def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    s.bind(('0.0.0.0',1123))
    nick_ip_dict={}

    while True:
        data, addr = s.recvfrom(4096)
        msg=data.decode()
        specs=msg.split(":")
        print(specs)
        if len(msg)>9:
            if specs[0]=="NICKNAME" and specs[1]!=" ":
                nick_ip_dict[specs[1]]=addr[0]
                print(nick_ip_dict)
                s.sendto("OK".encode(),addr)
    
if __name__=="__main__":
    main()