from sklearn import preprocessing
from joblib import dump as joblib_dump, load as joblib_load
import pandas as pd
from sklearn.metrics import confusion_matrix

import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split

obj = joblib_load("gst_models.joblib")
previous_classfier, previous_test_accuracy = joblib_load("gst_prediction.joblib")
print(previous_classfier, previous_test_accuracy)


df = pd.read_csv("new_dataset_classification.csv")

X = preprocessing.normalize(df.drop(columns=['target']).values, norm="max")
y = df['target'].values

import pandas as pd

df = pd.read_csv("dataset_classification.csv")

X = preprocessing.normalize(df.drop(columns=['target', 'speed']).values, norm="max")
# X = df.drop(columns=['target', 'latitude']).values
y = df['target'].values
labels = [str(i) for i in list(set(y))]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

for key, stuff in obj.items():
    previous_classfier = stuff[0]

    # y_test_pred = previous_classfier.predict(X_test)
    # y_pred = previous_classfier.predict(X)
    cm = stuff[-2]

    # print(cm)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                              display_labels=labels)
    # disp.plot()
    filename = f"{key}-confusion-matrix.png"
    print(filename)
    continue
    # plt.savefig(filename)
    # plt.show()

    # classification_report(y_test, Y_pred, target_names=target_names)

