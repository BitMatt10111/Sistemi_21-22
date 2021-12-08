import socket as sck

def main():
    s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
    s.bind(('0.0.0.0',8000))
    nick_ip_dict={}

    while True:
        data, addr = s.recvfrom(4096)
        msg=data.decode()
        specs=msg.split("\n")
        print(specs)
        if specs[0].lower()=="nickname" and specs[1]!="":
                nick_ip_dict[specs[1]]=addr
                print(nick_ip_dict)
                s.sendto("ok".encode(),addr)
        if len(specs)==3:
            for user in nick_ip_dict.keys():
                if user==specs[1]:
                    print(f"{specs[0]} manda a {specs[1]}: {specs[2]}")
                    s.sendto(data, nick_ip_dict[user])
    
if __name__=="__main__":
    main()
