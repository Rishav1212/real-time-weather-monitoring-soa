from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "5c3d17fae85199faffda8c73d24f3df9"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city'].strip().title()  # Clean and format input
        if city:
            params = {
                'q': city,
                'appid': API_KEY,
                'units': 'metric'
            }
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                try:
                    # Extract more detailed error message from API
                    weather_data = {'error': response.json().get('message', 'City not found.')}
                except Exception:
                    weather_data = {'error': 'City not found or API error.'}
        else:
            weather_data = {'error': 'Please enter a valid city name.'}
    return render_template('weather.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
