```python
from flask import Flask, render_template
import os
import pandas as pd
from sklearn.externals import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/continue_work')
def continue_work():
    data = pd.read_csv('data/data.csv')
    model = joblib.load('models/model.pkl')
    result = model.predict(data)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```