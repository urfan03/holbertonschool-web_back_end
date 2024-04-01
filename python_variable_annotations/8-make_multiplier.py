#!/usr/bin/env python3
'''
Write a type-annotated function make_multiplier
that takes a float multiplier as argument and returns
a function that multiplies a float by multiplier.
'''

from typing import Callable


def make_multiplier(multiplier: float, x: float) -> Callable[[float], float]:
    """multiplies a float by multiplier"""
    return x * multiplier
