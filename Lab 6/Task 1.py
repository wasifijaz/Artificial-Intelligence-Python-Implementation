# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 13:46:34 2021

@author: Dell
"""
import pytictoc as tp

t = tp.TicToc()
vertexList = ['A','B','C','D','E']
edgeList = [('A','B'),('A','D'),('A','E'),('B','A'),('B','D'),('B','E'),('C','D'),('D','A'),('D','B'),('D','C'),('E','A'),('E','B')]
graphs = (vertexList,edgeList)

def dfs(graph, start):
    vertexList, edgeList = graph
    visitedVertex = []
    stack = [start]
    adjacencyList = [[] for vertex in vertexList]

    for edge in edgeList:
        adjacencyList[vertexList.index(edge[0])].append(edge[1])
    print('\nAdjacency List:',*adjacencyList,sep = "\n\t")
    
    print('\n')
    t.tic()
    while stack:
        current = stack.pop()
        for neighbor in adjacencyList[vertexList.index(current)]:
            if not neighbor in visitedVertex:
                stack.append(neighbor)
        if current not in visitedVertex:
            visitedVertex.append(current)
    t.toc() 
    return visitedVertex  

print('Vertex List:',*vertexList,sep = "\n\t")
print('\nEdge List:',*edgeList,sep = "\n\t")
print('\nDFS: ',dfs(graphs,'A'))