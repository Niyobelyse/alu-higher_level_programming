#!/usr/bin/python3
'''Creating a private instance attribute within class square'''


class Square():
    '''Class definition'''
    def __init__(self, size):
        '''function body'''
        self.__size = size
