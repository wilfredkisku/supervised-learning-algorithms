import pandas  as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#set the parameters for the plt
plt.rcParams['figure.figsize'] = [8,5]
plt.rcParams['font.size'] =14
plt.rcParams['font.weight']= 'bold'
plt.style.use('seaborn-whitegrid')

path = 'data/'
df = pd.read_csv(path+'insurance.csv')
print('\nNumber of rows and columns in the data set: ',df.shape)
print('')

print(df.head())

print(df.region.unique())
