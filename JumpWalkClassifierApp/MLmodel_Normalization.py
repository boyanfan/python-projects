import h5py
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# using z-score normalization
def normalize_data(data):
    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(data)
    return normalized_data

hdf5_file_path = './dataset_aftermovingMAFilter.h5'

X_train = []
y_train = []
with h5py.File(hdf5_file_path, 'r') as hdf:
    for i in range(141):
        segment_path = f'Dataset/Train/segment{i}'
        segment = hdf[segment_path][:]
        if len(segment) != 0:  # make sure segment isn't empty for error purposes
            labels = segment[:, -1]  # getting labels from last column
            # aggregate labels array into one value
            aggregated_label = np.sum(labels)
            # aggregated_label = np.argmax(np.bincount(labels))
            X_train.append(segment[:, :-1])  # extract data (everything but last column)
            y_train.append(aggregated_label)

# convert to numpy arrays
X_train = np.array(X_train)
y_train = np.array(y_train).astype(int)  # Convert labels to integer type

# normalize data before training
X_train_normalized = normalize_data(X_train)

# checking for NaN or infinite values in the normalized features for the erros
if np.isnan(X_train_normalized).any() or np.isinf(X_train_normalized).any():
    print("NaN or infinite values found in the normalized features. Please check your data preprocessing.")
else:
    # just using test train split for simplicity
    X_train_split, X_test_split, y_train_split, y_test_split = train_test_split(X_train_normalized, y_train, test_size=0.2, random_state=42)

    # train logistic regression model
    logreg_model = LogisticRegression()
    logreg_model.fit(X_train_split, y_train_split)

    # predict
    y_pred = logreg_model.predict(X_test_split)

    # determine accuracy
    accuracy = accuracy_score(y_test_split, y_pred)
    print("Accuracy:", accuracy)
