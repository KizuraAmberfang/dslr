import numpy as np
import pandas as pd
from utils.ft_pandas import MyDataset
from utils.read_csv import read_csv

prova = MyDataset(read_csv('data/dataset_train.csv'))
prova.unique()
print('\n')

prova2 = pd.read_csv('data/dataset_train.csv')
print(prova2.nunique())
print(prova2.describe(include='all'))
print('\n')
prova.describe()
