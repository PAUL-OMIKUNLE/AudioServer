from flask import Flask,render_template,request,url_for
import pandas as pd 
import numpy as np 



app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/predict',methods=["GET","POST"])


	return render_template('index.html',prediction=my_prediction,pred_score=pred_score,verse_sentiment=verse_sentiment,raw_text=raw_text)


if __name__ == '__main__':
	app.run(debug=True)
© 2021 GitHub, Inc.
