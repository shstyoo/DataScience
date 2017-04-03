import sys
import os
import time

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report

def usage():
    print("Usage:")
    print("python %s <train_dir> <test_dir>" % sys.argv[0])

if __name__ in '__main__':
    if len(sys.argv) < 3:
        usage()
        sys.exit(1)

    train_dir = sys.argv[1]
    test_dir = sys.argv[2]
    classes = ['pos', 'neg']

    train_data = []
    train_labels = []
    test_data = []
    test_labels = []
    for _class in classes:
        dirname = os.path.join(train_dir, _class)
        i = 0
        for fname in os.listdir(dirname):
            with open(os.path.join(dirname, fname), 'r', errors='ignore') as f:
                content = f.read()
                train_data.append(content)
                train_labels.append(_class)
        dirname = os.path.join(test_dir, _class)
        i = 0
        for fname in os.listdir(dirname):
            with open(os.path.join(dirname, fname), 'r', errors='ignore') as f:
                content = f.read()
                test_data.append(content)
                test_labels.append(_class)
    print('vector start')
    vectorizer = TfidfVectorizer(min_df=5,
                                 max_df=.8,
                                 sublinear_tf=True,
                                 use_idf=True,
                                 decode_error='ignore')
    train_vectors = vectorizer.fit_transform(train_data)
    test_vectors = vectorizer.transform(test_data)
    print('classifier rbf start')
    classifier_rbf = svm.SVC()
    t0 = time.time()
    classifier_rbf.fit(train_vectors, train_labels)
    t1 = time.time()
    prediction_rbf = classifier_rbf.predict(test_vectors)
    t2 = time.time()
    time_rbf_train = t1-t0
    time_rbf_predict = t2-t1
    print('linear classifier start')
    classifier_linear = svm.SVC(kernel='linear')
    t0 = time.time()
    classifier_linear.fit(train_vectors, train_labels)
    t1 = time.time()
    prediction_linear = classifier_linear.predict(test_vectors)
    t2 = time.time()
    time_linear_train = t1-t0
    time_linear_predict = t2-t1
    print('liblinear classifier start')
    classifier_liblinear = svm.LinearSVC()
    t0 = time.time()
    classifier_liblinear.fit(train_vectors, train_labels)
    t1 = time.time()
    prediction_liblinear = classifier_liblinear.predict(test_vectors)
    t2 = time.time()
    time_liblinear_train = t1-t0
    time_liblinear_predict = t2-t1

    # Print results in a nice table
    print("Results for SVC(kernel=rbf)")
    print("Training time: %fs; Prediction time: %fs" % (time_rbf_train, time_rbf_predict))
    print(classification_report(test_labels, prediction_rbf))
    print("Results for SVC(kernel=linear)")
    print("Training time: %fs; Prediction time: %fs" % (time_linear_train, time_linear_predict))
    print(classification_report(test_labels, prediction_linear))
    print("Results for LinearSVC()")
    print("Training time: %fs; Prediction time: %fs" % (time_liblinear_train, time_liblinear_predict))
    print(classification_report(test_labels, prediction_liblinear))
