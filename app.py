from flask import Flask, render_template,request,url_for
import pickle

with open('floodpred.pkl', 'rb') as f:
    model = pickle.load(f)
    
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    return "not complete"
    
if __name__ == "__main__":
    app.run(debug=True)
