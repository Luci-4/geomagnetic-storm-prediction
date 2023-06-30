import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing
import numpy as np

# df = pd.read_csv("dataset_classification.csv")
df = pd.read_csv("dataset_classification.csv")
X = df.drop(columns=['target']).values
target = df['target'].values

num_points = len(list(target))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = preprocessing.normalize(X[:, 0].reshape(1, -1), norm="max")
y = preprocessing.normalize(X[:, 1].reshape(1, -1), norm="max")
z = preprocessing.normalize(X[:, 2].reshape(1, -1), norm="max")
x = X[:, 0]
y = X[:, 1]
z = X[:, 2]

colors_map = {e: i+1 for i, e in enumerate(list(set(list(target))))}

ax.scatter(
    x,
    y,
    z,
    c=[2-colors_map[e] for e in list(target)],
    marker='o'
)

# origin = [0], [0], [0]
# print(origin)

# for i in range(num_points):
#     ax.plot(
#         [0, x[0, i]],
#         [0, y[0, i]],
#         [0, z[0, i]],
#         c='r',
#         alpha=0.3
#     )


ax.set_xlabel('latitude')
ax.set_ylabel('longitude')
ax.set_zlabel('half angle')
plt.show()

