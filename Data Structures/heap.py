# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:35:27 2019

@author: RAPHAEL
"""

from math import floor

class Heap:
    
    def __init__(self, lis = []):
        self.items = []
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def __getitem__(self, key):
        return self.items[key]
    
    def __iter__(self):
        return iter(self.items)
        
    
    def sortUp(self, itemIndex):
        '''
        Receives and item index in the list and then procedes to
        heapify it upwards
        '''
        
        parentIndex = floor((itemIndex + 1)/2)
        currentIndex = itemIndex + 1
        
        while self.items[currentIndex - 1] < self.items[parentIndex - 1]:
                self.items[parentIndex - 1], self.items[currentIndex - 1] = self.items[currentIndex - 1], self.items[parentIndex - 1]
                currentIndex = parentIndex
                parentIndex = floor(parentIndex/2)
                
    
    def add(self, *items):
        for i in items:
            self.size += 1
            self.items.append(i)
            self.sortUp(self.size-1)
        
    