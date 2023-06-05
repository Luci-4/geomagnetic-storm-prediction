import json
import pandas as pd
from datetime import datetime


def get_data_from_json(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data


def get_the_most_acurate_analysis(cme_analyses):

    for cme_analysis in cme_analyses:
        if cme_analysis["isMostAccurate"]:
            return cme_analysis
    return cme_analyses[-1]


def convert_activity_id_to_datetime(activity_id):
    date_string = activity_id[:19]
    return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")


def convert_to_event_code(text: str):
    codes = [
        "GST",
        "FLR",
        "IPS",
        "SEP",
        "MPC",
        "RBE"
    ]
    for code in codes:
        if code in text:
            return code


def get_cme_data_point(cme):

    cme_analyses = cme["cmeAnalyses"]

    if cme_analyses is None:
        return

    cme_analysis = get_the_most_acurate_analysis(cme_analyses)
    enlilList = cme_analysis.get("enlilList", None)

    if not enlilList:
        return

    # enlilList_elem = enlilList[0]
    # if enlilList_elem["isEarthGB"]:
    #     print(cme["linkedEvents"])

    x = [
        cme_analysis["latitude"],
        cme_analysis["longitude"],
        cme_analysis["halfAngle"],
    ]

    if None in x:
        return
    if not cme["linkedEvents"]:
        return

    y = int(bool(cme["linkedEvents"]) and any([("GST" in i["activityID"]) for i in cme["linkedEvents"]]))
    return x, y


def create_classification_dataset(source_json_filename):
    data = get_data_from_json(source_json_filename)
    X = []
    Y = []
    column_labels = ['latitude', 'longitude', 'halfAngle']
    for cme in data:
        data_point = get_cme_data_point(cme)
        if data_point is None:
            continue
        x, y = data_point
        X.append(x)
        Y.append(y)

    df = pd.DataFrame(X, columns=column_labels)
    df['target'] = Y
    return df


def create_and_load_classification_to_csv():
    df = create_classification_dataset("current_cme_data.json")
    df.to_csv("new_dataset_classification.csv", index=False)


create_and_load_classification_to_csv()
