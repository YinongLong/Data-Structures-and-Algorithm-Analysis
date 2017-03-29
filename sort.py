# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 08:56:42 2017

@author: YinongLong
"""
from __future__ import print_function

import random


class Sort(object):
    
    def __init__(self):
        pass
    
    def sort_array(self, array, sort='quick_sort', inplace=False):
        if inplace:
            self.array = array
        else:
            self.array = [item for item in array]
            
        if sort == 'quick_sort':
            start = 0; end = len(self.array) - 1
            self._quickSort(start, end)
        return self.array
    
    def _quickSort(self, start, end):
        index = self._partition(start, end)
        if index > start:
            self._quickSort(start, index - 1)
        if index < end:
            self._quickSort(index + 1, end)
    
    def _partition(self, start, end):
        """
        实现对序列的划分，即针对选择的一个数字将其放在正确的位置上
        
        Parameters
        ----------
        start: int
            序列的开始索引
            
        end: int
            序列的结束索引
        """
        mid = random.randint(start, end)
        self.array[end], self.array[mid] = self.array[mid], self.array[end]
        small = start - 1
        for index in range(start, end):
            if self.array[index] < self.array[end]:
                small += 1
                if small != index:
                    self.array[small], self.array[index] = self.array[index], self.array[small]
        small += 1
        self.array[small], self.array[end] = self.array[end], self.array[small]

        return small
    
def main():
    pass
    
if __name__ == '__main__':
    main()