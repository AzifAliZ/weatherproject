##🌤️ SkyForecast — Weather Forecast Website

A simple and elegant weather forecasting website built using **Django** and the **Open-Meteo API**.
It shows real-time weather conditions like temperature, humidity, windspeed, rain, UV index, sunrise/sunset, and more.
The app also displays dynamic weather backgrounds based on weather codes.

---

## 🚀 Features

* 🌍 Search weather by city name
* 📍 Automatic latitude & longitude detection using Open-Meteo Geocoding API
* 🌡️ Shows current temperature
* 🌫️ Humidity, cloud cover, windspeed
* 🌧️ Precipitation & pressure
* 🌅 Sunrise & sunset time
* 🔆 UV index (current & max)
* 🎨 Dynamic weather background images based on weather conditions
* ❄️ Supports rain, snow, thunderstorm, fog, clear sky, and more
* 💎 Glass-effect UI card (beautiful design)

---

## 🛠️ Tech Stack

* **Backend:** Django
* **Frontend:** HTML, CSS
* **API:** Open-Meteo Free Weather API
* **Icons/Images:** Custom weather icons (based on weather codes)

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/SkyForecast.git
cd SkyForecast
```

### 2️⃣ Create a virtual environment

```bash
python -m venv env
```

Activate:

**Windows:**

```bash
env\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Django server

```bash
python manage.py runserver
```

Now open in browser:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🌦️ Weather Image Mapping

Each weather code automatically loads a related background:

| Code | Condition                  | Image                          |
| ---- | -------------------------- | ------------------------------ |
| 0    | Clear sky                  | `clear_sky.jpg`                |
| 1    | Mainly clear               | `mainly_clear.jpg`             |
| 2    | Partly cloudy              | `partly_cloudy.jpg`            |
| 3    | Overcast                   | `overcast.jpg`                 |
| 45   | Fog                        | `fog.jpg`                      |
| 48   | Depositing rime fog        | `rime_fog.jpg`                 |
| 51   | Light drizzle              | `light_drizzle.jpg`            |
| 53   | Moderate drizzle           | `moderate_drizzle.jpg`         |
| 55   | Dense drizzle              | `dense_drizzle.jpg`            |
| 61   | Slight rain                | `slight_rain.jpg`              |
| 63   | Moderate rain              | `moderate_rain.jpg`            |
| 65   | Heavy rain                 | `heavy_rain.jpg`               |
| 71   | Slight snow                | `slight_snow.jpg`              |
| 73   | Moderate snow              | `moderate_snow.jpg`            |
| 75   | Heavy snow                 | `heavy_snow.jpg`               |
| 80   | Rain showers               | `rain_showers.jpg`             |
| 81   | Heavy rain showers         | `heavy_rain_showers.jpg`       |
| 82   | Violent rain showers       | `violent_rain_showers.jpg`     |
| 95   | Thunderstorm               | `thunderstorm.jpg`             |
| 96   | Thunderstorm + hail        | `thunderstorm_hail.jpg`        |
| 99   | Severe thunderstorm + hail | `severe_thunderstorm_hail.jpg` |

Put all images here:

```
weatherapp/static/weather_images/
```

---

## 📁 Project Structure

```
SkyForecast/
│
├── weatherapp/
│   ├── templates/
│   │   └── weather.html
│   ├── static/
│   │   └── weather_images/
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│
├── weatherproject/
│   ├── settings.py
│   ├── urls.py
│
├── README.md
└── manage.py
```

---

## 🧪 API Used

### **Open-Meteo Free Weather API**

No API key needed.
Docs: [https://open-meteo.com/](https://open-meteo.com/)

---

## 📝 License

This project is open-source and free to use under the MIT License.

---

## 💙 Author

**Azif Ali**
🔗 GitHub: [https://github.com/YOUR_USERNAME](https://github.com/AzifAliZ)
🌟 If you like this project, please star the repo!

---

If you want, I can also create a **requirements.txt**, **LICENSE**, or a more detailed README with screenshots.
