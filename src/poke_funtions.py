from flask import Flask, jsonify, Response, render_template
import requests
import io
import matplotlib 
import matplotlib.pyplot as plt
import base64
import json
matplotlib.use('agg')


def getData(typeResponse = 'Api'):
    #Get data from PokeAPI
    response = requests.get('https://pokeapi.co/api/v2/berry/')

    if response.status_code == 200:
        data = response.json()
        berries = data['results']
        urlNextData = data['next']

        # Get all the information
        while urlNextData != None:
            response = requests.get(urlNextData)
            if response.status_code == 200:
                data = response.json()
                tempBerries = data['results']
                urlNextData = data['next']
                berries.extend(tempBerries)
            else:
                break
        
        return getDataBerries(berries, typeResponse)
    else:
        return Response(
        response='El servicio no esta disponible',
        status=400,
        mimetype='application/json',
        headers={'Content-Disposition': 'inline'},
        direct_passthrough=True
    )

def getDataBerries(berries, typeResponse):
    # Get data from berries URL's
    names = []
    growthTimes = []
    for berry in berries:
        berryResponse = requests.get(berry['url'])
        berryData = berryResponse.json()
        names.append(berryData['name'].capitalize())
        growthTimes.append(berryData['growth_time'])

    # Calculate data
    min_growth_time = min(growthTimes)
    median_growth_time = sorted(growthTimes)[len(growthTimes) // 2]
    max_growth_time = max(growthTimes)
    variance_growth_time = round(sum((x - sum(growthTimes) / len(growthTimes)) ** 2 for x in growthTimes) / len(growthTimes), 2)
    mean_growth_time = round(sum(growthTimes) / len(growthTimes), 2)

    frequency_growth_time = {}
    for time in growthTimes:
        frequency_growth_time[time] = frequency_growth_time.get(time, 0) + 1

    # Response
    response_data = {
        "berries_names": names,
        "min_growth_time": min_growth_time,
        "median_growth_time": median_growth_time,
        "max_growth_time": max_growth_time,
        "variance_growth_time": variance_growth_time,
        "mean_growth_time": mean_growth_time,
        "frequency_growth_time": frequency_growth_time
    }

    if typeResponse == 'Web':
        # Create HistoGraph
        fig, ax = plt.subplots()
        ax.hist(growthTimes, bins='auto')
        ax.set_xlabel('Growth Time')
        ax.set_ylabel('Frequency')
        ax.set_title('Poke-Berries Growth Time Histogram')

        image_stream = io.BytesIO()
        plt.savefig(image_stream, format='png')
        plt.close(fig)
        image_stream.seek(0)
        
        # Encode Image
        image_base64 = base64.b64encode(image_stream.read()).decode('utf-8')

        # Add image to Response
        response_data['histogram_image'] = image_base64       

        return response_data
    
    return Response(
        response=jsonify(response_data).data,
        status=200,
        mimetype='application/json',
        headers={'Content-Disposition': 'inline'},
        direct_passthrough=True
    )