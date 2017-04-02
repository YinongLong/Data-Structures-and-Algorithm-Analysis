# -*- coding:utf-8 -*-
"""

在这里主要实现一些面试中遇到的问题

"""
from __future__ import print_function

import operator


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
    print(find_longest_sequence('queue', 'sequence'))
    pass


if __name__ == '__main__':
    main()
