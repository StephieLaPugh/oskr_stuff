# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 07:39:24 2022
@title: moving files based on substring in filename
@author: spugh
"""

import pandas as pd
import numpy as np
import os
import shutil

# SET DISPLAY OPTIONS
pd.set_option('display.max_columns', 8)     #show 8 columns
pd.set_option('display.max_colwidth', 20)   #30 characters per column 
pd.set_option('display.width', 200)         #total display width = 200 pixels
pd.options.display.float_format = '{:,.2f}'.format # commas and 2 decimals

source_path: "Path\to\files"
dest_path = "Path\to\copyto"
this = 'text to find'


for filename in os.listdir(source_path):
    if this in filename:
        if filename.endswith(('.xls','.xlsx')): # in my use case, I also wanted only Excel files 
            shutil.copy2(os.path.abspath(filename), os.path.join(pln + '\\' + filename))