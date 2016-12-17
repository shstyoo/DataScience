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
# Split data into labels and features (Genre has been commented out for now)
templabel = []
for item in dataset:
	templabel.append(item[3])
labels = templabel
tempfeature = []
tempdirector = []
tempgenre = []
for item in dataset:
	templist = []
	# If a director already exists, append his index into the dataset
	if item[0] in tempdirector:
		templist.append(tempdirector.index(item[0]))
	# If a director doesn't exist append him into the director list and append to dataset
	else:
		tempdirector.append(item[0])
		templist.append(tempdirector.index(item[0]))
	# Discretize genre by number
	temp = item[1].split('|')
	temp2 = []
	for genre in temp:
		if genre in tempgenre:
			temp2.append(tempgenre.index(genre))
		else:
			tempgenre.append(genre)
			temp2.append(tempgenre.index(genre))
	templist.append(temp2)
	templist.append(item[2])
	tempfeature.append(templist)
# Our key on directors is here
director_key = tempdirector
# Our genre key is here
genre_key = tempgenre
# Our features are output here
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
