from urllib import response
import requests

# Enter your OpenWeather API key
api_key = "<your_api_key>"

# Enter City name 
city = input('Enter City Name')

# URL for the OpenWeatherMap API
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# make the API call anf get the responce 
response = requests.get(url)

#check if the request was sucsessful 
if response.status_code == 200:
    #convert the respomce to a dictionary 
    weather_data = response.json

    #Extract the relevant information from the dictionary
    temperature = weather_data["main"]["temp"]
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"]

    #Print the current weather conditions 
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Description: {description}")

else:

   # print an error message    

    print("Error: Could not recieve weather data.")
    