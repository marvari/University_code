#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas
import matplotlib
import matplotlib.pyplot as plt
from scipy import stats


df1 = pandas.read_csv("experiments.csv")
df1['experiments'].plot(kind='bar')


print(df1.experiments.describe())


distribution = pandas.DataFrame(data={
    'df1': df1['experiments'],
})

distribution.plot.kde()

d1 = distribution['df1']

print(stats.kstest('norm', 'norm', N = 500))
print(stats.kstest(d1, 'norm', (d1.mean(), d1.std()), N = len(d1)))
plt.show()
