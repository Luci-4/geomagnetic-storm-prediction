import json

import pandas as pd
from datetime import datetime
FLRClasses = [

    "A",
    "B",
    "C",
    "M",
    "X"
]

def calculate_FLR_power(class_type):
    flr_class = class_type[0]

    score = float(class_type[1:])

    end = 10**(FLRClasses.index(flr_class) + 1)
    start = 10**(FLRClasses.index(flr_class))
    range = end - start;
    relativeScore = 0.1*score*range
    absoluteScore = start + relativeScore
    return absoluteScore

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


def get_data_from_json():
    with open("flr_data.json", "r") as f:
        # Load the JSON data into a dictionary
        data = json.load(f)
    return data


def create_classification_dataset():
    data = get_data_from_json()
    X = []
    Y = []
    for flr in data:


        x = [
            flr["activeRegionNum"],
            calculate_FLR_power(flr["classType"])
        ]

        if None in x:
            continue
        if not flr["linkedEvents"]:
            continue
        y = int(bool(flr["linkedEvents"]) and any([("CME" in i["activityID"]) for i in flr["linkedEvents"]]))
        X.append(x)
        Y.append(y)
    return X, Y

def create_dataframe(X, Y):

    df = pd.DataFrame(X, columns=['activeRegionNum', 'classType'])
    df['target'] = Y
    return df

def create_and_load_classification_to_csv():

    X, Y = create_classification_dataset()
    df = create_dataframe(X, Y)
    df.to_csv("dataset_classification.csv", index=False)

create_and_load_classification_to_csv()
