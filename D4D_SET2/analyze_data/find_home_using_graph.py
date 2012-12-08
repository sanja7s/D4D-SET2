'''
Created on Nov 19, 2012

@author: sscepano
'''

import networkx as nx
from collections import OrderedDict
from read_in_data import users_movements_v2

test_users = [937]

usr_mov = users_movements_v2.read_in_seq_usrs_mov()

for usr in test_users:
    usrG = users_movements_v2.single_usr_graph_mov(usr, usr_mov)
    ant_times = usr_mov[usr]
    pr = nx.pagerank(usrG,alpha=0.9)
    opr = OrderedDict(sorted(pr.items(), key=lambda t: t[1], reverse=True))
    print(opr)
fileout = str(usr) + '.tsv'
fout = open(fileout, 'w')

for usr in test_users:
    fout.write(str(usr) + '\n')
    for mov in usr_mov[usr]:
        fout.write(str(mov) + '\t')
    fout.write('\n')
    
    for key in opr.keys():
        fout.write(str(key) + '\t' + str(opr[key]) + '\n')
        for time in ant_times[key]:
            fout.write(str(time) + '\n')
        
    
    
    
