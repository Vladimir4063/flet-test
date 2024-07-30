import flet as ft

from flet import View, Page, AppBar, ElevatedButton, Text
from flet import RouteChangeEvent, ViewPopEvent, CrossAxisAlignment, MainAxisAlignment

def main(page:Page)-> None:
    page.title = "My store"

    def route_change(e: RouteChangeEvent)-> None:
        page.views.clear()
        
        page.views.append(
            View(
                route="/",
                controls=[
                    AppBar(title=Text('Home'), bgcolor='blue'),
                    Text(value='Home', size=30),
                    ElevatedButton(text="Go to store", on_click=lambda _: page.go("/store")),
                    ElevatedButton(text="Go to Info", on_click=lambda _: page.go("/info"))
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=MainAxisAlignment.CENTER,
                spacing=26
            )
        )
        # Store
        if page.route == '/store':
            page.views.append(
                View(
                    route="/store",
                    controls=[
                        AppBar(title=Text('Store'), bgcolor='green'),
                        Text(value='Store', size=30),
                        ElevatedButton(text="Go back",on_click=lambda _: page.go("/"))
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=MainAxisAlignment.CENTER,
                    spacing=26
                )
            )
        if page.route == "/info":
            page.views.append(
                View(
                    route="/info",
                    controls=[
                        AppBar(title=Text("Infoooo"), bgcolor="orange"),
                        Text(value=" Llegaste a la info de la App", size=30),
                        ElevatedButton(text="Go back", on_click=lambda _: page.go("/"))
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=MainAxisAlignment.CENTER,
                    spacing=26
                )
            )



        page.update()
    
    def view_pop(e: ViewPopEvent) -> None:
        page.views.pop()
        top_view: View = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(main)