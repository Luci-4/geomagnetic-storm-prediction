import numpy as np

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd

# Generate random data for two classes
np.random.seed(0)
n_samples = 1000
X = np.random.randn(n_samples, 2)
y = np.concatenate((np.zeros(n_samples), np.ones(n_samples)))

df = pd.read_csv("dataset_classification.csv")
X = df.drop(columns=['target']).values
y = df['target'].values

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Define the logistic regression classifier
classifier = LogisticRegression()

# Train the classifier
classifier.fit(X_train, y_train)

# Predict on the training set
y_train_pred = classifier.predict(X_train)

# Predict on the testing set
y_test_pred = classifier.predict(X_test)

# Calculate accuracy
train_accuracy = np.mean(y_train_pred == y_train)
test_accuracy = np.mean(y_test_pred == y_test)
# Plot the training data
plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=plt.cm.Paired, label='Training Data')

# Plot the testing data
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=plt.cm.Paired, marker='x', label='Testing Data')

plt.xlabel('X1')
plt.ylabel('X2')
plt.title('Training and Testing Data')
plt.legend()
plt.show()
print("Training Accuracy:", train_accuracy)
print("Testing Accuracy:", test_accuracy)
