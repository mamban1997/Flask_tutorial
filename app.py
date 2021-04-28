import pickle
import numpy as np
import sys
import os
from sklearn.neighbors import KNeighborsClassifier
import sqlite3
import random

from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

port = int(os.environ.get('PORT', 5000))

with open('./model.pkl', 'rb') as model_pkl:
    knn = pickle.load(model_pkl)
    
app = Flask(__name__)
iris={
    0:['Setosa', 'irissetosa1.jpg'],
    1:['Versicolor','iris_versicolor_3.jpg'],
    2:['Virginica','iris_virginica.jpg']
}

@app.route('/', methods=('GET', 'POST'))
def predicting():
    name = None
    if request.method == 'POST':
        sl = float(request.form.get('sepallength'))
        sw = float(request.form.get('sepalwidth'))
        pl = float(request.form.get('petallength'))
        pw = float(request.form.get('petalwidth'))
        print(sl, sw, pl, pw)
        param =[sl, sw, pl, pw]
        new_record = np.array([[sl, sw, pl, pw]])
        predict_result = knn.predict(new_record)
        print(predict_result)
        name = iris[predict_result[0]][0]
        path = iris[predict_result[0]][1]
        return render_template('index.html', name=name, path = path, param = param)
    return render_template('index.html', name=name, )

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)