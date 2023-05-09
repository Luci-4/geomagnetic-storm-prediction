
import matplotlib.pyplot as plt
from sklearn import datasets, preprocessing
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.utils import Bunch
import numpy as np
import pandas as pd

def apply_lda_to_dataset(dataset):
    lda = LinearDiscriminantAnalysis(n_components=2)

    x = dataset.data
    y = dataset.target
    print(x.shape, y.shape)
    # lda.fit(x, y)

    colors_map = {e: i+1 for i, e in enumerate(list(set(list(y))))}
    X_lda = lda.fit_transform(x, y)
    print(x.shape)
    print(X_lda.shape)

    plt.scatter(X_lda[:, 0], X_lda[:, 1], c=[colors_map[e] for e in list(y)],
)
    plt.xlabel('LD1')
    plt.ylabel('LD2')
    plt.title('LDA on dataset')
    plt.show()


df = pd.read_csv("dataset_classification.csv")
X = df.drop(columns=['target', 'halfAngle']).values
y = df['target'].values
dataset = Bunch(data=X, target=y)
apply_lda_to_dataset(dataset)
