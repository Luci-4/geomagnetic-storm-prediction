import json
import pandas as pd


def get_data_from_json():
    with open("cme_data.json", "r") as f:
        # Load the JSON data into a dictionary
        data = json.load(f)
    return data


def get_the_most_acurate_analysis(cme_analyses):

    for cme_analysis in cme_analyses:
        if cme_analysis["isMostAccurate"]:
            return cme_analysis
    return cme_analyses[-1]


def create_classification_dataset():
    data = get_data_from_json()
    X = []
    Y = []
    for cme in data:
        cme_analyses = cme["cmeAnalyses"]

        if cme_analyses is None:
            continue

        cme_analysis = get_the_most_acurate_analysis(cme_analyses)
        enlilList = cme_analysis.get("enlilList", None)

        if not enlilList:
            continue

        enlilList_elem = enlilList[0]

        x = [
            cme_analysis["longitude"],
            cme_analysis["halfAngle"],
        ]

        if None in x:
            continue
        y = int(enlilList_elem["isEarthGB"])
        X.append(x)
        Y.append(y)
    return X, Y


def create_regression_dataset():
    data = get_data_from_json()
    X = []
    Y = []
    for cme in data:
        cme_analyses = cme["cmeAnalyses"]
        if cme_analyses is None:
            continue

        cme_analysis = get_the_most_acurate_analysis(cme_analyses)

        x = [
            cme_analysis["halfAngle"],
            cme_analysis["speed"],
        ]
        if None in x:
            continue


        linkedEvents = cme["linkedEvents"]
        if linkedEvents is None:
            y = 0
        elif (linked:=[i for i in linkedEvents if "SEP" in i["activityID"] or "IPS" in i["activityID"]]):
            y = len(linked)
        else:
            y = 0

        X.append(x)
        Y.append(y)
    return X, Y


def create_dataframe(X, Y):
    df = pd.DataFrame(X, columns=['longitude', 'halfAngle'])
    df['target'] = Y
    return df


def create_and_load_classification_to_csv():

    X, Y = create_classification_dataset()
    df = create_dataframe(X, Y)
    df.to_csv("dataset_classification.csv", index=False)


def create_and_load_regression_to_csv():
    X, Y = create_regression_dataset()
    df = create_dataframe(X, Y)
    df.to_csv("dataset_regression.csv", index=False)


# create_and_load_regression_to_csv()
create_and_load_classification_to_csv()
