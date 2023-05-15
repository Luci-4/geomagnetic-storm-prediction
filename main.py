import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
import numpy as np


df = pd.read_csv("dataset_classification.csv")
X = df.drop(columns=['target', "latitude", "speed"]).values
y = df['target'].values



colors_map = {e: i+1 for i, e in enumerate(list(set(list(y))))}

# plt.scatter(preprocessing.normalize(X[:, 1].reshape(1, -1), norm="max"), preprocessing.normalize(X[:, 0].reshape(1, -1), norm="max"), c=[colors_map[e] for e in list(y)])
plt.scatter(X[:, 1], X[:, 0], c=[colors_map[e] for e in list(y)])
plt.show()
exit()




df = pd.read_csv("dataset_regression.csv")
X = df.drop(columns=['target']).values
y = df['target'].values
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.scatter(preprocessing.normalize(X[:, 0].reshape(1, -1), norm="max"), preprocessing.normalize(X[:, 1].reshape(1, -1), norm="max"), y)
plt.show()

# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')

# plt.show()
