import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pandas as pd

df = pd.read_csv("dataset_classification.csv")

X = preprocessing.normalize(df.drop(columns=['target', 'latitude', 'speed']).values, norm="max")
# X = df.drop(columns=['target', 'latitude']).values
y = df['target'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = svm.SVC()
model.fit(X_train, y_train)

# Obtain the minimum and maximum values for each feature in your dataset
x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1

# Generate a grid of points that spans the entire feature space
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))

# Predict the class labels for each point on the grid
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])

# Reshape the predictions to the same shape as the grid
Z = Z.reshape(xx.shape)

# Plot the contour filled with different colors representing different classes
plt.contourf(xx, yy, Z, alpha=0.8)

# Plot the training points
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, edgecolors='k')

# Add labels and title to the plot
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Decision Boundaries')

# Show the plot
plt.show()
