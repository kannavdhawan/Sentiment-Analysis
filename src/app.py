from flask import Flask, send_file, make_response, session
from flask import request, jsonify
#from NEw_modification import do_plot
import matplotlib.pyplot as plt
import io
#import M0_main
from M0_main import code
#from NEw_modification import Pie_dict, WC_dict
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.config['DEBUG'] = True
cors = CORS(app)




@app.route('/', methods = ['GET'])
def home():
    return "<h1> Welcome </h1>"


@app.route('/word', methods = ['GET', 'POST'])
def wordspace():
    if request.method == 'GET':
        place = request.args.get('place')
        #place = request.args['place']
        data = code(place)

        return jsonify(data)
        #global a, b
        # session['a'] = code(place)[0]
        # session['b'] = code(place)[1]

        #print('+++++++++++++')
        #print(type(a))
        


app.run()
