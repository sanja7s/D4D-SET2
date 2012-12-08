'''
Created on Nov 1, 2012

@author: sanja7s
'''
from os.path import join
import networkx as nx

def read_in_antennas():

    D4DPath = "/home/sscepano/DATA SET7S/D4D"
    file7s = "ANT_POS.TSV"
    f = open(join(D4DPath,file7s), 'r')
    
    aG = nx.DiGraph()
    
    for line in f:
        sid, slon, slat = line.split('\t')
        aid = int(sid)
        alon = float(slon)
        alat = float(slat[:-1])
        aG.add_node(aid, lon = alon, lat = alat)
        
    return aG
    
    
