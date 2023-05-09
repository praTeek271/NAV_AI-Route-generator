class Api_Data:

    def __init__(self, coodinate):
        self.co = coodinate
    

    def air_index(self):

        import requests
        ENDPOINT = 'https://api.openaq.org/v1/latest'
        parameters = {
            'coordinates': f'{self.co}', # Example coordinates for San Francisco
            'radius': '10000', # Search radius in meters
            'parameter': 'pm25', # Pollutant of interest
        }
        self.resp_air_index = requests.get(ENDPOINT, params=parameters)

        # Extract the air quality index from the API response
        data = response.json()['results'][0]['measurements'][0]['value']
        unit = response.json()['results'][0]['measurements'][0]['unit']
        return(f'The air quality index is {data} {unit}')

    def is_holiday(self):
        import requests
        import datetime
        # find year
        year = datetime.datetime.now().year
        ENDPOINT = 'https://calendarific.com/api/v2/holidays'
        parameters = {
            'api_key': '2e72745fd6562bd393296f14baacf18f92b08b3a',
            'country': 'US',
            'year': year,
        }

        self.resp_is_holiday = requests.get(ENDPOINT, params=parameters)

        holidays = response.json()['response']['holidays']
        # currrent date
        today = datetime.datetime.now().strftime('%Y-%m-%d')
        for holiday in holidays:
            name = holiday['name']
            date = holiday['date']['iso']
            if date == today:
                return True
        return False
    
    def is_weekend(self):

        import datetime
        today = datetime.datetime.now().strftime('%A')
        if today == 'Saturday' or today == 'Sunday':
            return True
        return False

    def wind_direction(self):
        import requests

        # Define the endpoint and parameters for the OpenWeatherMap API
        ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'
        parameters = {
            'lat': self.co[0],
            'lon': self.co[1],
            'appid': '0794673555559a129540662e3029b866',
        }

        # Make a request to the OpenWeatherMap API with your API key and parameters
        response = requests.get(ENDPOINT, params=parameters)

        # Extract the wind direction from the API response
        wind_direction = response.json()['wind']['deg']
        
        # Convert wind direction to cardinal direction
        directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]
        index = round(wind_direction / (360. / len(directions)))
        return (directions[index % len(directions)])

    def temperature(self):  

        import requests
        ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'
        parameters = {
            'lat': lat,
            'lon': lon,
            'appid': '0794673555559a129540662e3029b866',
            'units': 'metric',
        }

        # Make a request to the OpenWeatherMap API with your API key and parameters
        response = requests.get(ENDPOINT, params=parameters)

        # Extract the temperature from the API response
        temperature = response.json()['main']['temp']
        return temperature

    def humidity(self):
        ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'
        parameters = {
            'lat': self.co[0],
            'lon': self.co[1],
            'appid': '0794673555559a129540662e3029b866',
            'units': 'metric',
        }

        # Make a request to the OpenWeatherMap API with your API key and parameters
        response = requests.get(ENDPOINT, params=parameters)

        # Extract the humidity from the API response
        humidity = response.json()['main']['humidity']
        return humidity