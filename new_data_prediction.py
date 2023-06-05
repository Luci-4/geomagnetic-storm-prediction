from sklearn import preprocessing
from joblib import dump as joblib_dump, load as joblib_load
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

previous_classfier, previous_test_accuracy = joblib_load("gst_prediction.joblib")
print(previous_classfier, previous_test_accuracy)

import pandas as pd

df = pd.read_csv("dataset_classification.csv")

X = preprocessing.normalize(df.drop(columns=['target', 'speed']).values, norm="max")
# X = df.drop(columns=['target', 'latitude']).values

print(previous_classfier, previous_test_accuracy)
y = df['target'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
y_pred = previous_classfier.predict(X_test)
print(confusion_matrix(y_test, y_pred))
