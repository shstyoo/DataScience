import random
# Import math libraries to calculate nearest distance
from scipy.spatial import distance

# Define our function to return the nearest distance between two pair of points
def euc(a,b):
    return distance.euclidean(a,b)

# Define our K-NN function (note only takes into account the nearest neighbor as K is hardcoded as 1)
class scrappyknn():
    # Constructor class
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    # Predict the labels using our closest function
    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    # Define our closest classifier to use euc(a,b) to find shortest distance
    def closest(self, row):
        # We find the first point in our dataset and set that as our best point (shortest point)
        best_dist = euc(row, self.X_train[0])
        # The best index of the item is 0
        best_index = 0
        # We then iterate over every single value in the training set to find the shortest distance
        for i in range(1, len(self.X_train)):
            # We use euc(a,b) here to find the shortest distance regularily update best_dict and best_index
            dist = euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        # Once the code is complete we then return the index with the best value
        return self.y_train[best_index]

# Import our iris dataset
from sklearn.datasets import load_iris
iris = load_iris()

# The training and testing data is partitioned here
X = iris.data
y = iris.target

# We split the iris dataset and the labels into half
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)

# These two lines can be changed to fit other classifiers (such as K-neighbors) to test the fit of data
# This particular scrappyKNN is created above
my_classifier = scrappyknn()
my_classifier.fit(X_train, y_train)

print(y_train[0])

predictions = my_classifier.predict(X_test)
print(predictions)

from sklearn.metrics import accuracy_score
print accuracy_score(y_test, predictions)
