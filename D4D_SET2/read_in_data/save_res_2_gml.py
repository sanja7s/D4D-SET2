'''
Created on Nov 19, 2012

@author: sscepano
'''
import networkx as nx
import os.path
import users_movements_v2

test_users = [937, 30765, 1110]
usr_mov = users_movements_v2.read_in_seq_usrs_mov()

gmlPath = os.path.join((os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]),'gml')

for usr in test_users:
    usrG = users_movements_v2.single_usr_graph_mov(usr, usr_mov)
    nx.write_gml(usrG, gmlPath + '/' + str(usr) + 'mov.gml')