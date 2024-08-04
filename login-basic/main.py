import flet as ft
from flet import TextField, Checkbox, ElevatedButton, Text, Row, Column
from flet_core.control_event import ControlEvent

def main(page:ft.Page):
    page.page="Signup"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.theme_mode=ft.ThemeMode.LIGHT
    page.window.width=380
    page.window.height=720
    page.window_resizable=False

    text_username = TextField(label="Username", text_align=ft.TextAlign.LEFT, width=200)
    text_password = TextField(label="Password", text_align=ft.TextAlign.LEFT, width=200, password=True)
    checkbox_signup = Checkbox(label="I agree to stuff", value=False)
    btn_submit = ElevatedButton(text="Sign Up", width=200, disabled=True)
     
    #  new
    def validate(e: ControlEvent) -> None:
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            btn_submit.disabled = False
        else:
            btn_submit.disabled = True

        page.update()

    def submit(e: ControlEvent) -> None:
        print("Username: ", text_username.value)
        print("Password: ", text_password.value)

        page.clean()
        page.add(
            Row(
                controls=[
                    Text(
                        value=f"Welcome: {text_username.value}",
                        size=20
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        )
    
    # control Event 
    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    btn_submit.on_click = submit

    # render page signup
    page.add(
        Row(
            controls=[
                Column(
                    [text_username,
                     text_password,
                     checkbox_signup,
                     btn_submit]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

if __name__ == "__main__":
    ft.app(main)