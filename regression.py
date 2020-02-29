import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

tr_k = pd.read_csv('training_known.csv').fillna(0)
tr_u = pd.read_csv('training_unknown.csv').fillna(1)
te_k = pd.read_csv('test_known.csv').fillna(0)
te_u = pd.read_csv('test_unknown.csv').fillna(1)

reg = LinearRegression().fit(tr_k, tr_u)
reconstructed = reg.predict(te_k)

rmse = np.sqrt(((reconstructed - te_u) ** 2).mean())

print(rmse)
