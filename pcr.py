import pandas as pd
import numpy as np
# import seaborn as sb

# PCA
df = pd.read_csv('./clean_short.csv')
covariance_matrix = df.corr()
covariance_matrix.fillna(0, inplace=True)
(eig_values, eig_vectors) = np.linalg.eig(covariance_matrix)

principal_components = eig_vectors[:,1:10]

# Regression

