import tkinter as tk
import requests
import json

# Define GUI class
class WeatherApp:

    def __init__(self, master):

        self.master = master
        self.master.title('Weather App')

        self.city_label = tk.Label(self.master, text='City:')
        self.city_label.grid(row=0, column=0)

        self.city_entry = tk.Entry(self.master)
        self.city_entry.grid(row=0, column=1)

        self.get_weather_button = tk.Button(self.master, text='Get Weather', command=self.get_weather)
        self.get_weather_button.grid(row=1, column=0, columnspan=2)

        self.weather_label = tk.Label(self.master, text='')
        self.weather_label.grid(row=2, column=0, columnspan=2)

    def get_weather(self):

        city = self.city_entry.get()
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric'

        response = requests.get(url)
        weather_data = json.loads(response.text)

        if weather_data['cod'] == '404':
            self.weather_label.config(text='City not found.')
        else:
            temp = weather_data['main']['temp']
            feels_like = weather_data['main']['feels_like']
            description = weather_data['weather'][0]['description']
            self.weather_label.config(text=f'Temperature: {temp}°C\nFeels like: {feels_like}°C\nDescription: {description}')

# Run GUI app
root = tk.Tk()
app = WeatherApp(root)
root.mainloop()
