import requests
from django.shortcuts import render

def weather_view(request):
    city = request.GET.get("city", "Kochi")

    # STEP 1: Get latitude & longitude
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_data = requests.get(geo_url).json()

    if "results" not in geo_data:
        return render(request, "weather.html", {"error": "City not found"})

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]
    country = geo_data["results"][0]["country"]

    # STEP 2: Get weather data
    weather_url = (
        "https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        "&current_weather=true"
        "&hourly=temperature_2m,relativehumidity_2m,precipitation,"
        "cloudcover,pressure_msl,uv_index,windspeed_10m"
        "&daily=weathercode,temperature_2m_max,temperature_2m_min,"
        "sunrise,sunset,uv_index_max"
        "&timezone=auto"
    )
    weather_data = requests.get(weather_url).json()

    # CURRENT WEATHER
    current = weather_data["current_weather"]

    # HOURLY
    hourly = weather_data["hourly"]

    # DAILY
    daily = weather_data["daily"]

    # Weathercode → Text
    weather_code_map = {
        0: "Clear sky ☀️",
        1: "Mainly clear 🌤️",
        2: "Partly cloudy 🌤",
        3: "Overcast ☁️",
        45: "Fog 🌫️",
        48: "Depositing Rime Fog ❄️🌫️",
        51: "Light drizzle 🌦️",
        53: "Moderate drizzle 🌧️",
        55: "Dense drizzle 🌧",
        61: "Slight rain 🌧️",
        63: "Moderate rain 🌧️🌧️",
        65: "Heavy rain 🌧️🌧️🌧️",
        71: "Slight snow ❄️",
        73: "Moderate snow ❄️❄️",
        75: "Heavy snow ❄️❄️❄️",
        80: "Rain showers 🌧️",
        81: "Heavy rain showers 🌧️🌧️",
        82: "Violent rain showers ⛈️",
        95: "Thunderstorm ⛈️",
        96: "Thunderstorm with hail ⛈️❄️",
        99: "Severe thunderstorm + hail 🌀⚡",
    }

    # Weathercode → Background image filename
    weather_bg = {
        0: "weather/clear_sky.png",
        1: "weather/mainly_clear.png",
        2: "weather/partly_cloudy.png",
        3: "weather/overcast.png",

        45: "weather/fog.png",
        48: "weather/rime_fog.png",

        51: "weather/light_drizzle.png",
        53: "weather/moderate_drizzle.png",
        55: "weather/dense_drizzle.png",

        61: "weather/slight_rain.png",
        63: "weather/moderate_rain.png",
        65: "weather/heavy_rain.png",

        71: "weather/slight_snow.png",
        73: "weather/moderate_snow.png",
        75: "weather/heavy_snow.png",

        80: "weather/rain_showers.png",
        81: "weather/heavy_rain_showers.png",
        82: "weather/violent_rain_showers.png",

        95: "weather/thunderstorm.png",
        96: "weather/thunderstorm_hail.png",
        99: "weather/severe_thunderstorm_hail.png",
    }

    # Get text + background
    weather_description = weather_code_map.get(current["weathercode"], "Unknown")
    bg_image = weather_bg.get(current["weathercode"], "weather/default.png")

    context = {
        "city": city,
        "country": country,

        # CURRENT
        "temperature": current["temperature"],
        "windspeed": current["windspeed"],
        "weathercode": current["weathercode"],
        "weather_text": weather_description,
        "bg_image": bg_image,

        # HOURLY
        "humidity": hourly["relativehumidity_2m"][0],
        "precipitation": hourly["precipitation"][0],
        "cloudcover": hourly["cloudcover"][0],
        "pressure": hourly["pressure_msl"][0],
        "uv_index": hourly["uv_index"][0],

        # DAILY
        "temp_max": daily["temperature_2m_max"][0],
        "temp_min": daily["temperature_2m_min"][0],
        "sunrise": daily["sunrise"][0],
        "sunset": daily["sunset"][0],
        "uv_index_max": daily["uv_index_max"][0],
    }

    return render(request, "weather.html", context)
