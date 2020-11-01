import pickle
import numpy as np
import random
import csv
import time
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import xgboost
start = time.time()

def accuracy(a,b):
	correct = 0
	for i in range(len(a)):
		if a[i]==b[i]:
			correct += 1
	return correct/len(a)

def under_sampling_random(x, y):
	a, x_train, y_train = [], [], []
	for i in range(len(x)):
		if y[i]==1:
			a.append(x[i]+[y[i]])
		else:
			x_train.append(x[i])
			y_train.append(y[i])
	random.shuffle(a)
	for i in range(len(x_train)):
		x_train.append(a[i][:-1])
		y_train.append(a[i][-1])
	return x_train, y_train

with open("given_dataset.csv","r") as f:
	reader = csv.reader(f)
	x_train, y_train, x, y = [], [], [], []
	for i in reader:
		if i[0] == "id":
			continue
		x.append(list(map(float,i[1:-1])))
		y.append(float(i[-1]))

x_train, y_train = under_sampling_random(x,y)
x_train, x_test, y_train, y_test = train_test_split(x_train, y_train)

d, train_acc, test_acc = [], [], []
for depth in range(5,25):
	model = xgboost.XGBClassifier(max_depth=depth)
	model.fit(np.array(x_train), np.array(y_train))
	print ("Model Trained! Time Elapsed : ",time.time()-start)
	y_pred_test = model.predict(np.array(x_test))
	y_pred_train = model.predict(np.array(x_train))
	d.append(depth)
	train_acc.append(accuracy(y_train, y_pred_train))
	test_acc.append(accuracy(y_test, y_pred_test))

plt.plot(d, train_acc, label="Training Accuracy")
plt.plot(d, test_acc, label="Testing Accuracy")
plt.legend()
plt.xlabel("Max Depth")
plt.show()

d, train_acc, test_acc = [], [], []
for n_estimator in range(50,151,25):
	model = xgboost.XGBClassifier(n_estimators=n_estimator)
	model.fit(np.array(x_train), np.array(y_train))
	print ("Model Trained! Time Elapsed : ",time.time()-start)
	y_pred_test = model.predict(np.array(x_test))
	y_pred_train = model.predict(np.array(x_train))
	d.append(n_estimator)
	train_acc.append(accuracy(y_train, y_pred_train))
	test_acc.append(accuracy(y_test, y_pred_test))

plt.plot(d, train_acc, label="Training Accuracy")
plt.plot(d, test_acc, label="Testing Accuracy")
plt.legend()
plt.xlabel("n_estimators")
plt.show()



