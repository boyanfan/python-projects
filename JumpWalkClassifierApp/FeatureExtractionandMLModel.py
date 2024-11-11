#
# ELEC 292 Final Project - Group 53
# Created by Boyan Fan, Naman Nagia, Walker Yee on 04/06/2024
#

import h5py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
import joblib

with h5py.File('./dataset_aftermovingMAFilter.h5', 'r') as hdf:
    features = ['x mean', 'y mean', 'z mean', 'x max', 'y max', 'z max', 'x min', 'y min', 'z min', 'x range', 'y range', 'z range', 'x median', 'y median','z median', 'x var', 'y var', 'z var', 'x skew', 'y skew', 'z skew', 'x std', 'y std', 'z std', 'isJump']
    feature_extracted_array=np.array([features])
    for i in range(141): #get features from training set
        set = hdf.get(f'Dataset/Train/segment{i}')
        array = np.array(set)  # convert segment to array
        dataset = pd.DataFrame(array)  # convert array to dataframe
        xmean=dataset[1].mean()
        ymean = dataset[2].mean()
        zmean = dataset[3].mean()
        xmax = dataset[1].max()
        ymax = dataset[2].max()
        zmax = dataset[3].max()
        xmin = dataset[1].min()
        ymin = dataset[2].min()
        zmin = dataset[3].min()
        xrange = (dataset[1].max()-(dataset[1].min()))
        yrange = (dataset[2].max())-(dataset[2].min())
        zrange = (dataset[3].max())-(dataset[3].min())
        xmed = dataset[1].median()
        ymed = dataset[2].median()
        zmed = dataset[3].median()
        xvar = dataset[1].var()
        yvar = dataset[2].var()
        zvar = dataset[3].var()
        xskew = dataset[1].skew()
        yskew = dataset[2].skew()
        zskew = dataset[3].skew()
        xstd = dataset[1].std()
        ystd = dataset[2].std()
        zstd = dataset[3].std()
        isJump = int(dataset[4].mean())
        feature_array = np.array([xmean, ymean, zmean, xmax,ymax,zmax,xmin,ymin,zmin,xrange,yrange,zrange,xmed,ymed,zmed,xvar,yvar,zvar,xskew,yskew,zskew,xstd,ystd,zstd,isJump])
        feature_extracted_array = np.vstack((feature_extracted_array,feature_array))

    testfeature_extracted_array=np.array([features])
    for j in range(16): #get features from test set
        test_set = hdf.get(f'Dataset/Test/segment{j}')
        test_array = np.array(test_set)  # convert segment to array
        test_dataset = pd.DataFrame(test_array)  # convert array to dataframe
        xmean = test_dataset[1].mean()
        ymean = test_dataset[2].mean()
        zmean = test_dataset[3].mean()
        xmax = test_dataset[1].max()
        ymax = test_dataset[2].max()
        zmax = test_dataset[3].max()
        xmin = test_dataset[1].min()
        ymin = test_dataset[2].min()
        zmin = test_dataset[3].min()
        xrange = (test_dataset[1].max() - (test_dataset[1].min()))
        yrange = (test_dataset[2].max()) - (test_dataset[2].min())
        zrange = (test_dataset[3].max()) - (test_dataset[3].min())
        xmed = test_dataset[1].median()
        ymed = test_dataset[2].median()
        zmed = test_dataset[3].median()
        xvar = test_dataset[1].var()
        yvar = test_dataset[2].var()
        zvar = test_dataset[3].var()
        xskew = test_dataset[1].skew()
        yskew = test_dataset[2].skew()
        zskew = test_dataset[3].skew()
        xstd = test_dataset[1].std()
        ystd = test_dataset[2].std()
        zstd = test_dataset[3].std()
        isJump = int(test_dataset[4].mean())
        testfeature_array = np.array([xmean, ymean, zmean, xmax, ymax, zmax, xmin, ymin, zmin, xrange, yrange, zrange, xmed, ymed, zmed, xvar, yvar, zvar, xskew, yskew, zskew, xstd, ystd, zstd, isJump])
        testfeature_extracted_array = np.vstack((testfeature_extracted_array, testfeature_array))


#delete column names(not needed)
feature_extracted_array = np.delete(feature_extracted_array,0,0)
testfeature_extracted_array = np.delete(testfeature_extracted_array,0,0)

#turn arrays into datasets
features_dataset = pd.DataFrame(feature_extracted_array)
testfeatures_dataset = pd.DataFrame(testfeature_extracted_array)
#drop any NaN values, if any
features_dataset.dropna(inplace=True)
testfeatures_dataset.dropna(inplace=True)


#get labels and data for test and training sets
train_labels=features_dataset.iloc[:,-1]
train_data=features_dataset.iloc[:,1:-1]
test_labels = testfeatures_dataset.iloc[:,-1]
test_data = testfeatures_dataset.iloc[:,1:-1]

X_train = train_data
Y_train = train_labels
X_test = test_data
Y_test = test_labels

#normalize data and perform logistic regreesion
scaler = StandardScaler()
l_reg = LogisticRegression(max_iter=10000)
clf = make_pipeline(scaler, l_reg)
clf.fit(X_train, Y_train)

joblib.dump(clf, 'model.pkl')

#test model
y_pred = clf.predict(X_test)
y_clf_prob = clf.predict_proba(X_test)

acc=accuracy_score(Y_test,y_pred)
print('accuracy is:',acc)