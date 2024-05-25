from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.backdrop.backdrop import MDCard

import config
from config import APY_KEY, API_URL
import requests as req


class WeatherCard(MDCard):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class MainScreen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def weather_search(self):
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
        self.ids.weather_card.ids.label.text = descripition#Звертаємось до карточки і переіменовуємо текст


class WeatherApp(MDApp):
    def build(self):
        Builder.load_file('style.kv')
        self.theme_cls.theme_style = 'Dark'
        self.screen = MainScreen('main_screen')
        return self.screen


WeatherApp().run()