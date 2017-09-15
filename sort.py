# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 08:56:42 2017

@author: YinongLong

使用Python实现排序相关的算法
"""
from __future__ import print_function

import random
import time


def merge_sort(array):
    """
    对可比较的对象列表进行归并排序

    :param array: list
        存储待排序对象的列表

    :return: None
        无返回值，在原址进行排序
    """
    len_array = len(array)
    temp_array = list(array)
    _ms_sort(array, temp_array, 0, len_array - 1)


def _ms_sort(array, temp_array, start, end):
    """
    归并排序的递归部分

    :param array: list
        待排序的对象列表

    :param temp_array: list
        进行有序子列表的合并列表

    :param start: int
        递归排序列表的起始索引

    :param end: int
        递归排序列表的终止索引

    :return: None
        原址排序，不返回值
    """
    if start < end:
        center = (start + end) / 2
        _ms_sort(array, temp_array, start, center)
        _ms_sort(array, temp_array, center + 1, end)
        _merge_sub_array(array, temp_array, start, center + 1, end)


def _merge_sub_array(array, temp_array, left_start, right_start, right_end):
    """
    对两个有序的子列表进行合并

    :param array: list
        原始待排序列表

    :param temp_array: list
        进行合并存储的临时列表

    :param left_start: int
        待合并子列表的前一个的起始索引

    :param right_start: int
        待合并子列表的后一个的起始索引

    :param right_end: int
        待合并子列表的后一个的终止索引

    :return: None
        不返回值
    """
    left_end = right_start - 1
    temp_index = left_start
    left_start_copy = left_start
    while (left_start <= left_end) and (right_start <= right_end):
        if array[left_start] <= array[right_start]:
            temp_array[temp_index] = array[left_start]
            left_start += 1
        else:
            temp_array[temp_index] = array[right_start]
            right_start += 1
        temp_index += 1
    while left_start <= left_end:
        temp_array[temp_index] = array[left_start]
        left_start += 1
        temp_index += 1
    while right_start <= right_end:
        temp_array[temp_index] = array[right_start]
        right_start += 1
        temp_index += 1
    # 将临时列表中的合并结果复制回原排序列表
    while right_end >= left_start_copy:
        array[right_end] = temp_array[right_end]
        right_end -= 1


def _maintain_heap(array, index, len_array):
    """
    在堆排序中维持最大堆结构

    :param array: list
        存储对象的堆（使用列表表示）

    :param index: int
        需要维护的子堆索引

    :param len_array: int
        存储堆结构的列表的大小

    :return: None
        不返回值，只是在原址对堆进行维护
    """

    def get_left_child(i):
        return i * 2 + 1

    child = get_left_child(index)
    temp_value = array[index]
    while child < len_array:
        # 判断是否存在右孩子，以及右孩子是否大于左孩子存储的值
        if (child < (len_array - 1)) and (array[child + 1] > array[child]):
            child += 1
        if temp_value < array[child]:
            array[index] = array[child]
            index = child
            child = get_left_child(index)
        else:
            break
    array[index] = temp_value


def heap_sort(array):
    """
    实现堆排序

    :param array: list
        待排序的对象列表

    :return: None
        对待排序的列表进行原址排序，不返回任何值
    """
    len_array = len(array)
    # 首先对整个列表构造一个最大堆
    index = len_array / 2
    while index >= 0:
        _maintain_heap(array, index, len_array)
        index -= 1
    # 开始从堆顶删除元素（即与堆尾元素交换，最后使得列表按照递增排序）
    for i in range(1, len_array):
        array[0], array[-i] = array[-i], array[0]
        _maintain_heap(array, 0, len_array - i)


def shell_sort(array, steps=None):
    """
    实现希尔排序

    :param array: list
        待排序对象的列表

    :param steps: list
        希尔排序使用的步长列表，第一个元素必须是1，后面依次增长

    :return: None
        对对象序列进行原址排序
    """
    len_array = len(array)
    if steps is None:
        steps = []
        temp_val = len_array / 2
        while temp_val:
            steps.append(temp_val)
            temp_val /= 2
    for step in steps:
        for i in range(step, len_array):
            temp_val = array[i]
            for j in range(i, -1, -step):
                if (j - step) >= 0 and (array[j - step] > temp_val):
                    array[j] = array[j - step]
                else:
                    array[j] = temp_val
                    break


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
        else:  # 注意这里使用了Python语言的特殊语法
            array[0] = temp_value


def quick_sort(array):
    """
    快速排序的递归入口

    :param array: List
        待排序的数值列表
    """
    _quick_sort(array, 0, len(array) - 1)


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
    # 这里之所以进行+1以后进行交换，是因为避免前面的-1可能出现的情况，这个时候将mid放在了正确的位置
    small += 1
    array[small], array[end] = array[end], array[small]
    return small


def run_cost_time(algorithm, array):
    """
    记录排序算法运行的时间
    :param algorithm: object
        用来进行排序的算法

    :param array: list
        待排序的列表

    :return: None
        打印输出运行排序算法所需要的时间
    """
    start_time = time.time()
    algorithm(array)
    end_time = time.time()
    cost_time = end_time - start_time
    print('Running algorithm %s spends: %.2f' % (str(algorithm), cost_time))


def main():
    """
    对于随机产生的数列，测试所有的排序算法

    :return: None
    """
    size = 3000
    array = [random.randint(0, 100) for _ in range(size)]
    sort_algorithms = [insert_sort, shell_sort, quick_sort, heap_sort, merge_sort]
    result = []
    for algorithm in sort_algorithms:
        copy_array = list(array)
        # print(copy_array)
        run_cost_time(algorithm, copy_array)
        # print(copy_array, '\n')
        result.append(copy_array)
    for i in range(1, len(result)):
        if result[i] != result[i-1]:
            print('Sort Algorithms %s and %s have problems!' % (str(sort_algorithms[i - 1]), str(sort_algorithms[i])))
    print('Sort Algorithms are all right!')


if __name__ == '__main__':
    main()
