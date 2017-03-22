# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 08:25:14 2017

@author: YinongLong
"""
from __future__ import print_function

from Queue import Queue

class Graph(object):
    """
    定义图的数据结构（使用邻接表存储），并且实现对图的各种操作（拓扑排序）
    """
    
    def __init__(self, edge_pairs):
        """
        初始化图
        
        Parameters
        ----------
        edge_pairs: list
            存储图的边连接的列表，其中用二元组表示一条边，且第一个元素
            表示起点，第二个元素表示终点
        """
        # 存储顶点的名称
        self.names = []
        # 给定点分配编号
        self._number = 0
        # 存储顶点名称和编号的对应关系
        self.name_coder = {}
        # 存储图的邻接表
        self._adjacencyList = []
        for edge in edge_pairs:
            node1, node2 = edge
            if node1 not in self.name_coder:
                self.name_coder[node1] = self._number
                self.names.append(node1)
                self._adjacencyList.append([])
                self._number += 1
            if node2 not in self.name_coder:
                self.name_coder[node2] = self._number
                self.names.append(node2)
                self._adjacencyList.append([])
                self._number += 1
            num1 = self.name_coder[node1]
            num2 = self.name_coder[node2]
            self._adjacencyList[num1].append(num2)
        self.nums_vertex = len(self.names)
            
    def topologySort(self):
        """
        实现图（只针对有向图）的拓扑排序（可以用来判断有向图是否存在圈）
        """
        # 首先计算每一个顶点的入度，这里会对每一条边进行遍历，因此时间复杂度为O(V+E)
        indegree = [0] * self.nums_vertex
        for nodes in self._adjacencyList:
            for node in nodes:
                indegree[node] += 1
        # 将入度为0的定点放入队列，这里使用队列存储入度为0的顶点，相比于每次扫描一遍
        # 记录入度的数组的时间复杂度O(V^2)提高到了O(V+E)
        candidates = Queue(self.nums_vertex)
        for index in xrange(self.nums_vertex):
            if indegree[index] == 0:
                candidates.put(index)
            
        topo_sort = []
        while not candidates.empty():
            index = candidates.get()
            topo_sort.append(self.names[index])
            for node in self._adjacencyList[index]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    candidates.put(node)
        if len(topo_sort) != self.nums_vertex:
            raise TypeError("This graph has a loop !!! ")
        return topo_sort
    
    def unweightedShortPath(self, vertex_name):
        """
        实现有向图的单原点无权最短路径，即从指定顶点出发到其他顶点最短
        需要经过的边数。实现的想法就是图的广度优先遍历（breadth-first search）
        
        Parameters
        ----------
        vertex_name: str
            用来指定计算无权最短路径的起点的顶点名称
        """
        # 将源点到所有顶点的无权最短路径存储在一个列表的列表中
        """
        这里的这个关于records的初始化超级坑！！！！！！
        开始是使用:
            records = [[None, None]] * self.nums_vertex
        来进行初始化的，但是这样初始化的方式存在大问题！！！这样的初始化使得records里面
        的每一个列表都对应的同一个引用，所有每一次对其中一个元素的赋值都会影响到其它所
        有的项！！
        """
        records = [[None, None] for _ in xrange(self.nums_vertex)]
        vertex_num = self.name_coder[vertex_name]
        # 源点到自身的无权最短路径为0
       
        records[vertex_num][0] = 0
        
        candidates = Queue(self.nums_vertex)
        candidates.put(vertex_num)
        
        while not candidates.empty():
            temp_vertex = candidates.get()
            for node in self._adjacencyList[temp_vertex]:
                if records[node][0] == None:
                    records[node][0] = records[temp_vertex][0] + 1
                    records[node][1] = temp_vertex
                    candidates.put(node)
        # 返回路径
        def getPath(nodes, index):
            path = ""
            while nodes[index][1] != None:
                if path != "":
                    path = '->' + path
                path = self.names[nodes[index][1]] + path
                index = nodes[index][1]
            return path
        
        for index in xrange(self.nums_vertex):
            path = getPath(records, index)
            path += "->" + self.names[index]
            print("The dist between Original vertex and %s is: %d" % (self.names[index], records[index][0]))
            print(path)
            
    def __str__(self):
        """
        打印图
        """
        print(" " * 3, "Vertex", " " * 6, "Adjacency Nodes")
        for index in xrange(len(self._adjacencyList)):
            if len(self._adjacencyList[index]) == 0:
                print(" " * 3, self.names[index])
            else:
                print(" " * 3,  self.names[index], " ", "-" * 4, " ", end="")
                for node in self._adjacencyList[index]:
                    print("  ", self.names[node], end="")
                print()
        return ""