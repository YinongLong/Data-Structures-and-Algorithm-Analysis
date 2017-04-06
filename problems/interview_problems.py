# -*- coding:utf-8 -*-
"""

在这里主要实现一些面试中遇到的问题

"""
from __future__ import print_function

import operator
import itertools


class CandiesHeap(object):

    def __init__(self):
        """
        初始化堆对象
        """
        # 存放糖果对象的列表
        self.container = []
        # 存放糖果的个数
        self.length = 0
        # 记录放入堆中的顺序
        self.counter = itertools.count()

    def _maintain_heap(self, index, length):
        """
        从index位置开始维持堆结构
        
        :param index: int
            开始维持堆结构的位置
            
        :param length: int
            堆的大小
            
        :return: None
            不返回任何值
        """
        def get_left_child(i):
            return 2 * i + 1

        child = get_left_child(index)
        temp_value = self.container[index]
        while child < length:
            if (child < (length - 1)) and (self.container[child + 1] > self.container[child]):
                child += 1
            if self.container[child] > temp_value:
                self.container[index] = self.container[child]
                index = child
                child = get_left_child(index)
            else:
                break
        self.container[index] = temp_value

    def push(self, num_ingredient, number):
        item = (num_ingredient, self.counter.next(), number)
        self.container.append(item)
        self.length += 1
        self._maintain_heap(0, self.length)

    def pop(self):
        if self.length == 0:
            return False
        else:
            item = self.container.pop(0)
            self.length -= 1
            return item[0], item[2]

    def empty(self):
        return False if self.length > 0 else True


def _deal_with_candies(numbers, volume):
    # 将两类糖果按照类别分别放在两个堆中，且在各自的堆中按照魔幻因子的从大到小弹出
    candies_1_heap = CandiesHeap()
    candies_2_heap = CandiesHeap()
    for i in range(numbers):
        category, ingredient = raw_input().strip().split()
        category, ingredient = int(category), int(ingredient)
        if category == 1:
            candies_1_heap.push(ingredient, i + 1)
        else:
            candies_2_heap.push(ingredient, i + 1)
    candy_2_num = None
    candy_2_order = None
    candy_11_num = None
    candy_12_num = None
    candy_11_order = None
    candy_12_order = None
    sum_ingredient = 0
    container_1 = []
    container_2 = []
    while volume > 0:
        if not candies_2_heap.empty() and (candy_2_num is None):
            candy_2_num, candy_2_order = candies_2_heap.pop()
        if not candies_1_heap.empty() and (candy_11_num is None):
            candy_11_num, candy_11_order = candies_1_heap.pop()
            second_result = candies_1_heap.pop()
            if second_result is not False:
                candy_12_num, candy_12_order = second_result
            else:
                candy_12_num, candy_12_order = 0, None
        if (candy_11_num + candy_12_num) > candy_2_num:
            sum_ingredient += candy_11_num + candy_12_num
            container_1.append((candy_11_num, candy_11_order))
            if candy_12_order is not None:
                container_1.append((candy_12_num, candy_12_order))
            candy_11_num = None
            candy_12_num = None
            if candy_12_order is None:
                volume -= 1
            else:
                volume -= 2
        else:
            sum_ingredient += candy_2_num
            container_2.append((candy_2_num, candy_2_order))
            candy_2_num = None
            volume -= 2
        if volume == 1:
            break
    if volume == 1:
        if not candies_2_heap.empty() and (candy_2_num is None):
            candy_2_num, candy_2_order = candies_2_heap.pop()
        if candy_2_num is None:
            if not candies_1_heap.empty() and (candy_11_num is None):
                candy_11_num, candy_11_order = candies_1_heap.pop()
            if candy_11_num is not None:
                sum_ingredient += candy_11_num
                container_1.append((candy_11_num, candy_11_order))
        else:
            if not candies_1_heap.empty() and (candy_11_num is None):
                candy_11_num, candy_11_order = candies_1_heap.pop()
            if candy_11_num is None:
                if len(container_1) != 0 and container_1[-1][0] < candy_2_num:
                    sum_ingredient -= container_1[-1][0]
                    sum_ingredient += candy_2_num
                    container_1.pop(-1)
                    container_2.append((candy_2_num, candy_2_order))
            else:
                if len(container_1) == 0:
                    sum_ingredient += candy_11_num
                    container_1.append((candy_11_num, candy_11_order))
                else:
                    if (candy_11_num + container_1[-1][0]) < candy_2_num:
                        sum_ingredient -= container_1[-1][0]
                        sum_ingredient += candy_2_num
                        container_1.pop(-1)
                        container_2.append((candy_2_num, candy_2_order))
    order_heap = CandiesHeap()
    for _, item_number in container_1:
        order_heap.push(item_number, -1)
    for _, item_number in container_2:
        order_heap.push(item_number, -1)
    result = []
    while not order_heap.empty():
        number, _ = order_heap.pop()
        result.insert(0, number)
    print_result = ''
    for i in range(len(result)):
        if i < (len(result) - 1):
            print_result += str(result[i]) + ' '
        else:
            print_result += str(result[i])
    if sum_ingredient == 0:
        print_result = 'No'
    print(sum_ingredient)
    print(print_result)


