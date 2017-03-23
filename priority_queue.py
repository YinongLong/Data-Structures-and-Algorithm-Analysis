# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 09:05:22 2017

@author: YinongLong

使用Python标准库中的heapq处理关于优先队列时存在的几个问题

首先Python标准库中heapq实现优先队列是根据array来进行实现的，并且实现的是
min-heap，而且array的索引从0开始，所以heap[i]的孩子节点为heap[2*i+1]和
heap[2*i+2]。

关于heapq的使用，初始化有两种方式：一种是使用heapq.heapify(list)方法，将
一个列表转换成一个min-heap，它的时间复杂都为O(len(list))；另一种方法是直接
使用一个空的列表[]，在后面关于heapq的操作中将这个列表传入即可，这个列表就是
这个min-heap的载体，而heap[0]就是列表的头元素即最小元素。

现在假设将min-heap用于任务的优先级安排或者在我们平常使用min-heap时，那么可
能会存在下面的几个问题：
（1）：当heap中存储着(priority, task)的项，那么当两个task的priority相同时，
如何在pop的过程中保持两个项的原有push顺序？
（2）：当task的priority改变时，如何将heap中的项(priority, task)放到正确的
位置？
（3）：当需要删除min-heap中的某些项的时候，如何来找到这些项以及删除它们？

对于第一个问题，可以将保存的项(priority, task)扩展为一个[priority, counter,
task]列表，其中的counter用来记录push的顺序。
对于后面两个问题，主要的问题是在查找和更新或者删除min-heap中的项，其中查找的
问题可以通过使用一个dictionary pointing来指向min-heap中的项，而更新的话，如
果直接更新就会破坏堆结构，所以可以通过添加标记的方式标记heap中待更新的项为删
除状态，对于更新的话，然后将更新priority的task再push进heap中。

将这个模块可以通过改写，使用到Dijkstra算法中。
"""
import itertools
import heapq

# 用来存储堆内容的列表
pq = []
# 用来记录堆中的项的字典
entry_finder = {}
# 表示删除的flag
REMOVED = "removed"
# 用来给压入堆的项分配序号
counter = itertools.count()

def remove_task(task):
    "标记一个已存在的task为删除状态，如果不存在，则引发KeyError"
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def add_task(task, priority=0):
    # 首先判断该task是否已经存在，如果存在，则表示更新值
    if task in entry_finder:
        remove_task(task)
    count = counter.next()
    entry = [priority, count, task]
    entry_finder[task] = entry
    heapq.heappush(pq, entry)
    
def pop_task():
    "移除和返回priority最小的task，如果min-heap为空，则引发KeyError"
    while pq:
        priority, count, task = heapq.heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError("pop from an empty priority queue!")

