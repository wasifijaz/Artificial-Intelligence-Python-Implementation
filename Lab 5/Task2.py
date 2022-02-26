# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 15:31:38 2021

@author: Dell
"""

class Graph:
    def __init__(self, graph = None):
        if graph == None:
            graph = {}
        self.__graph = graph
        
    def find_shortest_path(self, start, end, path = []):
        path = path + [start]
        if start == end:
            return path
        shortest = None
        for node in self.__graph[start]:
            if node not in path:
                newpath = self.find_shortest_path(node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

    def find_all_paths(self, start, end, path = []):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in self.__graph[start]:
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
    
    def degree_of_nodes(self):
        for i in self.__graph.items():
            print("Degree of Node ", i[0], " = ", len(i[1]))
    
    def print_graph(self):
        print("\nGraph:")
        for key, value in self.__graph.items():
            print("\t",key, ' : ', value)
        print("\n")


g = { '1' : ['2','5'],
          '2' : ['1','3','5'],
          '3' : ['2','4'],
          '4' : ['3','5','6'],
          '5' : ['1','2','4'],
          '6' : ['4']
          }
    
graph = Graph(g)
graph.print_graph()
graph.degree_of_nodes()
print("\nShortest path from 6 to 1: ", graph.find_shortest_path('6', '1'))
print("\nAll paths from 6 to 1: ", graph.find_all_paths('6', '1'))