def buy_candies():
    """
    实现一个关于京东2016实习生笔试的买糖果的问题
    
    构建一个用来模拟车厢大小的小顶堆，先将所有的魔幻因子比较大的体积
    为1的糖果放入堆中，尽量填满，如果不够，使用魔幻因子比较大的体积为
    2的糖果来补充
    """
    while True:
        numbers, volume = raw_input().strip().split()
        numbers, volume = int(numbers), int(volume)
        _deal_with_candies(numbers, volume)


def top_k_number(array, k=5):
    """
    实现查找列表的前K大数字，思路：构造max-heap即可
    
    :param array: list
        存储数字的列表
        
    :param k: int
        指定需要查找的最大的数字个数
        
    :return: list
        找出的K大数字
    """
    # 获取堆节点的左孩子
    def get_left_child(i):
        return 2 * i + 1

    # 维持堆结构
    def maintain_heap(arr, j, length):
        child = get_left_child(j)
        temp_value = arr[j]
        while child < length:
            if (child < (length - 1)) and (arr[child] < arr[child + 1]):
                child += 1
            if arr[child] > temp_value:
                arr[j] = arr[child]
                j = child
                child = get_left_child(j)
            else:
                break
        arr[j] = temp_value

    len_array = len(array)
    mid = len_array / 2
    for index in range(mid, -1, -1):
        maintain_heap(array, index, len_array)
    result = []
    end = len_array - 1
    while k > 0:
        result.append(array[0])
        array[0], array[end] = array[end], array[0]
        maintain_heap(array, 0, end)
        end -= 1
        k -= 1
    return result


def find_longest_sequence(str1, str2):
    """
    查找两个字符串的最长公共子序列（注意与最长公共子串的区别）
    
    :param str1: str
        其中的一个字符串参数
        
    :param str2: str
        其中的另外一个字符串参数
        
    :return: str
        返回的最长子序列结果
    """
    len_str1 = len(str1)
    len_str2 = len(str2)
    # 初始化存储中间状态的矩阵
    matrix = [[0 for _ in range(len_str1 + 1)] for _ in range(len_str2 + 1)]
    for i in range(len_str2):
        char_str2 = str2[i]
        for j in range(len_str1):
            char_str1 = str1[j]
            if char_str1 == char_str2:
                matrix[i+1][j+1] = matrix[i][j] + 1
            else:
                matrix[i+1][j+1] = max(matrix[i+1][j], matrix[i][j+1])
    row = len_str2
    col = len_str1
    result = ''
    while (row > 0) and (col > 0):
        temp_num = matrix[row][col]
        while (col > 1) and (matrix[row][col-1] == temp_num):
            col -= 1
        while (row > 1) and (matrix[row-1][col] == temp_num):
            row -= 1
        result = str1[col-1] + result
        row -= 1
        col -= 1
    return result


def find_longest_substring(str1, str2):
    """
    查找两个字符串的最长公共子串（注意与最长子序列的差别）
    
    :param str1: str
        其中一个字符串参数
        
    :param str2: str
        其中另外一个字符串参数
        
    :return: str
        两个字符串的最长公共子串
    """
    len_str1 = len(str1)
    len_str2 = len(str2)
    # 初始化存储中间状态的矩阵
    matrix = [[0 for _ in range(len_str1 + 1)] for _ in range(len_str2 + 1)]
    len_max = -1
    position = [-1, -1]
    for i in range(len_str2):
        char_str2 = str2[i]
        for j in range(len_str1):
            char_str1 = str1[j]
            if char_str1 == char_str2:
                matrix[i+1][j+1] = matrix[i][j] + 1
                if matrix[i+1][j+1] > len_max:
                    len_max = matrix[i+1][j+1]
                    position = [i, j]
    i, j = position
    longest_substring = ''
    while (i >= 0) and (j >= 0):
        longest_substring = str2[i] + longest_substring
        i -= 1
        j -= 1
    return longest_substring


