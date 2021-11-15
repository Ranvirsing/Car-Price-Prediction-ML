from flask import Flask,jsonify,request
import util 
app=Flask(__name__)

@app.route('/get_est_price', methods = ['POST','GET'])
def get_est_price():
    year=int(request.form['year'])
    km=int(request.form['km'])
    tran=request.form['tran']
    mileage=int(request.form['mileage'])
    fuel=request.form['fuel'] 
    response = jsonify({
        'est_price':util.get_est_price(year,km,tran,mileage,fuel)
        })
    response.headers.add('Access-Control-Allow-Origin','*')
    
    return response


if __name__ == '__main__':
    util.load_artfacts()
    app.run(debug=True)
