from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.backdrop.backdrop import MDCard

import config
from config import APY_KEY, API_URL
import requests as req


class WeatherCard(MDCard):

        def __init__(self, descripition, icon, temp, rain, wind, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.ids.desc_text.text = descripition
            self.ids.temp_text.text = f'{temp}°C'
            self.ids.rain_text.text = f'Йморівність опадів: {rain * 100}%'
            self.ids.wind_text.text = f'Швидкість вітру: {wind} м/с'
            self.ids.weather_icon.source = f"https://openweathermap.org/img/wn/{icon}@2x.png"



class MainScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def weather_search(self):
        self.ids.weather_carousel.clear_widgets()
        #Отримуємо текст з кествого поля міста
        city = self.ids.text_fell.text.strip().lower()
        #Робимо налажтування
        api_params = {
            'q': city,
            'appid': APY_KEY

        }

        #Робимо запит і получаємо відповідь
        data = req.get(API_URL, api_params)
        response = data.json()
        print(response)
        descripition = response['weather'][0]['description']
        icon = response['weather'][0]['icon']
        temp = response['main']['temp']

        if 'rain' in response:
            rain = response['rain']['1h']
        else:
            rain = 0
        wind = response['wind']['speed']
        new_card = WeatherCard(descripition, icon, temp, rain, wind)
        self.ids.weather_carousel.add_widget(new_card)

class WeatherApp(MDApp):
    def build(self):
        Builder.load_file('style.kv')
        self.theme_cls.theme_style = 'Dark'
        self.screen = MainScreen('main_screen')
        return self.screen


WeatherApp().run()