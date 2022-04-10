import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')

X = np.array(data[['x1', 'x2']])
y = np.array(data['y'])

print(X)
print(y)
