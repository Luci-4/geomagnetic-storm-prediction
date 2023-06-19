from sklearn import preprocessing
from joblib import dump as joblib_dump, load as joblib_load
from sklearn.metrics import confusion_matrix

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split
from imblearn import over_sampling
import pandas as pd

previous_classfier, previous_test_accuracy = joblib_load("gst_prediction.joblib")
print(previous_classfier, previous_test_accuracy)


df = pd.read_csv("dataset_classification.csv")

X = preprocessing.normalize(df.drop(columns=['target', 'speed']).values, norm="max")
# X = df.drop(columns=['target', 'latitude']).values

y = df['target'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

y_pred = previous_classfier.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print("recall", recall_score(y_test, y_pred))
print("f1", f1_score(y_test, y_pred))
print(0.9470588235294117
*0.25
*0.3076923076923077
*(159+2-3-6))


print(0.9529411764705882
*0.9230769230769231
*0.9600000000000001
*(157+12-1))   

