import flet as ft
import requests
import geocoder

def send_location():
    # Obtener la ubicación actual
    g = geocoder.ip("me")
    print("IP################")
    location = g.latlng
    print(g)
    # Enviar la ubicación al backend
    response = requests.post("http://tu-backend-url.com/location", json={"location": location})
    if response.status_code == 200:
        print("Ubicación enviada exitosamente")
    else:
        print("Error al enviar la ubicación")

def main(page):
    page.title = "Envío de Ubicación en Tiempo Real"
    
    btn_send_location = ft.ElevatedButton(text="Enviar Ubicación", on_click=lambda _: send_location())
    
    page.add(btn_send_location)

ft.app(target=main)
