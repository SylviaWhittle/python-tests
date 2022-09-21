#%%
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#%%

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

# Dataset
# print(dataset)

# Shape of the dataset (instances, attributes)
print(dataset.shape)

# Print first 20 rows of the data
print(dataset.head(20))

# Description
print(dataset.describe())

# Class descriptions
print(dataset.groupby('class').size())


# %%

# Univariate plots
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)

# Histograms
dataset.hist()
pyplot.show()

# %% Multivariate plots

# Scatter plot matrix
scatter_matrix(dataset)
pyplot.show()

# %% Validation dataset

# Need an unseen set of data to test the models
# Separate out 20% of the data to keep for later
array = dataset.values
X = array[:,0:4]
Y = array[:, 4]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, Y, test_size = 0.2, random_state=1)
# train is for preparing models and validation is for testing
# random seed is set  to a fixed number so each algo is evaluated on the
# same splits of the training set

# %% Stratified 10 fold cross validation
# Will split data into 10 parts, training on 9 and testing on 1
# then repeat for all combinations of train-test splits

# Stratified means each fold/split of dataset will aim to have same
# distribution of example by class as exist in the whole training 
# dataset

# An explanation on k-fold cross validation:
# https://machinelearningmastery.com/k-fold-cross-validation/
# Briefly:
# Shuffle 
# Split into k groups
# For each unique group:
#   Take group as a test set
#   Take remaining groups as training
#   Fit a model on the training set and evaluate it on the test set
# Summarize the skill using the sample of model evaluation scores

# The metric that I am using is accuracy.
# I am defining accuracy to be the ratio of the number of correctly predited instances
# to to the number of instances in the dataset. 

# Test 6 different algorithms:
# Logistic Regression (LR) (Linear)
# Linear Discriminant Analysis (LDA) (Linear)
# K - Nearest Neighbors (KNN) (Nonlinear)
# Classification and Regression Trees (CART) (Nonlinear)
# Gaussian Naive Bayes (NB) (Nonlinear)
# Support Vector Machines (SVM) (Nonlinear)

# Spot check algos 
models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC(gamma='auto')))
# Evaluate each model in turn
results = []
names = []
for name, model in models:
    kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
    cv_results = cross_val_score(model, X_train, Y_train, cv = kfold, scoring='accuracy')
    results.append(cv_results)
    names.append(name)
    print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

# This provides accuracy estimations for each of the 6 models.
# Compare the models to each other and select the most accurate one.

# %% Compare algos
pyplot.boxplot(results, labels=names)
pyplot.title('Algo Comparison')
pyplot.show()


# %% Make predictions
# Choose model
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)
# This is collecting the predicted data from the validation
# dataset

# %% Evaluate predictions
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

# %%
