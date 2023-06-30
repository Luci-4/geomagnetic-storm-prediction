from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, recall_score, f1_score, confusion_matrix, classification_report


from joblib import dump as joblib_dump, load as joblib_load
import pandas as pd

# df = pd.read_csv("dataset_classification.csv")
df = pd.read_csv("dataset_classification.csv")

X = preprocessing.normalize(df.drop(columns=['target']).values, norm="max")
# X = df.drop(columns=['target', 'latitude']).values
y = df['target'].values
labels = [str(i) for i in list(set(y))]


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

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    classifier_obj = classifier()

    classifier_obj.fit(X_train, y_train)

    y_train_pred = classifier_obj.predict(X_train)
    y_test_pred = classifier_obj.predict(X_test)

    train_accuracy = classifier_obj.score(X_train, y_train)
    test_accuracy = classifier_obj.score(X_test, y_test)
    recall = recall_score(y_test, y_test_pred)
    f1 = f1_score(y_test, y_test_pred)
    confusion_mx = confusion_matrix(y_test, y_test_pred)
    print(train_accuracy, test_accuracy, recall, f1, confusion_mx) 
    report = classification_report(y_test, y_test_pred, target_names=labels)
    return classifier_obj, train_accuracy, test_accuracy, recall, f1, confusion_mx, report


def train_and_save():

    results = []
    for classifier_cls, classifier_name in zip(classifiers, classifiers_names):

        classifier, train_accuracy, test_accuracy, recall, f1, confusion_mx, report = train(classifier_cls, classifier_name)
        results.append((
                classifier,
                classifier_name,
                train_accuracy,
                test_accuracy,
                recall,
                f1,
                confusion_mx,
                report

            ))

    results.sort(reverse=True, key=lambda x: x[3])
    # pprint(results[0][1:])
    # classifier, classifier_name, train_accuracy, test_accuracy = results[0]
    for classifier, classifier_name, train_accuracy, test_accuracy, recall, f1, confusion_mx, report in results:

        classifiers_obj = joblib_load("gst_models.joblib")
        previous_classfier, previous_test_accuracy, previous_train_accuracy, previous_recall, previous_f1, previous_confusion_mx, previous_report = classifiers_obj.get(classifier_name, (None, 0, 0, 0, 0, [[-1000, -1000], [-1000, -1000]], {}))
        if test_accuracy > previous_test_accuracy:
            classifiers_obj[classifier_name] = (classifier, test_accuracy, train_accuracy, recall, f1, confusion_mx, report)
            # pprint(classifiers_obj)

            joblib_dump(classifiers_obj, "gst_models.joblib")


joblib_dump({}, "gst_models.joblib")


for _ in range(100):
    train_and_save()
obj_ = joblib_load("gst_models.joblib")
items = [k for k in obj_.items()]
items.sort(key=lambda x: x[1][1])

for k, (obj, test_, train_, recall_, f1_, confusion_matrix_, report_) in obj_.items():
    print(k)
    print(test_)
    print(train_)
    print(recall_)
    print(f1_)
    print(confusion_matrix_)
    print(report_)
    print(30*"-")
    print()
