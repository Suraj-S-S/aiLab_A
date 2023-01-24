# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 11:23:13 2022

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
        visited=[False for i in range(self.vertices)]
        path=[]
        edges=[]
        for i in range(0,self.vertices):
            if(self.depth_limited_search(b,e,visited,path,edges,i)):
                print('Found at depth : ',i)
                return
        
        print('Path not found')
        
    def depth_limited_search(self,b,e,visited,path,edges,depth):
        
        visited[b]=True
        path.append(b)
        
        if(b==e):
            print(path)
            print(edges)
            
            G1 = nx.Graph()
            G1.add_edges_from(self.edges)
            edge_colors=['green' if [e[0],e[1]] in edges or [e[1],e[0]] in edges else 'red' for e in G1.edges]
            #print(edge_colors)
            nx.draw_networkx(G1,edge_color=edge_colors)

            plt.show()
            return True
            
        else : 
            if depth>0:
                for i in self.adj[b]:
                    if(visited[i]==False):
                        t=[b,i]
                        edges.append(t)
                        return self.depth_limited_search(i,e,visited,path,edges,depth-1)
                        edges.pop()
        path.pop()
        visited[b]=False
        
            
    
        
G = GraphVisualization(20)
G.addEdge(0, 3)
G.addEdge(3, 0)

G.addEdge(1, 0)
G.addEdge(0, 1)

G.addEdge(1, 2)
G.addEdge(2, 1)

G.addEdge(1, 4)
G.addEdge(4, 1)

G.addEdge(2, 7)
G.addEdge(7, 2)

G.addEdge(3, 5)
G.addEdge(5, 3)

G.addEdge(3, 4)
G.addEdge(4, 3)

G.addEdge(4, 6)
G.addEdge(6, 4)

G.addEdge(5, 6)
G.addEdge(6, 5)

G.addEdge(6, 7)
G.addEdge(7, 6)
    
    


G1 = GraphVisualization(13)
adj=[[0,2],[0,3],[0,1],[2,4],[3,5],[3,6],[1,3],[4,7],[4,5],[5,2],[6,5],[7,5],[7,8]]
for i in adj:
    G1.addEdge(i[0], i[1])

G.visualize()       

G.print_path(0,7)
