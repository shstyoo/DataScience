from imdb_predict import imdb_data

# Create imdbget object for our imdb_data class
imdbget = imdb_data()
# Get the imdbdata from the csv file
data = imdbget.getimdbdata('ignore/movie_metadata_updated.csv')
# Select indexes of features and labels we wish to extract
features_list = ['1', '9', '12', '25']
# 2D array from csv data is stored into dataset
dataset = imdbget.setvalues(data, features_list)
# Prune indexes that have bad values
prune_index = []
curr_index = 0
for item in dataset:
	try:
		if float(item[3]) > 10 or float(item[3]) < 0:
			del dataset[curr_index]
			curr_index = curr_index - 1
	except:
		del dataset[curr_index]
		curr_index = curr_index - 1
	curr_index = curr_index + 1
# Split data into labels and features
templabel = []
for item in dataset:
	templabel.append(item[3])
labels = templabel
tempfeature = []
for item in dataset:
	templist = []
#	Stuff testing stuff testing
#	templist.append(item[0])
#	templist.append(item[1])
	templist.append(item[2])
	tempfeature.append(templist)
features = tempfeature
# Training and testing data is partitioned here
X = features
y = labels

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)

from sklearn import tree
my_classifier = tree.DecisionTreeClassifier()
my_classifier.fit(X_train, y_train)
predictions = my_classifier.predict(X_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))
