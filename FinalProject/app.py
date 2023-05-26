from flask import Flask,render_template,request
import pickle
import numpy as np
app = Flask(__name__,template_folder='./templates',static_folder='./static')

model = pickle.load(open('classi.pkl', 'rb'))

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def homeq():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    data7 = request.form['g']
    data8 = request.form['h']
    data9 = request.form['i']
    data10 = request.form['j']
    data11 = request.form['k']
    data12 = request.form['l']
    data13 = request.form['m']
   # a = [[data1, data2, data3, data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
   # arr = np.array(a,dtype=float)
   # pred = model.predict(arr)
    return render_template('after.html', data=int(data7))

if __name__ == "__main__":
    app.run(debug=True)