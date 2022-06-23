import numpy as np


x = np.array([['ciao',2],['prova', 4], ['test', 6]], dtype={'names': ['a', 'b'], 'formats': ['U32', 'i4']})
print(x)
print(x.dtype)