def big_integer_add(num1, num2):
    """
    实现大整数的加法，在这里需要注意正负符号的问题。
    
    :param num1: str
        字符串表示的大整数
        
    :param num2: str
        字符串表示的大整数
        
    :return: str
        返回最后相加的结果
    """
    def raise_val_error():
        raise ValueError('The argument value is not correct!')

    # 进行参数的检查，并且返回参数的正负性，如果是正数，则返回True
    def check_parameter(parameter):
        para_positive = False if parameter.startswith('-') else True
        if para_positive and not parameter.isdigit():
            raise_val_error()
        if not para_positive and not parameter[1:].isdigit():
            raise_val_error()
        return para_positive

    num1_positive = check_parameter(num1)
    num2_positive = check_parameter(num2)
    # 设置两个大整数数位之间运算的操作符
    op = operator.sub if (num1_positive ^ num2_positive) else operator.add
    # 获取两个数位的长度
    num1_len = len(num1)
    if not num1_positive:
        num1_len -= 1
    num2_len = len(num2)
    if not num2_positive:
        num2_len -= 1

    # 开始进行计算
    index = -1
    temp_result = []
    while (abs(index) <= num1_len) and (abs(index) <= num2_len):
        value = op(int(num1[index]), int(num2[index]))
        temp_result.insert(0, value)
        index -= 1
    while abs(index) <= num1_len:
        value = int(num1[index])
        temp_result.insert(0, value)
        index -= 1
    while abs(index) <= num2_len:
        value = op(0, int(num2[index]))
        temp_result.insert(0, value)
        index -= 1
    # 计算结束，开始进行进位或借位操作
    need_update = False
    if op is operator.add:  # 进位操作
        for i in range(-1, -len(temp_result)-1, -1):
            value = temp_result[i]
            if need_update:
                value += 1
                need_update = False
            if value >= 10:
                value %= 10
                need_update = True
            temp_result[i] = value
        if need_update:
            temp_result.insert(0, 1)
        result = ''
        if not num1_positive and not num2_positive:
            result += '-'
        for item in temp_result:
            result += str(item)
    else:  # 借位操作
        # 标记最终结果的正负号
        num_sign = -1 if temp_result[0] < 0 else 1
        for i in range(-1, -len(temp_result)-1, -1):
            value = temp_result[i]
            if need_update:
                value += (-1 * num_sign)
                need_update = False
            if (num_sign * value) < 0:
                value += (10 * num_sign)
                need_update = True
            temp_result[i] = abs(value)
        while len(temp_result) > 0 and (temp_result[0] == 0):
            temp_result.pop(0)
        result = ''
        if num1_positive and len(temp_result) > 0:
            if num_sign == -1:
                result += '-'
        if num2_positive and len(temp_result) > 0:
            if num_sign == 1:
                result += '-'
        for item in temp_result:
            result += str(item)
        if len(result) == 0:
            result += '0'
    return result


def big_integer_add_1(var):
    """
    实现大整数加 1，在这个实现中是直接从字符串的
    角度进行操作，另外一个关于大整数加法的实现是从
    列表的角度进行实现
    
    :param var: str
        使用字符串表示的大整数
        
    :return: str 
        返回大整数加1的结果
    """
    if not isinstance(var, str):
        raise TypeError('The input variable type is wrong !')
    is_negative = False
    length_str = len(var)
    if var.startswith('-'):
        is_negative = True
        length_str -= 1
    index = 1 if is_negative else 0
    if not var[index:].isdigit():
        raise ValueError('The input value is wrong !')

    # 记录处理的数字的索引位
    index = -1
    # 记录处理结束的数字部分
    str_semi = ''

    if is_negative:
        while True:
            last_num = int(var[index])
            result = last_num - 1
            need_update = False
            if result < 0:
                result += 10
                need_update = True
            if not need_update:
                if (abs(index) == length_str) and (result == 0):
                    if length_str == 1:  # 处理 -1 的特殊情况
                        return '0'
                    return var[:index] + str_semi
                else:
                    return var[:index] + str(result) + str_semi
            else:
                str_semi = str(result) + str_semi
            index -= 1
    else:
        while True:
            if abs(index) > length_str:
                last_num = 0
            else:
                last_num = int(var[index])
            result = last_num + 1
            need_update = False
            if result >= 10:
                result %= 10
                need_update = True
            if need_update:
                str_semi = str(result) + str_semi
            else:
                return var[:index] + str(result) + str_semi
            index -= 1


def main():
    buy_candies()
    # print(find_longest_sequence('queue', 'sequence'))
    # print(top_k_number([1, 4, 2, 6, 8], 3))
    pass


if __name__ == '__main__':
    main()
