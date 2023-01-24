# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 10:39:47 2022

@author: 20pt04
"""


import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class GraphVisualization:
    
    
    def __init__(self,vertices):
        self.edges = []
        self.adj = defaultdict(list)
        self.vertices = vertices
        self.num_edges=0
	
        
    def addEdge(self, a, b):
        temp = [a, b]
        self.adj[a].append(b)
        self.edges.append(temp)
        self.num_edges+=1
		
    def visualize(self):
        G = nx.Graph()
        edge_colors = ['grey']*10
        G.add_edges_from(self.edges)
        nx.draw_networkx(G,edge_color=edge_colors)
        plt.show()
        
    def print_path(self,b,e):     
        unvisited=[]
        path=[]
        path_edges=[]
        self.breadth_first_search(b,e,unvisited,path,path_edges)
        
        
    def breadth_first_search(self,b,e,unvisited,path,path_edges):
        
        node=b
        unvisited.append(b)
        while(node!=e and len(unvisited)>0):
            
            node=unvisited.pop(0)
            path.append(node)
            for i in self.adj[node]:
                if i not in unvisited and i not in path:
                    unvisited.append(i)
                    path_edges.append([node,i])
        
        print(path)
        print(path_edges)
        G1 = nx.Graph()
        G1.add_edges_from(self.edges)
        edge_colors=['green' if [e[0],e[1]] in path_edges or [e[1],e[0]] in path_edges else 'red' for e in G1.edges]
        #print(edge_colors)
        nx.draw_networkx(G1,edge_color=edge_colors)

        plt.show()
        
        
    
    
    
# Driver code
G = GraphVisualization(20)
G.addEdge(0, 3)
#G.addEdge(3, 0)

G.addEdge(1, 0)
#G.addEdge(0, 1)

G.addEdge(1, 2)
#G.addEdge(2, 1)

G.addEdge(1, 4)
#G.addEdge(4, 1)

G.addEdge(2, 7)
#G.addEdge(7, 2)

G.addEdge(3, 5)
#G.addEdge(5, 3)

G.addEdge(3, 4)
#G.addEdge(4, 3)

G.addEdge(4, 6)
#G.addEdge(6, 4)

G.addEdge(5, 6)
#G.addEdge(6, 5)

G.addEdge(6, 7)
#G.addEdge(7, 6)


G1 = GraphVisualization(13)
adj=[[0,2],[0,3],[0,1],[2,4],[3,5],[3,6],[1,3],[4,7],[4,5],[5,2],[6,5],[7,5],[7,8]]
for i in adj:
    G1.addEdge(i[0], i[1])

G1.visualize()
G1.print_path(1, 8)        


