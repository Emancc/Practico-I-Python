from flask import Flask, render_template, request
import requests


app = Flask(__name__)

ciudades = {
    "Río Cuarto": {"lat": -33.1333, "lon": -64.3500},
    "Mendoza" : {"lat": -32.8833, "lon": -68.8167},
    "Santa Fe" : {"lat": -31.6333, "lon": -60.7000},
    "Buenos Aires": {"lat": -34.6037, "lon": -58.3816},
    "Córdoba": {"lat": -31.4201, "lon": -64.1888},
    "Madrid": {"lat": 40.4168, "lon": -3.7038},
    "Nueva York": {"lat": 40.7128, "lon": -74.0060},
    "Tokio": {"lat": 35.6895, "lon": 139.6917},
    "París": {"lat": 48.8566, "lon": 2.3522},
    "Londres": {"lat": 51.5074, "lon": -0.1278},
    "Sídney": {"lat": -33.8688, "lon": 151.2093},
    "Ciudad de México": {"lat": 19.4326, "lon": -99.1332},
    "El Cairo": {"lat": 30.0444, "lon": 31.2357}
}

@app.route('/')
def index():
    return render_template('index.html', ciudades=ciudades)

@app.route('/clima')
def clima():
    nombre = request.args.get('ciudad')
    latitud = ciudades[nombre]["lat"]
    longitud = ciudades[nombre]["lon"]

    url_clima = f'https://api.open-meteo.com/v1/forecast?latitude={latitud}&longitude={longitud}&current_weather=true'

    weather_codes = {
        0: "Despejado",
        1: "Mayormente despejado",
        2: "Parcialmente nublado",
        3: "Nublado",
        45: "Niebla",
        48: "Niebla densa",
        51: "Llovizna ligera",
        53: "Llovizna moderada",
        55: "Llovizna fuerte",
        56: "Llovizna helada ligera",
        57: "Llovizna helada densa",
        61: "Lluvia ligera",
        63: "Lluvia moderada",
        65: "Lluvia fuerte",
        66: "Lluvia helada ligera",
        67: "Lluvia helada fuerte",
        71: "Nieve ligera",
        73: "Nieve moderada",
        75: "Nieve fuerte",
        77: "Graupel",
        80: "Chubascos de lluvia ligeros",
        81: "Chubascos de lluvia moderados",
        82: "Chubascos de lluvia fuertes",
        85: "Chubascos de nieve ligeros",
        86: "Chubascos de nieve fuertes",
        95: "Tormenta eléctrica",
        96: "Tormenta eléctrica con granizo ligero",
        99: "Tormenta eléctrica con granizo fuerte",
    }
    descripcion_clima = weather_codes.get(requests.get(url_clima).json()["current_weather"].get("weathercode"), "Información no disponible")

    return render_template("clima.html",
            ciudad=nombre,
            temperatura=requests.get(url_clima).json()["current_weather"].get("temperature"),
            velocidad_viento=requests.get(url_clima).json()["current_weather"].get("windspeed"),
            descripcion_clima=descripcion_clima)



if __name__ == '__main__':
    app.run()