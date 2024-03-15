# This ia a new version of the lambda function. 
# The code is used to get only the temperature in Celcius for a given latitude and longitude.
import json
import urllib3

def lambda_handler(event, context):
    # Log the event argument for debugging and for use in local development.
    print(json.dumps(event, indent=2))

    apiPath = '/weather'
    response = None

    if apiPath == '/weather':
        lat = event['parameters'][0]['value']
        long = event['parameters'][1]['value']

        weather_info = get_weather(lat, long)
        temperature_celsius = convert_kelvin_to_celsius(weather_info['main']['temp'])
        formatted_temperature = "{:.2f}".format(temperature_celsius)
        print("Temperature in Celsius:", formatted_temperature)
        response = {"temperature": formatted_temperature}

    result = {
        'messageVersion': '1.0',
        'response': {
            'actionGroup': event['actionGroup'],
            'apiPath': event['apiPath'],
            'httpMethod': event['httpMethod'],
            'httpStatusCode': 200,
            'responseBody': {
                'application/json': {
                    'body': response
                }
            },
            'sessionAttributes': {},
            'promptSessionAttributes': {}
        }
    }

    print(result)
    return result

def get_weather(lat, long):
    apikey = 'OPEN_WEATHER_API_KEY'
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={apikey}'

    http = urllib3.PoolManager()
    response = http.request('GET', url)
    weather_data = json.loads(response.data.decode('utf-8'))

    return weather_data

def convert_kelvin_to_celsius(kelvin_temp):
    return kelvin_temp - 273.15



{
  "actionGroup": "sampleActionGroup",
  "apiPath": "/weather",
  "httpMethod": "GET",
  "parameters": [
    {
      "value": "-1"
    },
    {
      "value": "0"
    }
  ]
}