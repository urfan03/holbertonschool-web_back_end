#!/usr/bin/env python3
'''
Write a type-annotated function sum_list
which takes a list input_list of floats as
argument and returns their sum as a float.
'''

from typing import List


def sum_mixed_list(mxd_lst: List[float, int]) -> float:
    """returns their sum as a float"""
    return sum(mxd_lst)
