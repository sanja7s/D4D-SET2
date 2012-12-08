'''
Created on Nov 21, 2012

@author: sscepano
'''

from read_in_data import user_movements_v2 as um
import dateutil.parser
from collections import OrderedDict

#import code; code.interact(local=locals())
#import pdb; pdb.set_trace()

#This is a very slow code

def find_home(usr_mov):
    #usr_mov = um.read_in_seq_usr_mov()
    usr_night = {}
    
    
    for usr in usr_mov.iterkeys():
        usr_night[usr] = {}
        for ant in usr_mov[usr].iterkeys():
            get_usr_night_ant = usr_night[usr].get
            usr_night[usr][ant] = get_usr_night_ant(ant,0)
            for call_time in usr_mov[usr][ant]:
                dt = dateutil.parser.parse(call_time)
                if dt.hour > 19 or dt.hour <= 5:
                    usr_night[usr][ant] += 1
               
    for usr in usr_night.iterkeys():
        usr_night[usr] = OrderedDict(sorted(usr_night[usr].items(), key=lambda t: t[1], reverse=True))   
    
    
    fileout = 'FQ_User_homes.tsv'    
    fout = open(fileout, 'w')    
    for usr in usr_night.iterkeys():
        fout.write(str(usr) + '\n')
        for ant in usr_night[usr].iterkeys():
            fout.write(str(ant) + ':\t' + str(usr_night[usr][ant]) + '\n')
            
    print ('Found Home locations saved under' + fileout)