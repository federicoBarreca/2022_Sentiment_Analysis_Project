from joblib import dump, load



def testFunction(x):

    #dump(cv, 'FDS_project_2022/repo/lrCountVectorizer.joblib')
    #dump(lrModel, 'FDS_project_2022/repo/lrTrainedModel.joblib')

    lrModel = load('FDS_project_2022/repo/lrTrainedModel.joblib')
    cv = load('FDS_project_2022/repo/lrCountVectorizer.joblib')
    x = cv.transform([x])

    res = lrModel.predict(x)
    
    return res
