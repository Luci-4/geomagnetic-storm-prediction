import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing

df = pd.read_csv("dataset_classification.csv")
X = df.drop(columns=['target']).values
target = df['target'].values

fig = plt.figure()

# 3D Plot
ax = fig.add_subplot(221, projection='3d')
x = preprocessing.normalize(X[:, 0].reshape(1, -1), norm="max")
y = preprocessing.normalize(X[:, 1].reshape(1, -1), norm="max")
z = preprocessing.normalize(X[:, 2].reshape(1, -1), norm="max")
x = X[:, 0]
y = X[:, 1]
z = X[:, 2]

colors_map = {e: i + 1 for i, e in enumerate(set(target))}

ax.scatter(
    x,
    y,
    z,
    c=[2 - colors_map[e] for e in target],
    marker='o'
)

ax.set_xlabel('latitude', fontsize=16)
ax.set_ylabel('longitude', fontsize=16)
ax.set_zlabel('half angle', fontsize=16)

# Cross-sections
ax = fig.add_subplot(222)
ax.scatter(x, y, c=[2 - colors_map[e] for e in target], marker='o')
ax.set_xlabel('latitude', fontsize=16)
ax.set_ylabel('longitude', fontsize=16)

ax = fig.add_subplot(223)
ax.scatter(x, z, c=[2 - colors_map[e] for e in target], marker='o')
ax.set_xlabel('latitude', fontsize=16)
ax.set_ylabel('half angle', fontsize=16)

ax = fig.add_subplot(224)
ax.scatter(y, z, c=[2 - colors_map[e] for e in target], marker='o')
ax.set_xlabel('longitude', fontsize=16)
ax.set_ylabel('half angle', fontsize=16)

plt.tight_layout()
plt.show()
