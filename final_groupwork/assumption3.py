#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import pandas as pd


with open("timestamp.txt","r") as f:
    data = f.read()
    ls = map(int,data.split("\n"))

df = pd.DataFrame(ls,columns=["timestamp"])
day = map(int,(df["timestamp"]-df['timestamp'].shift(-1,fill_value=0,axis=0))/3600*24)
df.insert(1,"timegap",list(day))
timegap = df.iloc[0:999,1]

max_ = max(timegap)
min_ = min(timegap)

plt.hist(timegap,bins=100)
plt.ylabel("Number of submissions in days")
plt.xlabel("Days")
plt.title("Recent 1000 commit frequency")
plt.ylim([0,100])
plt.xlim([min_,max_])
plt.show()
