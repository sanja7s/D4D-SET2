'''
Created on Nov 26, 2012

@author: sscepano
'''
from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np


def num_visited_locations(um):
    nvl = np.zeros(150)
    #get_nvl = nvl.get
    test = []
    test2 = []
    max = 0
    total_users = len(um)
    
    for user in um.iterkeys():
        count = 0
        count = len(um[user])
        nvl[count] += 1
#        for ant in um[user].iterkeys():
#            count += len(um[user][ant])
#        #nvl[count] = get_nvl(count, 0)
#        nvl[count] += 1  
#        test.append(count)
        
        if count > max:
            max = count
            user_max = user
#        if count >= 1200: 
#            print ('Mnogoposjetni lik sam ja ',user)      
    #print nvl
    #print len(nvl)
    print max
    print user_max
    
        
    
#    print um[111]
#    print len(um[111][610])
    
    #plt.hist(test2, 200, normed=1, facecolor='green', alpha=0.75)  
    for i in range(150):
        print i
        print nvl[i]
        nvl[i] = nvl[i]/total_users
    print(len(nvl))
    #fig = plt.figure()  
    plt.plot(nvl, 'co')
    plt.yscale('log')
    plt.xscale('log')
    #ax = fig.add_subplot(2,1,1)
    #ax.plot(nvl, 'co')
    #ax.set_yscale('log')
    plt.show()   
    
    return nvl