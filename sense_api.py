#!/usr/bin/python3

from flask import Flask, request
from flask_cors import CORS
from sense_hat import SenseHat

sense = SenseHat()

#clear sensehat and intialise light_state
sense.clear()

app = Flask(__name__)
CORS(app)

@app.route('/sensehat/temp',methods=['GET'])
def current_temp():
    temp=round(sense.get_temperature(),2)
    return str(temp)+"\n"

@app.route('/sensehat/light',methods=['GET'])
def light_get():
    #check top left pixel value(==0 - off, >0 - on) 
    print(sense.get_pixel(0, 0)) 
    if sense.get_pixel(0, 0)[0] == 0:
        return '{"state":"off"}'
    else:
            return '{"state":"on"}'

@app.route('/sensehat/light',methods=['POST'])
def light_post():
    state=request.args.get('state')
    print (state)
    if (state=="on"):
        sense.clear(255,255,255)
        return '{"state":"on"}'
    else: 
        sense.clear(0,0,0)
        return '{"state":"off"}'
    
    
if __name__ == "__main__":
    #Run API on port 5000, set debug to true
    app.run(host='0.0.0.0', port=5000, debug=True)
