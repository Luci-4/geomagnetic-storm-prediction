from sklearn import preprocessing
from joblib import dump as joblib_dump, load as joblib_load
import pandas as pd

previous_classfier, previous_test_accuracy = joblib_load("gst_prediction.joblib")
print(previous_classfier, previous_test_accuracy)


df = pd.read_csv("new_dataset_classification.csv")

X = preprocessing.normalize(df.drop(columns=['target']).values, norm="max")
y = df['target'].values

y_pred = previous_classfier.predict(X)
print(y_pred)
