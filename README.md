# *This documentation is for deploy Poke-App-Stats in local, it works in python 3.11*

## 1. Install lib virtualenv
`pip install virtualenv`

## 2. Create virtual enviroment called env in root path
`virtualenv env`

## 3. Activate virtualenv
`source env/bin/activate`

## 4. Install dependencies
`pip install -r requirements.txt`

## 5. Run the app
`python app.py`

## 6. Once the app is running, it expouse a web page with data and also an API with the information
* Api http://127.0.0.1:443/allBerryStats METHOD GET
* Web http://127.0.0.1:443/allBerryStatsWeb METHOD GET

## 7. The app is deployed in Heroku, if you want to try you can use the URL's below
* Api https://app-poke-stats.herokuapp.com/allBerryStats METHOD GET
* Web https://app-poke-stats.herokuapp.com/allBerryStatsWeb METHOD GET

