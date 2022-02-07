#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import os
import csv
import collections
from collections import Counter

# - Variables
candidates = []
votes_per = []

# - Read in csv and then DF
csv_path = r"C:\Users\rzh00\Documents\gt-virt-atl-data-pt-09-2021-u-c-master\gt-virt-atl-data-pt-09-2021-u-c-master\02-Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv"
df = pd.read_csv(csv_path)


# In[23]:


# - Open csv
with open(csv_path, newline = '') as csvfile:
    
    csv_read = csv.reader(csvfile, delimiter = ',')
    
    # - Header
    csv_header = next(csvfile)
    
    #print(csv_header)
    
    for row in csv_read:
        candidates.append(row[2])
    
    sorted_list = sorted(candidates)
    
    arrange_list = sorted_list
    
    count_candidate = Counter (arrange_list)
    votes_per.append(count_candidate.most_common())
    
    for item in votes_per:
        first = format((item[0][1])*100/(sum(count_candidate.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_candidate.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_candidate.values())),'.3f')
        fourth = format((item[3][1])*100/(sum(count_candidate.values())),'.3f')
        
print('Election Results')
print('-' * 20)
print(f'Total Votes: {sum(count_candidate.values())}')
print('-' * 20)
print(f'{votes_per[0][0][0]}: {first}% ({votes_per[0][0][1]})')
print(f'{votes_per[0][1][0]}: {second}% ({votes_per[0][1][1]})')
print(f'{votes_per[0][2][0]}: {third}% ({votes_per[0][2][1]})')
print(f'{votes_per[0][3][0]}: {fourth}% ({votes_per[0][3][1]})')
print('-' * 20)
print(f'Winner: {votes_per[0][0][0]}')
print('-' * 20)


# In[ ]:




