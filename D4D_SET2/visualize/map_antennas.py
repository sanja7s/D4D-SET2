'''
Created on Nov 5, 2012

@author: sanja7s
'''
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.basemap import Basemap
from read_in_data import antennas_graph
import matplotlib.pyplot as plt
import networkx as nx
import os.path
#import matplotlib.cm as cm

#matplotlib.use('Agg')

#from matplotlib.figure import Figure

# we take info from the read_in antenna graph
#aG = weights_links.read_in_link_weights()
aG = antennas_graph.read_in_antennas()

# we read data exported from Gephi AntennasWeighted Modules.gml -- processed to have colors for modularity classes
#dataPath = os.path.join((os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]),'csv/5 mc_pagerank_count 7.gml')
#G = nx.read_gml(dataPath)

def plot_movements_on_map(G):
    # set up Basemap lower left corner  coordinates (lon, lat)
    # and upper right corner
    # res and type of projection from offered by Basemap
    # center of the map coordinates are in lon_0 and lat_0
    # we found these to match Ivory Coast
    m = Basemap(llcrnrlon=-9, \
                llcrnrlat=3.8, \
                urcrnrlon=-1.5, \
                urcrnrlat = 11, \
                resolution = 'h', \
                projection = 'tmerc', \
                lat_0 = 7.38, \
                lon_0 = -5.30)
    
    # the figure we will save
    fig = plt.figure()
    canvas = FigureCanvas(fig)
    m.ax = fig.add_axes([0, 0, 1, 1])
    fig.set_figheight(8) 
    fig.set_figwidth(8/m.aspect)
    
    # we will use these coordinates for plotting data
    lats = []
    lons = []
    name = []
    usr = 0
    i = 0
    
    # we read id and lon and lat coordinates for every node
    for edge in G.edges_iter(data=True):
        node1 = edge[0]
        node2 = edge[1]
        usr = edge[2]['user']
        n1 = aG.node[node1]
        n2 = aG.node[node2]
        lon1 = n1['lon']
        lat1 = n1['lat']
        lon2 = n2['lon']
        lat2 = n2['lat']
        an = []
        #print(col)
        lats.append(float(lat1))
        lons.append(float(lon1))
        lats.append(float(lat2))
        lons.append(float(lon2))
        an.append(node1)
        an.append(node2)
        name.append(usr)
        #sizes7s.append(siz)
        i = i + 1
    # convert lons and lats from degrees to Basemap required meter values   
    x, y = m(lons, lats)
    m.drawcoastlines(color='gray')
    m.drawcountries(color='gray')
    #m.fillcontinents(color='beige')
    # we draw blue circles
    #cm.register_cmap(name='choppy', data=color7s)
    #m.scatter(x, y, color='green')
    m.plot(x, y)
    m.scatter(x, y, color='green', )
    #plt.title('sanjas i dace Bog')
    #plt.show()
#    for name, xc, yc in zip(an, x, y):
#    # draw the pref name in a yellow (shaded) box
#        plt.text(xc+3, yc-3, name,bbox=dict(facecolor='beige', alpha=0.2))
    
    mapPath = os.path.join((os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]),'maps')
    
    canvas.print_figure(mapPath + '/POS_SAMPLE_0_' + str(usr) + 'walk.png', dpi=100)
    # ex to try plt.title('Atlantic Hurricane Tracks (Storms Reaching Category 4, 1851-2004)')
    print('Map saved to file: ' + mapPath + '/POS_SAMPLE_0_' + str(usr) + 'walk.png')


