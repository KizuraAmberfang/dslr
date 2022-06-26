import numpy as np
import pandas as pd
from utils.ft_pandas import MyDataset
from utils.read_csv import read_csv

prova = MyDataset(read_csv('data/dataset_train.csv'))
prova.mean()
print('\n')

prova2 = pd.read_csv('data/dataset_train.csv')
prova3 = prova2.mean()
print(prova3)
print('\n')
prova.describe()
