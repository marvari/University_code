import pandas


df1 = pandas.read_csv("experiments.csv" , sep=';' )

df1['experiments'].plot(kind='bar')
