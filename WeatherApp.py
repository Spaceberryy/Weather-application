# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QLabel
import requests

# Important:
# You need to run the following command to generate the Weather_form.py file
#     pyside6-uic Weather_form.ui -o Weather_form.py, or
#     pyside2-uic Weather_form.ui -o Weather_form.py
from Weather_form import Ui_Weather_form

class WeatherApp(QWidget, Ui_Weather_form ):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Weather_form()
        self.ui.setupUi(self)

        self.ui.pb_getweather.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "bd4265d53bc82bebbe5b53d71b912f30"
        city = self.ui.city_name.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request:\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API key")
                case 403:
                    self.display_error("Forbidden:\nAccess is denied")
                case 404:
                    self.display_error("Not found:\nCity not found")
                case 500:
                    self.display_error("Internal server error:\nPlease try again later")
                case 502:
                    self.display_error("Bad gateway:\nInvalid response from the server")
                case 503:
                    self.display_error("Service unavailable:\nServer is down")
                case 504:
                    self.display_error("Gateway timeout:\nNo response from server")
                case _:
                    self.display_error(f"HTTP error occurred:\n{http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("TOo many redirects:\nCheck the the URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request error:\n{req_error}")

    def display_error(self, message):
        self.ui.feels_like.setText(message)
        self.ui.emoji_label.clear()
        self.ui.temp_val.clear()
        self.ui.feels_like.clear()

    def display_weather(self, data):
        temperature_K = data["main"]["temp"]
        temperature_C = int(temperature_K - 273.15)
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]

        print(data)

        self.ui.temp_val.setText(f"{temperature_C}°")
        self.ui.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.ui.feels_like.setText(weather_description)

    @staticmethod
    def get_weather_emoji(weather_id):

        if 200 <= weather_id <= 232:
            return "🌦"
        elif 300 <= weather_id <= 321:
            return "🌥"
        elif 500 <= weather_id <= 531:
            return "🌧"
        elif 600 <= weather_id <= 622:
            return "❄"
        elif 700 <= weather_id <= 741:
            return "🌫"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪"
        elif weather_id > 800:
            return "☁"
        else:
            return ""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Weather_form = WeatherApp()
    app.setStyle('fusion')
    Weather_form.show()
    sys.exit(app.exec())
