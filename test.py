from joblib import dump as joblib_dump, load as joblib_load


current_classfier = joblib_load("gst_prediction.joblib")
