# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:21:59 2024

@author: STORM
"""
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data_dict = pickle.load(open('./data.pickle','rb'))

data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

x_train,x_test,y_train,y_test = train_test_split(data,labels,test_size=0.2,shuffle=True,stratify=labels)

model = RandomForestClassifier()

model.fit(x_train,y_train)

y_predict = model.predict(x_test)

accuracy = accuracy_score(y_test,y_predict)

print('{}% of samples weere classified correctly !'.format(accuracy*100))

f = open('model.p','wb')
pickle.dump({'model':model},f)
f.close()
