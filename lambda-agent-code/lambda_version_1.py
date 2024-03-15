# This is lambda function code for the weather API. This code is written in Python 3.8.
# It is version 1 of the lambda function. The code is used to get the weather and other related information for a given latitude and longitude.
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
        print(weather_info)
        response = weather_info
        print(response)

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

    print(url)

    http = urllib3.PoolManager()
    response = http.request('GET', url)
    weather_data = json.loads(response.data.decode('utf-8'))

    print(weather_data)
    return weather_data

    print(url)

    http = urllib3.PoolManager()
    response = http.request('GET', url)
    weather_data = json.loads(response.data.decode('utf-8'))

    print(weather_data)
    return weather_data

