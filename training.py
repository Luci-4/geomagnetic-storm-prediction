import numpy as np

from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import confusion_matrix
from pprint import pprint

from joblib import dump as joblib_dump, load as joblib_load
import pandas as pd

df = pd.read_csv("dataset_classification.csv")

X = preprocessing.normalize(df.drop(columns=['target', 'speed']).values, norm="max")
# X = df.drop(columns=['target', 'latitude']).values
y = df['target'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

classifiers = [
        SVC,
        LogisticRegression,
        RandomForestClassifier,
        GaussianNB,
        KNeighborsClassifier,
        DecisionTreeClassifier
]
classifiers_names = [
        "SVC",
        "LogisticRegression",
        "RandomForestClassifier",
        "GaussianNB",
        "KNeighborsClassifier",
        "DecisionTreeClassifier"
]


def train(classifier, classifier_name):
    classifier_obj = classifier()

    classifier_obj.fit(X_train, y_train)

    y_train_pred = classifier_obj.predict(X_train)
    y_test_pred = classifier_obj.predict(X_test)

    train_accuracy = classifier_obj.score(X_train, y_train)
    test_accuracy = classifier_obj.score(X_test, y_test)
    return classifier_obj, train_accuracy, test_accuracy


def train_and_save():

    results = []
    for classifier_cls, classifier_name in zip(classifiers, classifiers_names):

        classifier, train_accuracy, test_accuracy = train(classifier_cls, classifier_name)
        # print(30*"-")
        # print(type(classifier))
        # print(30*"-")
        # print(classifier.feature_importances_)
        results.append((
                classifier,
                classifier_name,
                train_accuracy,
                test_accuracy
            ))

    results.sort(reverse=True, key=lambda x: x[3])
    # pprint(results[0][1:])
    classifier, classifier_name, train_accuracy, test_accuracy= results[0]

    try:
        previous_classfier, previous_test_accuracy = joblib_load("gst_prediction.joblib")
    except FileNotFoundError:
        previous_classfier = None
        previous_test_accuracy = 0

    # print(f"{test_accuracy =} > {previous_test_accuracy =}")
    if test_accuracy > previous_test_accuracy:
        # print(classifier)
        obj = (classifier, test_accuracy)
        joblib_dump(obj, "gst_prediction.joblib")

for _ in range(30):
    train_and_save()
# for (classifier, classifier_name, train_accuracy, test_accuracy) in results:
#     print(classifier_name)
#     print("Training Accuracy:", train_accuracy)
#     print("Testing Accuracy:", test_accuracy)
#     print(30*"-")
#     print()
