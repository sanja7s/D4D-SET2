'''
Created on Nov 21, 2012

@author: sscepano
'''

from collections import OrderedDict


#from IPython.Shell import IPShellEmbed
#ipshell = IPShellEmbed()
#
#        
#i = 0
# 
#print 'hi'
#       
#ipshell()
#
#i = i + 1
#
#print 'bye'
#
#ipshell()
#
#def process_one_item(item):
#        return item.x > 19 or item.x < 5
# 
# 
#reduce(lambda x,y: x+y, map(process_one_item, items)

#import dateutil.parser
#      
#      
#def find_home(usr_mov):
#    usr_night = {}
#    
#    
#    for usr in usr_mov.iterkeys():
#        
#        usr_night[usr] = {}
#        
#        for ant in usr_mov[usr].iterkeys():
#            
#            get_usr_night_ant = usr_night[usr].get
#            usr_night[usr][ant] = get_usr_night_ant(ant,0)
#            
#            for call_time in usr_mov[usr][ant]:
#                dt = dateutil.parser.parse(call_time)
#                dh = dt.hour
#                if dh > 19 or dh < 5:
#                    usr_night[usr][ant] += 1
#                    
#    print usr_mov[1100]


def filter_users():
    return None 
fq = 0.25
fileout = 'Usr_call_fq' + str(fq) + '.tsv'
fileout2 = 'OnlyFQ_Usr_call_fq' + str(fq) + '.tsv'


def find_usr_call_fq(um):
    ucf = [float] * 500000
    fout = open(fileout, 'w')
    fout2 = open(fileout2, 'w')
    um2 = {}
    i = 0
    i2 = 0
    print(len(um))
    for usr in um.iterkeys():
        ucf[usr] = 0
        if (len(um[usr]) >= 2):
            i = i + 1
            for ant in um[usr].iterkeys():
                ucf[usr] += len(um[usr][ant])
            ucf[usr] = ucf[usr] / (7.0*24.0*2.0)
            fout.write(str(usr) + '\t' + str(ucf[usr]) + '\n')
            if ucf[usr] >= fq:
                um2.keys().append(usr)
                um2[usr] = um[usr]        
                i2 = i2 + 1
                fout2.write(str(usr) + '\t' + str(ucf[usr]) + '\n')
    fout.close()
    fout2.close()
    print('All fq saved to file ' + fileout)
    print('Those that at least 2 antenna calls: ' + str(i))
    print('Only fq saved to file ' + fileout2)    
    print('Found ' + str(i2) + ' frequent callers (fq >= ' + str(fq) + ')')
    return um2
  
    