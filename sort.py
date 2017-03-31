# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 08:56:42 2017

@author: YinongLong

使用Python实现排序相关的算法
"""
from __future__ import print_function

import random


def shell_sort(array, steps=None):
    """
    实现希尔排序
    
    :param array: list
        待排序对象的列表
        
    :param steps: list
        希尔排序使用的步长列表，第一个元素必须是1，后面一次增长
        
    :return: None
        对对象序列进行原址排序
    """
    len_array = len(array)
    if steps is None:
        steps = []
        temp_val = len_array / 2
        while temp_val:
            steps.insert(0, temp_val)
            temp_val /= 2
    for step in steps:
        for i in range(step, len_array):
            temp_val = array[i]
            for j in range(i, 0, -step):
                if (j - step) >= 0 and (array[j - step] > temp_val):
                    array[j] = array[j - step]
                else:
                    array[j] = temp_val
                    break
            else:
                array[0] = temp_val


def insert_sort(array):
    """
    实现插入排序
    
    :param array: list
        待排序对象的列表
        
    :return: None
        对对象列表进行原址排序
    """
    len_array = len(array)
    for i in range(1, len_array):
        temp_value = array[i]
        for j in range(i, 0, -1):
            if array[j - 1] > temp_value:
                array[j] = array[j - 1]
            else:
                array[j] = temp_value
                break
        else:
            array[0] = temp_value


def quick_sort(array):
    _quick_sort(array, 0, len(array)-1)


def _quick_sort(array, start, end):
    """
    实现快速排序（递归形式）
    
    :param array: list
        存储待排序对象（实现大小的比较）的列表
        
    :param start: int
        排序的起始索引
        
    :param end: int
        排序的终止索引
        
    :return: None
        对列表进行原址排序
    """
    index = _partition(array, start, end)
    if index > start:
        _quick_sort(array, start, index - 1)
    if index < end:
        _quick_sort(array, index + 1, end)


def _partition(array, start, end):
    """
    对列表进行划分的步骤，将一个随机选择的对象放到正确的位置上
    
    :param array: list
        待排序的对象列表
        
    :param start: int
        获取划分的列表起始索引
        
    :param end: int
        获取划分的列表终止索引
        
    :return: int
        返回列表中已经放置到正确位置的对象索引
    """
    mid = random.randint(start, end)
    array[end], array[mid] = array[mid], array[end]
    small = start - 1
    for index in range(start, end):
        if array[index] < array[end]:
            small += 1
            if small != index:
                array[small], array[index] = array[index], array[small]
    small += 1
    array[small], array[end] = array[end], array[small]
    return small

    
def main():
    size = 20
    array = [random.randint(0, 100) for _ in range(size)]
    sort_algorithms = [insert_sort, shell_sort, quick_sort]
    result = []
    for algorithm in sort_algorithms:
        copy_array = list(array)
        print(copy_array)
        algorithm(copy_array)
        print(copy_array, '\n')
        result.append(copy_array)
    for i in range(1, len(result)):
        if result[i] != result[i]:
            print('Sort Algorithms %s and %s have problems!' % (str(sort_algorithms[i-1]), str(sort_algorithms[i])))
    print('Sort Algorithms are all right!')

    
if __name__ == '__main__':
    main()
