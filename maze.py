from PIL import Image 
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict

im = Image.open("./images_in/tiny.png")

class Maze:

    def __init__ (self,im):
        
        self.im = im 
        self.imdata = np.asarray(im)
        self.imdatav = np.rot90(self.imdata)
        self.start = None
        self.node = []
        self.width = self.im.size[0]
        self.height  = self.im.size[1]
        self.G = nx.Graph()
        self.node_data = self.G.nodes.data("pos")
        self.end = None 

        for pos , cell in np.ndenumerate(self.imdata):

            if cell == 1 :

                if pos[0] == 0 :

                    self.start = pos

                elif pos[0] == self.height-1 :
                
                    self.end = pos

                if pos != self.end :

                    self.position = [(self.imdata[pos[0]-1 , pos[1]]) , (self.imdata[pos[0]+1 , pos[1]]), 
                                    (self.imdata[pos[0] , pos[1]+1]) ,(self.imdata[pos[0] , pos[1]-1])]
                    
                    if( (self.position[0]== 1) or (self.position[1]== 1) ) and ((self.position[2] == 1) or (self.position[3]== 1)) :

                        self.node.append(pos)
                        self.G.add_node(self.node.index(pos), pos = (pos[1] , pos[0]))

                    if Maze.__check(self,pos[0] , pos[1]):

                        self.node.append(pos)
                        self.G.add_node(self.node.index(pos), pos = (pos[1] , pos[0]))

        self.node.append(self.end)
        self.G.add_node(self.node.index(self.end), pos = (self.end[1] , self.end[0]))

       
        self.count = len(self.node)
        Maze.edge_add(self)

        #Maze.show_graph(self)


    def __check(self, y,x):

        neighbour = [None , None , None , None]

        for pos in range(len(self.position)) :

            if self.position[pos] == 0:

                neighbour[pos] = 1

        if neighbour.count(1) == 3:

            return True
 
    def edge_add(self):

        y = defaultdict(list)
        x = defaultdict(list)

        for i , pos in self.node_data:

            y[pos[1]].append(pos[0])
            x[pos[0]].append(pos[1])
            
        #print(x,y)
        for key , value in y.items() :

            for i in range(len(value)):

                if i < len(value)-1:

                    if value[i+1] != value[i] +1 :

                        if all(self.imdata[key][value[i]+1 : value[i+1]]) :

                            self.G.add_edge(self.node.index((key , value[i])) , self.node.index((key , value[i+1])) , weight = value[i+1]- value[i]+1 )
                    else :
                        self.G.add_edge(self.node.index((key , value[i])) , self.node.index((key , value[i+1])) , weight =1 )


        for key , value in x.items() :

            for i in range(len(value)):

                if i < len(value)-1:

                    if value[i+1] != value[i] +1 :

                        if all(self.imdatav[self.width-key-1][value[i]+1 : value[i+1]]) :

                            self.G.add_edge(self.node.index((value[i] ,key )) , self.node.index((value[i+1] , key)) , weight = value[i+1]- value[i]+1)

                    else :
                        self.G.add_edge(self.node.index((value[i] ,key)) , self.node.index((value[i+1] ,key)) , weight = 1)


    def show_graph(self):

        nx.draw(self.G, nx.get_node_attributes(self.G, 'pos'), node_size=300 , with_labels = True)
        self.pos=nx.get_node_attributes(self.G, 'pos')
        #print(pos)
        labels = nx.get_edge_attributes(self.G,'weight')
        nx.draw_networkx_edge_labels(self.G,self.pos,edge_labels=labels)
        plt.gca().invert_yaxis()
        plt.show()


