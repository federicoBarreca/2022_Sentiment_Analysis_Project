from joblib import load

# Get a sample in input, extract the features and perform a class prediction
def predictEmotion(x):

    # Load logistic regression trained model
    lrModel = load('FDS_project_2022/repo/LogisticRegressionTrainedModel.joblib')
    
    # Load count vectorizer fitted for the model
    cv = load('FDS_project_2022/repo/FittedCountVectorizer.joblib')

    # Features extraction
    x = cv.transform([x])

    # Prediction
    res = lrModel.predict(x)
    
    return res
