#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
os.chdir("/Users/work-pc/Documents/GitHub/ThesisPaper1P2")
import pandas as pd 
import numpy as np 
data = pd.read_csv("NESdata.csv",delimiter=',')

df=pd.DataFrame(data)
df['Id2'].max()


print(df[df['2007 NAICS code'] >= 11])