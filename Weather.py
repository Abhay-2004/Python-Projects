import requests,json

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

URL = BASE_URL +"q=" + 'Bangalore' + "&appid=" + '9df487c92ff9ea0c4368b9b77c40e25c'

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()

    main = data['main']

    temperature = main['temp'] - 273.15

    humidity = main['humidity']

    pressure = main['pressure']

    report = data['weather']

    print(f"Temperature: {temperature}")
    print(f"Weather Report: {report[0]['description']}")
    print(f"Pressure: {pressure}")
    print(f"Humidity: {humidity}")

else:
    print("Error Occured")
