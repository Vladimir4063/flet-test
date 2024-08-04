import flet as ft
from router import views_handler

def main(page:ft.Page):
    print("Hola")
    def route_change(route):
        page.views.clear()
        page.views.append(views_handler(page)[page.route])

    page.on_route_change = route_change
    print("Hola2")
    page.go("/login", skip_route_change_event=False)
    print("Hola3")

ft.app(target=main, assets_dir="assets")
