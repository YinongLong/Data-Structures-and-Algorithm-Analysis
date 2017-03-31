# -*- coding:utf-8 -*-
"""
在这里主要实现一些面试中遇到的问题
"""
from __future__ import print_function


def addition_big_integer(var):
    """
    实现大整数加 1
    
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
    print(addition_big_integer('0'))
    pass


if __name__ == '__main__':
    main()
