# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 08:25:14 2017

@author: YinongLong
"""
from __future__ import print_function

from itertools import count
from collections import defaultdict

import heapq


class Graph(object):
    """
    定义图的数据结构（使用邻接表存储），并且实现对图的各种操作（拓扑排序、几种最短路径的实现）
    """

    def __init__(self, edge_pairs):
        """
        初始化图，将图初始化为带权图，如果初始化时没有给出权值，则默认为1
        
        Parameters
        ----------
        edge_pairs: list
            存储图的边连接的列表，其中用二元组表示一条边，且第一个元素
            表示起点，第二个元素表示终点
        """
        # 存储顶点的名称
        self.names = []
        # 给定点分配编号
        self._counter = count()
        # 存储顶点名称和编号的对应关系
        self.name_coder = {}
        # 存储图的邻接表
        self._adjacencyList = []
        for edge in edge_pairs:
            if len(edge) == 2:
                node1, node2 = edge
                weight = 1
            else:
                node1, node2, weight = edge
                
            if node1 not in self.name_coder:
                self.name_coder[node1] = self._counter.next()
                self.names.append(node1)
                self._adjacencyList.append([])
            if node2 not in self.name_coder:
                self.name_coder[node2] = self._counter.next()
                self.names.append(node2)
                self._adjacencyList.append([])
                
            num1 = self.name_coder[node1]
            num2 = self.name_coder[node2]
            self._adjacencyList[num1].append((num2, weight))
        self.nums_vertex = len(self.names)
            
    def topology_sort(self):
        """
        实现图（只针对有向图）的拓扑排序（可以用来判断有向图是否存在圈）
        """
        # 首先计算每一个顶点的入度，这里会对每一条边进行遍历，因此时间复杂度为O(V+E)
        in_degree = [0] * self.nums_vertex
        for nodes in self._adjacencyList:
            for node, _ in nodes:
                in_degree[node] += 1
        # 将入度为0的定点放入队列，这里使用队列存储入度为0的顶点，相比于每次扫描一遍
        # 记录入度的数组的时间复杂度O(V^2)提高到了O(V+E)
        candidates = []
        for index in range(self.nums_vertex):
            if in_degree[index] == 0:
                candidates.append(index)
            
        result = list()
        while candidates:
            index = candidates.pop(0)
            result.append(self.names[index])
            for node, _ in self._adjacencyList[index]:
                in_degree[node] -= 1
                if in_degree[node] == 0:
                    candidates.append(node)
        if len(result) != self.nums_vertex:
            raise TypeError("This graph has a loop !!! ")
        return result
    
    def unweighted_short_path(self, vertex_name):
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
        records = [[None, None] for _ in range(self.nums_vertex)]  # 涉及对象的深浅拷贝问题
        vertex_num = self.name_coder[vertex_name]
        # 源点到自身的无权最短路径为0
       
        records[vertex_num][0] = 0
        
        candidates = list()
        candidates.append(vertex_num)
        
        while candidates:
            temp_vertex = candidates.pop(0)
            for node, _ in self._adjacencyList[temp_vertex]:
                if records[node][0] is None:
                    records[node][0] = records[temp_vertex][0] + 1
                    records[node][1] = temp_vertex
                    candidates.append(node)
        self._print_short_path(records, start_point=vertex_num)

    def _print_short_path(self, records, start_point, _len_position=0, _par_position=1):
        """
        打印求出的最短路径
        
        Parameters
        ----------
        records: list
            记录图的每个顶点的状态
            
        start_point: int
            单源点最短路径的起始顶点的标号
            
        _len_position: int
            指明路径长度存放的位置
            
        _par_position: int
            指明存放路径上一个顶点的标号的位置
        """
        # 以递归的形式打印路径
        def print_path(nodes, no_index):
            if nodes[no_index][_par_position] is not None:
                temp_path = print_path(nodes, nodes[no_index][_par_position])
                temp_path += " -> "
                temp_path += self.names[no_index]
                return temp_path
            return self.names[no_index]
        
        for index in range(self.nums_vertex):
            path = print_path(records, index)
            print("The shortest path length between %s and %s is: %d" % (self.names[start_point],
                                                                         self.names[index],
                                                                         records[index][_len_position]))
            print(path)
            
    def negative_weighted_short_path(self, vertex_name):
        """
        计算制定源点到图中所有其它定点的加权最短路径（有负值权，但无负值圈）
        """
        # 记录顶点是否在队列中，以及当前源点到该顶点的路径长和上次更新路径的顶点编号
        records = [[0, None, None] for _ in range(self.nums_vertex)]
        num_vertex = self.name_coder[vertex_name]
        # 记录顶点进入队列的次数，有顶点进入队列的次数达到 N+1 时（N 表示图顶点数），说明存在负值圈
        counter_map = defaultdict(int)
        # 将源点放入队列，以及更新相关的信息
        candidates = list()
        candidates.append(num_vertex)
        counter_map[num_vertex] += 1
        records[num_vertex][0] = 1
        records[num_vertex][1] = 0
        
        while candidates:
            vertex = candidates.pop(0)
            records[vertex][0] = 0
            for node, weight in self._adjacencyList[vertex]:
                if (records[node][1] is None) or (records[vertex][1] + weight < records[node][1]):
                    records[node][1] = records[vertex][1] + weight
                    records[node][2] = vertex
                    if records[node][0] == 0:
                        candidates.append(node)
                        records[node][0] = 1
                        counter_map[node] += 1
                        # 说明已经出现了负值圈，终止循环
                        if counter_map[node] > self.nums_vertex:
                            break
        self._print_short_path(records, num_vertex, _len_position=1, _par_position=2)

    def positive_weighted_short_path(self, vertex_name):
        """
        计算指定源顶点到图中所有其它顶点的加权最短路径（无负权值）（Dijkstra的优先队列实现）
        
        Parameters
        ----------
        vertex_name: str
            指定计算的源顶点
        """
        # 记录是否已经找到最短路径，以及源点当前到该顶点的距离和上次更新该顶点的顶点号
        records = [[0, None, None] for _ in range(self.nums_vertex)]
        num_vertex = self.name_coder[vertex_name]
        
        candidates = PriorityQueue()
        candidates.push(priority=0, content=num_vertex)
        records[num_vertex][1] = 0
    
        while not candidates.empty():
            # 弹出待候选顶点中拥有最短距离的路径长和顶点号
            priority, vertex = candidates.pop()
            records[vertex][0] = 1
            # 更新弹出顶点邻接的顶点
            for node, weight in self._adjacencyList[vertex]:
                # 只更新未找到最短路径的顶点
                if records[node][0] == 0:
                    if records[node][1] is None:
                        records[node][1] = priority + weight
                        records[node][2] = vertex
                        candidates.push(priority=records[node][1], content=node)
                    elif (priority + weight) < records[node][1]:
                        records[node][1] = priority + weight
                        records[node][2] = vertex
                        candidates.push(priority=records[node][1], content=node)
        self._print_short_path(records, num_vertex, _len_position=1, _par_position=2)
        
    def min_span_tree_prim(self, start_point):
        """
        生成无向图的最小生成树（Prim算法）
        
        Parameters
        ----------
        start_point: str
            最开始加入到生成树中顶点名称
        """
        # 记录顶点的状态，包括是否已经是生成树中的节点，到树中顶点集的距离，以及最后更新该节点距离的节点号
        records = [[0, None, None] for _ in range(self.nums_vertex)]
        num_vertex = self.name_coder[start_point]
        records[num_vertex][1] = 0
        candidates = PriorityQueue()
        candidates.push(priority=0, content=num_vertex)

        # 代表最小生成树的总权重
        sum_weight = 0
        
        while not candidates.empty():
            priority, vertex = candidates.pop()
            sum_weight += priority
            records[vertex][0] = 1
            for node, weight in self._adjacencyList[vertex]:
                # 对还没有添加到生成树中的节点进行测试
                if records[node][0] == 0:
                    if (records[node][1] is None) or (records[node][1] > weight):
                        records[node][1] = weight
                        records[node][2] = vertex
                        candidates.push(weight, node)
        self._print_short_path(records, num_vertex, _len_position=1, _par_position=2)
        return sum_weight

    def min_span_tree_kruskal(self):
        """
        生成无向图的最小生成树（Kruskal算法）
        
        :returns: 返回最小生成树的权重和连接关系
        """
        # 存储无向图的边
        candidates = PriorityQueue()

        # 将无向图的边读取到优先队列中
        for index in range(self.nums_vertex):
            for node, weight in self._adjacencyList[index]:
                candidates.push(weight, (index, node))
        # 将每个顶点划分到不同的集合中，划分元组标记
        separate_set = dict()
        for vertex in range(self.nums_vertex):
            separate_set[vertex] = [vertex]
        # 记录已经添加到生成树中的边的个数和总权重
        edges_accepted = 0
        sum_weight = 0
        result = []
        while edges_accepted < (self.nums_vertex - 1):
            weight, edge = candidates.pop()
            v1, v2 = edge
            v1_set = separate_set[v1]
            v2_set = separate_set[v2]
            if v1_set is not v2_set:
                edges_accepted += 1
                result.append((self.names[v1], self.names[v2]))
                # 进行集合的合并
                temp_value = list()
                for item in v1_set:
                    separate_set[item] = temp_value
                    temp_value.append(item)
                for item in v2_set:
                    separate_set[item] = temp_value
                    temp_value.append(item)
                sum_weight += weight
        return sum_weight, result

    def __str__(self):
        """
        打印图
        """
        print(" " * 3, "Vertex", " " * 6, "Adjacency Nodes")
        for index in range(self.nums_vertex):
            if len(self._adjacencyList[index]) == 0:
                print(" " * 3, self.names[index])
            else:
                print(" " * 3,  self.names[index], " ", "-" * 4, " ", end="")
                for node, _ in self._adjacencyList[index]:
                    print("  ", self.names[node], end="")
                print()
        return ""
    
    
class PriorityQueue(object):
    """
    对Python标准库heapq优先队列的补充实现，来方便在优先队列中的查找、更新，以及
    删除操作，而且在对象具有相同优先级时，按照压入的顺序返回。这里利用了Python的
    引用机制，即使用一个字典保存压入堆的对象的引用，来方便后续实现对对象的删除以及
    更新操作。
    """
    
    def __init__(self):
        self._container = []
        self._entry_mapper = {}
        self._REMOVED = '<REMOVED>'
        self._counter = count()
        
    def push(self, priority, content):
        """
        将对象压入min-heap堆
        
        Parameters
        ----------
        priority: int
            在优先队列中进行排序的优先级
            
        content: object
            被压入对象的内容，必须是可以hash的，否则引发TypeError
        """
        if content in self._entry_mapper:
            self.remove(content)
        cnt = self._counter.next()
        entry = [priority, cnt, content]
        heapq.heappush(self._container, entry)
        # 将压入堆的项纪录在字典中
        self._entry_mapper[content] = entry
    
    def pop(self):
        """
        弹出优先级最小的堆顶元素（priority, content），如果队列已经为空，则引发KeyError
        """
        while self._container:
            priority, cnt, content = heapq.heappop(self._container)
            if content is not self._REMOVED:
                del self._entry_mapper[content]
                return priority, content
        raise KeyError("Pop from an empty priority queue !")
    
    def remove(self, content):
        """
        删除优先队列中的指定元素（用标记的方式）
        """
        entry = self._entry_mapper.pop(content)
        entry[-1] = self._REMOVED
        
    def empty(self):
        """
        返回队列是否为空，如果为空则返回True，否则为False
        """
        if len(self._entry_mapper) > 0:
            return False
        else:
            return True
    
    
def main():
    edges = [('v1', 'v2', 2), ('v1', 'v4', 1), ('v2', 'v1', 2), ('v4', 'v1', 1),
             ('v2', 'v4', 3), ('v2', 'v5', 10), ('v4', 'v2', 3), ('v5', 'v2', 10),
             ('v3', 'v1', 4), ('v3', 'v6', 5), ('v1', 'v3', 4), ('v6', 'v3', 5),
             ('v4', 'v3', 2), ('v4', 'v5', 7), ('v4', 'v6', 8), ('v4', 'v7', 4),
             ('v3', 'v4', 2), ('v5', 'v4', 7), ('v6', 'v4', 8), ('v7', 'v4', 4),
             ('v5', 'v7', 6), ('v7', 'v5', 6),
             ('v7', 'v6', 1), ('v6', 'v7', 1)]
    
    arcs = [('v1', 'v2', 2), ('v1', 'v4', 1),
            ('v2', 'v4', 3), ('v2', 'v5', 10),
            ('v3', 'v1', 4), ('v3', 'v6', 5),
            ('v4', 'v3', 2), ('v4', 'v5', 2), ('v4', 'v6', 8), ('v4', 'v7', 4),
            ('v5', 'v7', 6),
            ('v7', 'v6', 1)]
    gra = Graph(edges)
    print(gra.min_span_tree_kruskal())


if __name__ == '__main__':
    main()
