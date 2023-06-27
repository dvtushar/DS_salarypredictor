# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 16:15:13 2023

@author: 91991
"""

import glassdoor_scrapper as gs 
import pandas as pd 

path = "C:/Users/91991/Desktop/ds_salary/chromedriver"

df = gs.get_jobs('data scientist',1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)