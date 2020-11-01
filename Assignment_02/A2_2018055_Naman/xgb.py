import pickle
import numpy as np
import random
import csv
import time
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV
from imblearn.under_sampling import NearMiss
import xgboost
start = time.time()

def runner_function(file):
	with open(file,"r") as f:
		reader = csv.reader(f)
		x_test, ids = [], []
		for i in reader:
			if i[0] == "id":
				continue
			x_test.append(i[1:])
			ids.append(i[0])
	y_pred = model.predict(np.array(x_test))
	y_pred = y_pred.tolist()
	with open("pred_xgbr.csv","w") as f:
		writer = csv.writer(f)
		writer.writerow(["id","T"])
		for i in range(len(y_pred)):
			writer.writerow([ids[i],y_pred[i]])
	print ("Answer Predicted! Time Elapsed : ",time.time()-start)

def under_sampling_nm(x, y):
	nm = NearMiss(version = 3)
	x_train, y_train = nm.fit_resample(x, y)
	return x_train, y_train

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

params = {'n_estimators':[100,125],'max_depth':[6,7],'eta':[0.1,0.3,0.5]}
xgb = xgboost.XGBClassifier()
model = GridSearchCV(xgb, params)
model.fit(np.array(x_train), np.array(y_train))
print ("Model Trained! Time Elapsed : ",time.time()-start)
f = open("model_xgb","wb")
pickle.dump(model, f)


f = open("model_xgb","rb")
model = pickle.load(f)
print (model.best_params_)
print (model.best_estimator_)
runner_function("to_predict.csv")



