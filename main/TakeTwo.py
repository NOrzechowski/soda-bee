import numpy as np
import pandas
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

from main.CoasterUtils import CoasterUtils

var = int(input("Please enter a number: "))
print("You entered " + str(var))

utils = CoasterUtils()
training_data = np.array([utils.encode(i) for i in range(1, 20)])
validation_data = np.array([utils.encode(i) for i in range(1, var+1)])

data_set = pandas.DataFrame(training_data, columns=utils.get_attribute_names())
validation_set = pandas.DataFrame(validation_data, columns=utils.get_attribute_names())

# Split up data
array = data_set.values
X = array[:,0:8]
Y = array[:,8]
validation_size = 0
seed = 1
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# Test options and evaluation metric
seed = 7
scoring = 'accuracy'

# algorithm used
name = 'KNN'
model = KNeighborsClassifier()

# Evaluate
results = []
attribute_names = []
kfold = model_selection.KFold(n_splits=10, random_state=seed)
cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
results.append(cv_results)
attribute_names.append(name)
msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())


# Make predictions on training dataset
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)

# Validate
validation_array = validation_set.values
X_val = validation_array[:, 0:8]
Y_val = validation_array[:, 8]
predictions = knn.predict(X_val)

i = 1
for item in predictions:
    if item == "number":
        print(str(i), end=' ')
    else:
        print(item, end=' ')
    i += 1

print(accuracy_score(Y_val, predictions))
print(confusion_matrix(Y_val, predictions))
print(classification_report(Y_val, predictions))
