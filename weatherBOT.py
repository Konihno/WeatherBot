import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        weather_description = weather["description"]
        
        weather_info = (f"Temperature: {temperature}°C\n"
                        f"Pressure: {pressure} hPa\n"
                        f"Humidity: {humidity}%\n"
                        f"Description: {weather_description}")
    else:
        weather_info = "City Not Found!"
    
    return weather_info

def main():
    api_key = ""  
    city = input("Enter city name: ")
    weather_info = get_weather(city, api_key)
    print(weather_info)

if __name__ == "__main__":
    main()