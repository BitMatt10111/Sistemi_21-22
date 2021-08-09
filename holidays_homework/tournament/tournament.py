'''
Name: Matteo Lamberti
Date: 01/08/21

Tally the results of a small football competition.
Based on an input file containing which team played
against which and what the outcome was,
create a file with a table like this:

Team                           | MP |  W |  D |  L |  P
Devastating Donkeys            |  3 |  2 |  1 |  0 |  7
Allegoric Alaskans             |  3 |  2 |  0 |  1 |  6
Blithering Badgers             |  3 |  1 |  0 |  2 |  3
Courageous Californians        |  3 |  0 |  1 |  2 |  1
'''

def file_reader(fn):
    file = open(fn,"r")
    matches=[]
    for i,row in enumerate(file):
        matches.append(row[:-1].split(","))
    return matches

def dict_creator(m):
    table_dict={}
    for match in m:
        if not match[0] in table_dict:
            table_dict[match[0]]=[0,0,0,0,0]
        if not match[1] in table_dict:
            table_dict[match[1]]=[0,0,0,0,0]
        table_dict[match[0]][0]+=1
        table_dict[match[1]][0]+=1
        if match[2]>match[3]:
            table_dict[match[0]][1]+=1
            table_dict[match[1]][3]+=1
        elif match[2]<match[3]:
            table_dict[match[0]][3]+=1
            table_dict[match[1]][1]+=1
        else:
            table_dict[match[0]][2]+=1
            table_dict[match[1]][2]+=1
    for team in table_dict:
        table_dict[team][4]=(table_dict[team][1]*3)+(table_dict[team][2])
    return table_dict
            
def main():
    matches=file_reader("matches.csv")
    table_dict=dict_creator(matches)
    print(table_dict)

if __name__=="__main__":
    main()