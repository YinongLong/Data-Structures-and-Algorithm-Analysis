# -*- coding: utf-8 -*-
"""
Created on 2017/4/4 下午9:18

@author: YinongLong

@file: algorithms.py

在这里会实现一些基本的算法算法设计技术

（1）贪婪类型算法

"""
from __future__ import print_function

import itertools


def huffman_code(text):
    """
    对文本内容实现Huffman编码
    
    :param text: str
        待编码的文本内容
        
    :return: dict
        字符对应的编码
    """

    # 统计每一个字符出现的次数
    counter = dict()
    for char in text:
        counter[char] = counter.setdefault(char, 0) + 1

    # 构建Huffman编码树，利用优先队列来进行存储树的根结点
    candidates = PriorityQueue()
    for key, val in counter.items():
        candidates.push(key, [val])

    root = None
    while not candidates.empty():
        sub_tree_1 = candidates.pop()
        if candidates.empty():
            root = sub_tree_1
        else:
            sub_tree_2 = candidates.pop()
            temp_priority = sub_tree_1[0] + sub_tree_2[0]
            temp_children = [sub_tree_1[1], sub_tree_2[1]]
            candidates.push(temp_priority, temp_children)

    sum_times = root[0]

    pass


class PriorityQueue(object):
    """
    为了锻炼自己的编码能力，手工实现一个优先队列，即最小堆
    """

    def __init__(self):
        self._priority_queue = list()
        self._counter = itertools.count()
        self._length = 0

    def push(self, priority, item):
        """
        将指定优先级的对象压入优先队列
        
        :param priority: int
            对象的优先级，数值越小，代表优先级越高，反之
            
        :param item: object
            压入优先队列的对象
            
        :return: None
            不返回任何值
        """
        content = (priority, self._counter.next(), item)
        self._priority_queue.insert(0, content)
        self._length = len(self._priority_queue)
        self._maintain_heap(0, self._length)

    def pop(self):
        """
        返回优先队列中优先级最小的对象，如果优先队列为空，在引起
        IndexError
        
        :return: tuple
            返回对象的优先级，以及对象
        """
        content = self._priority_queue.pop(0)
        self._length = len(self._priority_queue)
        return content[0], content[2]

    def empty(self):
        """
        返回优先队列是否为空
        
        :return: bool
            如果优先队列为空，则返回True，否则返回False
        """
        return False if self._length else True

    def _maintain_heap(self, index, length):
        """
        维持最小堆结构
        
        :param index: int
            开始维持堆结构的列表索引位
            
        :param length: int
            整个堆所占的列表的长度
            
        :return: None
            不返回任何值
        """
        def get_left_child(i):
            return 2 * i + 1

        child = get_left_child(index)
        temp_val = self._priority_queue[index]
        while child < length:
            if (child < (length - 1)) and \
            (self._priority_queue[child + 1] < self._priority_queue[child]):
                child += 1
            if self._priority_queue[child] < temp_val:
                self._priority_queue[index] = self._priority_queue[child]
            else:
                break
            index = child
            child = get_left_child(index)
        self._priority_queue[index] = temp_val

    def __str__(self):
        return str(self._priority_queue)


def main():
    queue = PriorityQueue()
    queue.push(1, 'a')
    queue.push(2, 'b')
    queue.push(7, 'c')
    queue.push(3, 'd')
    queue.push(6, 'e')
    queue.push(4, 'f')
    print(queue)
    print(queue.empty())
    while not queue.empty():
        print(queue.pop())
    pass

if __name__ == '__main__':
    main()