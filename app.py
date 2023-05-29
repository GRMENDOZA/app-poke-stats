from flask import Flask, render_template, jsonify
from flask_caching import Cache
from src.poke_funtions import getData
import json
import os

app = Flask(__name__)

# Configure cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# Env Vars
timeOut = int(os.getenv("TIME_OUT"))
port = int(os.getenv("PORT"))
debug = os.getenv("DEBUG")

@app.route('/allBerryStats', methods=['GET'])
@cache.cached(timeout = timeOut) # Cache the response for 1 hour
def get_berry_data():
    try:
        return getData()
    except BaseException as error:
        return error
    
@app.route('/allBerryStatsWeb', methods=['GET'])
@cache.cached(timeout = timeOut) # Cache the response for 1 hour
def get_data_web():
    try:
        return render_template('graph.html', **getData('Web'))
    except:
        pass

@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error=str(e)), 404

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = port, debug = debug)
    
