from flask import Flask, render_template
from flask_caching import Cache
from src.poke_funtions import getData
import json
import os

app = Flask(__name__)

# Configure cache
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/allBerryStats', methods=['GET'])
@cache.cached(timeout=int(os.getenv("TIME_OUT"))) # Cache the response for 1 hour
def get_berry_data():
    try:
        return getData()
    except BaseException as error:
        return getErrorResponse(error)
    
@app.route('/allBerryStatsWeb', methods=['GET'])
@cache.cached(timeout=int(os.getenv("TIME_OUT"))) # Cache the response for 1 hour
def get_data_web():
    try:
        return render_template('graph.html', **getData('Web'))
    except:
        pass

def getErrorResponse(error):
    response = app.response_class(
        response=json.dumps({ 'error': '{}'.format(error)}),
        status=400,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.register_error_handler(404, getErrorResponse)
    app.run(host = '0.0.0.0', port = os.getenv("PORT"), debug = os.getenv("DEBUG"))
    
