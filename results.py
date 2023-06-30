from sklearn import preprocessing
from joblib import dump as joblib_dump, load as joblib_load
import pandas as pd
from sklearn.metrics import confusion_matrix

import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split

obj = joblib_load("gst_models.joblib")


df = pd.read_csv("new_dataset_classification.csv")

X = preprocessing.normalize(df.drop(columns=['target']).values, norm="max")
y = df['target'].values


df = pd.read_csv("dataset_classification.csv")

X = preprocessing.normalize(df.drop(columns=['target']).values, norm="max")
y = df['target'].values
labels = [str(i) for i in list(set(y))]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

for key, stuff in obj.items():
    previous_classfier = stuff[0]
    print(key)
    print(stuff[1])
    print(stuff[2])
    cm = stuff[-2]
    print(cm)
    print(stuff[-1])
    print(30*"_")

    disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                              display_labels=labels)
    disp.plot()
    filename = f"{key}-confusion-matrix.png"
    # plt.savefig(filename)
    # plt.show()


