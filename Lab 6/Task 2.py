# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 15:53:40 2021

@author: Dell
"""
import pytictoc as tp

t = tp.TicToc()
vertexList = ['A','B','C','D','E']
edgeList = [('A','B'),('A','D'),('A','E'),('B','A'),('B','D'),('B','E'),('C','D'),('D','A'),('D','B'),('D','C'),('E','A'),('E','B')]
graphs = (vertexList,edgeList)

def bfs(graph, start):
    vertexList, edgeList = graph
    visitedVertex = []
    queue = [start]
    adjacencyList = [[] for vertex in vertexList]

    for edge in edgeList:
        adjacencyList[vertexList.index(edge[0])].append(edge[1])
    print('\nAdjacency List:',*adjacencyList,sep = "\n\t")
    
    print('\n')
    t.tic()
    while queue:
        current = queue.pop()
        for neighbor in adjacencyList[vertexList.index(current)]:
            if not neighbor in visitedVertex:
                queue.insert(0,neighbor)
        if current not in visitedVertex:
            visitedVertex.append(current)
    t.toc()
    return visitedVertex

print('Vertex List:',*vertexList,sep = "\n\t")
print('\nEdge List:',*edgeList,sep = "\n\t")
print('\nBFS: ',bfs(graphs,'A'))