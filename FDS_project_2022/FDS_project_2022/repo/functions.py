from joblib import load

def predictEmotion(x):

    lrModel = load('FDS_project_2022/repo/LogisticRegressionTrainedModel.joblib')
    cv = load('FDS_project_2022/repo/FittedCountVectorizer.joblib')
    x = cv.transform([x])

    res = lrModel.predict(x)
    
    return res
