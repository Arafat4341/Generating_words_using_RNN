# -*- coding: utf-8 -*-
"""
Created on Sat May  5 21:03:56 2018

@author: Arafat
"""

data = open('kafka.txt', 'r').read()

chars = list(set(data)) # making a list of the unique chars from the data!

data_size, vocab_size = len(data), len(chars)

char_to_ix = {ch:i for i, ch in enumerate(chars)}
ix_to_char = {i:ch for i, ch in enumerate(chars)}
              
print(ix_to_char)