# -*- coding:utf-8 -*-
"""

在这里主要实现一些面试中遇到的问题

"""
from __future__ import print_function

import operator


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
    num1_len = len(num1)
    if not num1_positive:
        num1_len -= 1
    num2_len = len(num2)
    if not num2_positive:
        num2_len -= 1
    index = -1
    temp_result = []
    need_update = False
    while (abs(index) <= num1_len) and (abs(index) <= num2_len):
        value = op(int(num1[index]), int(num2[index]))
        if need_update and (op is operator.sub):
            value -= 1
            need_update = False
        elif need_update and (op is operator.add):
            value += 1
            need_update = False

        if (op is operator.sub) and value < 0:
            value += 10
            need_update = True
        elif (op is operator.add) and value > 9:
            value %= 10
            need_update = True
        temp_result.insert(0, value)
        index -= 1
    while abs(index) <= num1_len:
        value = int(num1[index])
        if need_update and (op is operator.sub):
            value -= 1
            need_update = False
        # elif need_update and (op is )


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
                    if length_str == 1: # 处理 -1 的特殊情况
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
    print(big_integer_add_1('-10'))
    pass


if __name__ == '__main__':
    main()
