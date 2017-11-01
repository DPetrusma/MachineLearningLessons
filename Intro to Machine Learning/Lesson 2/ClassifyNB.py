def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
    from sklearn.naive_bayes import GaussianNB
    from sklearn.svm import SVC
    
    #My_Classifier = GaussianNB()
    My_Classifier = SVC(C = 100, gamma = 20)
    My_Classifier.fit(features_train, labels_train)
    
    
    
    return My_Classifier
    
    