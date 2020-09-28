from flask import Flask
from politican import area
import json
app = Flask('__main__')

@app.route('/')
def hello_world():
    return 'good'

@app.route('/area')
def findArea():
    data=area.findArea()
    print(type(data))
    return json.dumps(area.findArea())
    
