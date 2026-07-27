from weather_api import get_weather
def display_weather(data):
    city= data["name"]
    temp= data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    wind = data["wind"]["speed"]
    print(f"\nWeather in {city}")
    print(f"Temperature: {temp}°C (feels like {feels_like}°C)")
    print(f"Condition: {description}")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {wind} m/s")

city = input("Enter city: ")
data = get_weather(city)
if data:
    display_weather(data)
else:
    print("City not found or something went wrong.")



#venv\Scripts\activate