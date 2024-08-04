import flet as ft

class  Login(ft.Container):
    def __init__(self, page:ft.Page):
        super().__init__()

        self.content = ft.Column(
            controls=[
                print("Login"),
                ft.Text("Hello, Login section", color="white"),
                print("Sin boton"),
                ft.ElevatedButton(text="signup", on_click= lambda e: page.go("/signup"))
            ]
        )