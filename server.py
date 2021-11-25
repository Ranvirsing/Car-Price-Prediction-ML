from flask import Flask,jsonify, render_template, request,url_for
import requests
import pickle
app = Flask(__name__)
model = pickle.load(open('carpred.pkl', 'rb'))
@app.route('/')
def Home():
    return render_template('app.html')

@app.route("/predict", methods=['POST'])
def predict():
    year=int(request.form.get('years'))
    km=int(request.form.get('kms'))
    tran=request.form.get('trans')
    mileage=int(request.form.get('ml'))
    fuel=request.form.get('fuels')
    if(tran=='Manual'):
        tran1=0
    else:
        tran1=1
    if(fuel=='Petrol'):
        fuel1=0
    elif(fuel=='Diesel'):
        fuel1=1
    elif(fuel=='LPG'):
        fuel1=2
    else:
        fuel1=3 
    output=int(model.predict([[year,km,tran1,mileage,fuel1]])[0])
    if output<0:
        return render_template('app.html',prediction_texts="Sorry you cannot sell this car")
    else:
        return render_template('app.html',prediction_text="You Can Sell The Car at {}".format(output))


if __name__=="__main__":
    app.run(debug=True)
