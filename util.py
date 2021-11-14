import pickle
__model = None # these are the instances 


def get_est_price(year,km,tran,mileage,fuel):
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
    return int(__model.predict([[year,km,tran1,mileage,fuel1]])[0]) # this will predict output and [0] bcz without that it will give ouput like [587453] and with zero it will give 587453
def load_artfacts():
    print('loading saved artifacts')   
    global __model    
    with open('./artifacts/carpred.pkl','rb') as f:  # loading saved model
        __model = pickle.load(f)
    print('loading Done')   
        
if __name__ == '__main__':
    load_artfacts()     # calling the methods that will return output
    print(get_est_price(10,150000,'Manual',23,'LPG'))
    print(get_est_price(10,150000,'Manual',23,'Petrol'))
    print(get_est_price(10,150000,'Manual',23,'Diesel'))
    print(get_est_price(10,150000,'Manual',23,'CNG'))