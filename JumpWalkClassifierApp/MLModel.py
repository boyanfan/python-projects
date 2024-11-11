#
# ELEC 292 Final Project - Group 53
# Created by Boyan Fan, Naman Nagia, Walker Yee on 03/31/2024
#

# The following code when run gives the following error: "ValueError: Field names only allowed for compound types"
# the error according to online sources is caused when the x_train and y_train datasets aren't the proper dimensions
# the x_train should be 2D array since each row contains a data point (which to my knowledge should be the 5-second
# interval accelerometer data) and each column containing the actual data and y_train should be a 1D array where each
# index corresponds to a data point and where the element at that index represents the isJump value for that specific
# data point the information above could be incorrect, and it's simply my understanding of it, the error could be
# caused by something else entirely
import h5py
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# load the data from the HDF5 file
with h5py.File('dataset.h5', 'r') as file:
    trainGroup = file['Dataset/Train']
    testGroup = file['Dataset/Test']

    # extracting data from trainGroup into x_train and y_train
    # where x_train contains the raw data and y_train contains the label (isJump)
    X_train = []
    y_train = []
    for i in range(141):
        segment = trainGroup.get(f'segment{i}')
        X_train.append(np.array(segment[:, 1:-1]))  # not sure if the label is called 'data'
        y_train.append(np.array(segment[:, -1]))  # Assuming 'isJump' is the dataset containing corresponding labels
    X_train = np.array(X_train)
    y_train = np.array(y_train)

    # similarly extracting data to test from testGroup
    X_test = []
    y_test = []
    for i in range(len(testGroup)):
        segment = testGroup.get(f'segment{i}')
        X_test.append(np.array(segment[:, 1:-1]))  # Assuming 'data' is the dataset containing accelerometer data
        y_test.append(np.array(segment[:, -1]))  # Assuming 'isJump' is the dataset containing corresponding labels
    X_test = np.array(X_test)
    y_test = np.array(y_test)

# initialize the random forest classifier with online researched values of 100 and 42 for the parameters
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# train the model with the data
rf_classifier.fit(X_train, y_train)

# test the data with test data
y_pred = rf_classifier.predict(X_test)

# determine the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)