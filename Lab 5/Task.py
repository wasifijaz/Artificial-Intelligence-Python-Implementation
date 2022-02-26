# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 13:21:07 2021

@author: Dell
"""
def find_all_paths(graph, start, end, path =[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def print_graph(graph):
    print("\nGraph:")
    for key, value in graph.items():
        print("\t",key, ' : ', value)
    print("\n")

graph = { '1' : ['2','5'],
          '2' : ['1','3','5'],
          '3' : ['2','4'],
          '4' : ['3','5','6'],
          '5' : ['1','2','4'],
          '6' : ['4']
         }

print_graph(graph)
print("All paths from 6 to 1: ", find_all_paths(graph, '6', '1'))

"""
def find_shortest_path(graph, start, end, path =[]):
        path = path + [start]
        if start == end:
            return path
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest
    
def degree_of_nodes(graph):
    for i in graph.items():
        print("Degree of Node ", i[0], " = ", len(i[1]))



degree_of_nodes(graph)
print("Shortest path from 6 to 1: ", find_shortest_path(graph, '6', '1'))


"""
