# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 08:32:36 2019

@author: penis
"""

import traceback
import sys

class linkedListNP:
      
    def __init__(self):
        self.next = [None]
        self.key = [None]
        self.prev = [None]
        
        self.size = 0
        
        
    def __getitem__(self, key):
        try:
            index, i = 0, 0
            while i < key:
                index = self.next[index]
                i += 1
            return self.key[index+1]
        
        except Exception:
            print("caralho")
            return None

        
    def __setitem__(self, key, value):
        try:
            index = 0
            
            for i in range(key):
                index = self.next[index]
            
            self.key[index+1] = value
        except TypeError as ke:
            print(ke.args)
            traceback.print_exc(file=sys.stdout)
        except IndexError:
            print("index error")
        except KeyError as ke:
            print("Key error")
            
    def __len__(self):
        return self.size
            
            
    def add(self, *items):
        
        for i in items:
            self.size += 1
            self.key.append(i)
            self.prev.append(self.size - 1)
            
            self.next[self.size - 1] = self.size
            self.next.append(None)
            
    def remove(self, key):
        try:
            index = 0
            for i in range(key):
                index = self.next[index]
                
            self.prev[self.next[index + 1]] = self.prev[index + 1]
            self.next[self.prev[index + 1]] = self.next[index + 1]
            
            self.key[index + 1] = None
            self.size -= 1
            
            return True
        except Exception as ke:
            print(ke.args)
            traceback.print_exc(file=sys.stdout)
            
    def list(self):
        index = 1
        for i in range(self.size):
            print(self.key[index])
            if index is not None:
                index = self.next[index]