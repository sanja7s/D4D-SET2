
from os import listdir
from os.path import isfile, join
from collections import OrderedDict
import antennas_graph
from visualize import map_antennas
import networkx as nx


def read_in_usr_mov_per_ant():
    # we have the nodes from the given antennas set with their positions (lon, lat)
    D4DPath_SET2 = "/home/sscepano/DATA SET7S/D4D/SET2TSVtest/"
    
    i = 0
    usr_mov = {}
    
    for fileName in listdir(D4DPath_SET2):
        fPath = join(D4DPath_SET2,fileName)
        if isfile(fPath) and fileName != '.DS_Store':
            file7s = open(fPath, 'r')
            for line in file7s:
                i = i + 1
                usr, datetime, antenna = line.split('\t')
                usr = int(usr)
                antenna = int(antenna[:-1])
                #if usr == 1: 
                    #print line
                get_usr = usr_mov.get
                usr_mov[usr] = get_usr(usr, {})
                get_ant = usr_mov[usr].get
                usr_mov[usr][antenna] = get_ant(antenna, [])
                usr_mov[usr][antenna].append(datetime)
                    
    #print i
    return usr_mov

def read_in_seq_usr_mov():
    # from here we read fine-grained user movements data
    D4DPath_SET2 = "/home/sscepano/DATA SET7S/D4D/SET2TSVtest/"
    usr_mov = {}
    
    # we read in files
    for fileName in listdir(D4DPath_SET2):
        fPath = join(D4DPath_SET2,fileName)
        if isfile(fPath) and fileName != '.DS_Store':
            file7s = open(fPath, 'r')
            for line in file7s:
                # line format is like this
                usr, datetime, antenna = line.split('\t')
                usr = int(usr)
                antenna = int(antenna[:-1])
                # to populate sequential dictionary which remembers moves in sequence for each user
                # we use dictionary helping function: get
                # to define empty list if key is not present and otherwise to append antenna and datetime
                if antenna <> -1:
                    get_usr = usr_mov.get
                    usr_mov[usr] = get_usr(usr, {})
                    get_usr_mov = usr_mov[usr].get
                    usr_mov[usr][antenna] = get_usr_mov(antenna, [])
                    usr_mov[usr][antenna].append(datetime)
                    
    return usr_mov
    
    

def find_ant_popularity_per_usr():            
                    
    usr_mov = read_in_usr_mov_per_ant()
    usr_pop_ant = {}
    
    for usr in usr_mov.keys():
        ant_data = usr_mov[usr]
        for antenna in ant_data.keys():
            popularity = len(ant_data[antenna])
            get_usr_pop_ant = usr_pop_ant.get
            usr_pop_ant[usr] = get_usr_pop_ant(usr, {})
            get_pop_ant = usr_pop_ant[usr].get
            usr_pop_ant[usr][antenna] = get_pop_ant(antenna, 0) + popularity
        
    ord_usr_pop_ant = {}               
    
    for usr in usr_pop_ant.keys():
        ord_usr_pop_ant[usr] = OrderedDict(sorted(usr_pop_ant[usr].items(), key=lambda t: t[1], reverse=True))        
        
    return ord_usr_pop_ant    

#def find_ant_times_per_user(usr, usr_mov):            
#                    
#    usr_ant_times = {}
#
#    ant_data = usr_mov[usr]
#    for antenna in ant_data.keys():
#        times = ant_data[antenna]
#        get_usr_ant_times = usr_ant_times.get
#        usr_ant_times[antenna] = get_usr_ant_times(antenna, [])
#        usr_ant_times[antenna].append(times)
#            
#    return usr_ant_times      

def save_usr_ant_popularity(fileout):
    
    ord_usr_pop_ant = find_ant_popularity_per_usr()
    fout = open(fileout, 'w')
    
    tl = 0
    tm = 0
    
    for usr in ord_usr_pop_ant.keys():
        fout.write(str(usr) + '::')
        l = len(ord_usr_pop_ant[usr].items())
        tl += l
        if l > tm:
            tm = l
        for ant in ord_usr_pop_ant[usr].keys():
            if l > 1:
                ant_cnt = ord_usr_pop_ant[usr][ant]
                if ant_cnt > 1:
                    fout.write('\t' + str(ant) + ':\t' + str(ant_cnt))
        fout.write('\n')
    avgl = tl / len(ord_usr_pop_ant.keys())
    fout.close()
    print ('Avg user per antenna ' , avgl)
    print ('Max antennas by one user ' , tm)
    print('Saved to file: ' + fileout)
    

def single_usr_graph_mov(usr, usr_mov):
#    # we have the nodes from the given antennas set with their positions (lon, lat)
#    aG = antennas_graph.read_in_antennas()
    # initialize variables
    i = 0
    antenna1 = -1
    antenna2 = -1
    usrG = nx.DiGraph()
    
    print(usr_mov[usr])
    # we use approach to connect every odd antenna to every following (even) antenna
    # (this way we can skip only the first antenna, if a user has only one antenna in his log. that user is not dynamic anyways.) 
    for ant in usr_mov[usr].keys():
        i = i + 1
        if (i % 2 == 1):
            antenna1 = ant
        if (i % 2 == 0):
            antenna2 = ant
        if antenna1 <> -1 and antenna2 <> -1:
            if usrG.has_edge(antenna1, antenna2):
                usrG[antenna1][antenna2]['weight']+=1
            else:
                usrG.add_edge(antenna1, antenna2, count = 0, user=usr)    
                
    return usrG
     
#fileout = 'User_FQ_per_antenna.tsv'    
#save_usr_ant_popularity(fileout)

#
#usr_mov = read_in_seq_usrs_mov()
#print (usr_mov[1110])

#usrG = single_usr_graph_mov(937, usr_mov)
#print(usrG.edges())
#map_antennas.plot_movements_on_map(usrG)
#usrG = single_usr_graph_mov(937, usr_mov)
#map_antennas.plot_movements_on_map(usrG)
#usrG = single_usr_graph_mov(1110, usr_mov)
#map_antennas.plot_movements_on_map(usrG)
#usrG = single_usr_graph_mov(41784, usr_mov)
#map_antennas.plot_movements_on_map(usrG)
#usrG = single_usr_graph_mov(41520, usr_mov)
#map_antennas.plot_movements_on_map(usrG)
#usrG = single_usr_graph_mov(49998, usr_mov)
#map_antennas.plot_movements_on_map(usrG)
#usrG = single_usr_graph_mov(30765, usr_mov)
#map_antennas.plot_movements_on_map(usrG)
#usrG = single_usr_graph_mov(22211, usr_mov)
#map_antennas.plot_movements_on_map(usrG)
#usrG = single_usr_graph_mov(220, usr_mov)
#map_antennas.plot_movements_on_map(usrG)
#usrG = single_usr_graph_mov(4400, usr_mov)
#map_antennas.plot_movements_on_map(usrG)
#print(usrG.number_of_edges())
#print(usrG.number_of_nodes())
#print(usrG.nodes())
#print(usrG.edges())
#map_antennas.plot_movements_on_map(usrG)

#usr_mov, aG = read_in_seq_user_mov_2graph()
#
#print(aG.nodes(data=True))
#print(aG.nodes(data=True)[2])
#print(aG.node[2])