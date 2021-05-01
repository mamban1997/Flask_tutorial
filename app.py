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
app.config['SECRET_KEY'] = 'secret key'

iris={
    0:['Setosa', 'irissetosa1.jpg'],
    1:['Versicolor','iris_versicolor_3.jpg'],
    2:['Virginica','iris_virginica.jpg']
}

def get_db_connection():
    conn = sqlite3.connect(r'database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_last_iris():
    conn = get_db_connection()
    last_iris = conn.execute('SELECT created, sepal_length, sepal_width, petal_length,petal_width,type_iris FROM iris_db ORDER BY 1 DESC LIMIT 3').fetchall()
    conn.close()
    if last_iris is None:
        abort(404)
    return last_iris

@app.route('/', methods=('GET', 'POST'))
def predicting():
    name = None
    last_iris = get_last_iris()
    if request.method == 'POST':
        try:
            sl = float(request.form.get('sepallength'))
            sw = float(request.form.get('sepalwidth'))
            pl = float(request.form.get('petallength'))
            pw = float(request.form.get('petalwidth'))
            param =[sl, sw, pl, pw]
            new_record = np.array([[sl, sw, pl, pw]])
            predict_result = knn.predict(new_record)
            name = iris[predict_result[0]][0]
            path = iris[predict_result[0]][1]

            conn = get_db_connection()
            conn.execute("INSERT INTO iris_db (sepal_length, sepal_width,petal_length,petal_width,type_iris) VALUES (?, ?, ?, ?, ?)",
                (sl, sw, pl, pw, name))
            conn.commit()
            conn.close()
            return render_template('index.html', name=name, path = path, param = param, last_iris = last_iris)
        except:
            flash('Enter all parameters!')
            return render_template('index.html', name=name, last_iris=last_iris)
        
    return render_template('index.html', name=name, last_iris=last_iris)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)