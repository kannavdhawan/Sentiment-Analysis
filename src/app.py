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
#app.config['CORS_HEADERS'] = 'Content-Type'
# a= None
# b= None

# temp= {}
# temp["Pie_Chart"] = Pie_dict
# temp["Word Cloud"] = WC_dict
#temp["Negative Tweets"] = NT_dict



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
        
# @app.route('/wordcloud', methods = ['GET'])
# def wordcloud():
#     if request.method == 'GET':
#         place = request.args.get('place')
#         im1 = code(place)[1]
#     print('++++++++++++++++++')
#     print(type(im1))
#     # B = io.BytesIO()
#     # B = session.get('b')
#     return send_file(im1, attachment_filename='plot.png', mimetype='image/png')

# @app.route('/pie', methods = ['GET'])
# def pie():
#     if request.method == 'GET':
#         place = request.args.get('place') 
#         im2 = code(place)
#     print('++++++++++++++++++')
#     print(type(im2))
#     # A = io.BytesIO()
#     # A = session.get('a')
#     return send_file(im2, attachment_filename='pl.png', mimetype='image/png')


# @app.route('/data', methods = ['GET'])
# def Visualizations(): 
#     if request.method == 'GET':
#         place = request.args.get('place')
#         data = code(place)
#         return jsonify(data)

app.run()
