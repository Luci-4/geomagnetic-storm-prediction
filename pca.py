import matplotlib.pyplot as plt
from sklearn import datasets, preprocessing
from sklearn.decomposition import PCA
import pandas as pd
from sklearn.utils import Bunch


def apply_pca_to_dataset(dataset):

    x = dataset.data
    y = dataset.target
    fig = plt.figure(1, figsize=(8, 6))
    ax = fig.add_subplot(111)
    x = preprocessing.StandardScaler().fit_transform(x)
    X_reduced = PCA(n_components=2).fit_transform(x)
    colors_map = {e: i+1 for i, e in enumerate(list(set(list(y))))}
    print((list(colors_map.keys())))
    ax.scatter(
        X_reduced[:, 0],
        X_reduced[:, 1],
        c=[colors_map[e] for e in list(y)],
        cmap=plt.cm.Set1,
        edgecolor="k",
        s=40,
    )

    ax.set_title("First two PCA directions")
    ax.set_xlabel("1st eigenvector")
    ax.xaxis.set_ticklabels([])
    ax.set_ylabel("2nd eigenvector")
    ax.yaxis.set_ticklabels([])

    plt.show()


df = pd.read_csv("dataset_classification.csv")
X = df.drop(columns=['target', "latitude"]).values
y = df['target'].values
print(X)
dataset = Bunch(data=X, target=y)
apply_pca_to_dataset(dataset)
