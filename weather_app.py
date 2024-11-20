# Weather App - A Simple Python Project to Fetch Real-Time Weather Data
# By Michael Morales

import requests
import json

# Function to fetch weather data from the OpenWeatherMap API
def get_weather(city, api_key):
    """
    Fetch the weather data for a given city using OpenWeatherMap API.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric',  # Temperature in Celsius
        'lang': 'en'  # Language in English
    }
    
    try:
        # Make the API request
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Check if the request was successful
        
        # Parse the JSON data
        data = response.json()

        if data['cod'] == 200:
            # Extracting relevant information from the response
            city_name = data['name']
            weather_desc = data['weather'][0]['description']
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            # Printing the weather data in a user-friendly format
            print(f"\nWeather Information for {city_name}:")
            print(f"Description: {weather_desc.capitalize()}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print("Error: Could not retrieve data for the city. Please try again.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Main function to run the weather app
def run_weather_app():
    """
    Main function to run the weather application.
    """
    print("Welcome to the Weather App!")
    
    # Ask the user for a city name
    city = input("Enter the city name: ").strip()
    
    # OpenWeatherMap API key (replace with your own API key)
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key

    # Fetch and display the weather data for the entered city
    get_weather(city, api_key)

# Run the app
if __name__ == "__main__":
    run_weather_app()
