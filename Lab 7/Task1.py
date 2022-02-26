# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 23:06:58 2021

@author: Dell
"""

class Graph(object):
    cost = {'Arad': [366],
            'Bucharest': [0],
            'Craiova': [160],
            'Dobreta': [242],
            'Eforie': [161],
            'Fagaras': [176],
            'Giurgiu': [77],
            'Hirsova': [151],
            'Lasi': [226],
            'Lugoj': [244],
            'Mehadia': [241],
            'Neamt': [234],
            'Oradea': [380],
            'Pitesti': [10],
            'Rimnicu Vilcea': [193],
            'Sibiu': [253],
            'Timisoara': [329],
            'Urziceni': [80],
            'Vaslui': [199],
            'Zerind': [374]
            }

    def __init__(self, graph_dict=None):
        if graph_dict == None:
           graph_dict = {}
        self.__graph_dict = graph_dict

    def print(self):
        return self.__graph_dict

    def get_neighbour(self,vertex):
        graph=self.__graph_dict
        temp = []
        for na in graph[vertex]:
            for na1 in na:
                temp.append(na1)
        return temp

    def minvalueneighbour(self,start):
        n2 = self.get_neighbour(start)
        n3=[]
        for index in n2:
            n3=n3+self.cost[index]

        i = 0
        while i < len(n3):
            key = i
            j = i + 1
            while j < len(n3):
                if n3[key] > n3[j]:
                    key = j
                j += 1
            n3[i], n3[key] = n3[key], n3[i]
            n2[i], n2[key] = n2[key], n2[i]
            i += 1

        return n2[0]

    def Greddy(self,start, goal, path=[]):
        path = path + [start]
        if (goal == start):
            return path
        minneighbour = self.minvalueneighbour(start)
        pathhh=self.Greddy(minneighbour , goal,path)
        return pathhh

g = {'Arad': [{'Zerind': [75]}, {'Timisoara': [118]}, {'Sibiu': [140]}],
             'Zerind': [{'Oradea': [71]}, {'Arad': [75]}],
             'Timisoara': [{'Lugoj': [111]}, {'Arad': [118]}],
             'Oradea': [{'Sibiu': [151]}, {'Zerind': [75]}],
             'Lugoj': [{'Mehadia': [70]}, {'Timisoara': [111]}],
             'Sibiu': [{'Fagaras': [99]}, {'Rimnicu Vilcea': [80]}, {'Arad': [140]}, {'Oradea': [151]}],
             'Mehadia': [{'Dobreta': [75]}, {'Lugoj': [70]}],
             'Dobreta': [{'Craiova': [120]}, {'Mehadia': [75]}],
             'Fagaras': [{'Bucharest': [211]}, {'Sibiu': [99]}],
             'Rimnicu Vilcea': [{'Pitesti': [97]}, {'Craiova': [146]}],
             'Craiova': [{'Rimnicu Vilcea': [146]}, {'Pitesti': [138]}],
             'Pitesti': [{'Bucharest': [101]}, {'Rimnicu Vilcea': [97]}],
             'Bucharest': [{'Urziceni': [85]}, {'Giurgiu': [90]}, {'Pitesti': [101]}, {'Fagaras': [211]}],
             'Giurgiu': [{'Bucharest': [90]}],
             'Urziceni': [{'Hirsova': [98]}, {'Bucharest': [85]}, {'Vaslui': [142]}],
             'Hirsova': [{'Urziceni': [98]}, {'Eforie': [86]}],
             'Eforie': [{'Hirsova': [86]}],
             'Vaslui': [{'Lasi': [92]}, {'Urziceni': [142]}],
             'Lasi': [{'Neamt': [87]}, {'Vaslui': [92]}],
             'Neamt': [{'Lasi': [87]}]
             }
graph = Graph(g)
print("Path From Arad to Bucharest")
print(graph.Greddy('Arad','Bucharest'))
