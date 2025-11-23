import requests
from datetime import datetime
from zoneinfo import ZoneInfo

def planos_atividade(latitude, longitude, date):
    url= 'https://api.sunrise-sunset.org/json'
    parametros = {
        "lat": latitude,
        "lng": longitude,
        "date": date,  
        "formatted": 0
    }
    
    data= requests.get(url, params=parametros).json()
    resultado =data["results"]

    tz = ZoneInfo("America/Sao_Paulo")
    sunrise = datetime.fromisoformat(resultado["sunrise"]).astimezone(tz)
    sunset = datetime.fromisoformat(resultado["sunset"]).astimezone(tz)

    sunrise_str = sunrise.strftime("%I:%M:%S %p").lstrip("0")
    sunset_str = sunset.strftime("%I:%M:%S %p").lstrip("0")
    sunrise_short = sunrise.strftime("%I:%M %p").lstrip("0")
    sunset_short = sunset.strftime("%I:%M %p").lstrip("0")

    atividades=[
        f"Meditação ao nascer do sol ás {sunrise_short} ",
        "Visitar uma cachoeira",
        f"Gravar vídeos do pôr do sol ás {sunset_short} ",
        "Ouvir música contemplando o céu",
    ]

    return{
        "Sunrise": sunrise_str,
        "Sunset": sunset_str,
        "atividades": atividades
    }


resultado=planos_atividade(-22.9068, -43.1729, "2003-12-21")
print("Saída igual o documento: ")
print(resultado)

print()

print("Saída separada em linhas:")
print(f"Sunrise: {resultado['Sunrise']}")
print(f"Sunset: {resultado['Sunset']}")
print("Atividades:")
for atividade in resultado["atividades"]:
    print(f" {atividade}")