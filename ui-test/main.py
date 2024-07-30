import flet as ft





container = ft.Container(
    ft.Column(
        [
            ft.Container(
                ft.Text(
                    "Iniciar Sesión",
                    text_align="center",
                    width=300,
                    size=30,
                    weight="w900",
                    color="white",
                ),
                padding=ft.padding.only(20,20),
                bgcolor="green"
            ),
            ft.Container(
                ft.TextField(
                    width=320,
                    height=40,
                    hint_text="Email",
                    border="underline",
                    color="white",
                    prefix_icon=ft.icons.EMAIL
                ),
                padding=ft.padding.only(1,20)
            ),
            ft.Container(
                ft.TextField(
                    width=320,
                    height=40,
                    hint_text="Contraseña",
                    border="underline",
                    color="white",
                    password=True,
                    prefix_icon=ft.icons.LOCK,
                ),
                padding=ft.padding.only(1,20)
            ),
            ft.Container(
                ft.ElevatedButton(
                    text="INICIAR",
                    width=280,
                    bgcolor="black",
                    color="white"
                ),
                padding=ft.padding.only(20,20),
            ),
            ft.Container(
                ft.Text(
                    "Iniciar sesión con",
                    text_align="center",
                    width=320
                ),
                padding=ft.padding.only(0,20),
            ),
            # ft.Container(
            #     ft.Row(
            #         [
            #             ft.Text("¿No tiene una cuenta?"),
            #             ft.TextButton("Crear cuenta")
            #         ],
            #         alignment=ft.MainAxisAlignment.CENTER
            #     ),
            #     padding=ft.padding.only(0,20)
            # )
            # ft.Container(
            #     ft.Row(
            #         [
            #             ft.IconButton(
            #                 icon=ft.icons.EMAIL, tooltip="Google", icon_size=35
            #             )
            #         ],
            #         alignment=ft.MainAxisAlignment.CENTER
            #     )
            # )
            # ft.Container(
            #     ft.Checkbox(label="Recordar contraseña", check_color="black"),
                
            # )

        ],
        alignment=ft.MainAxisAlignment.CENTER
    ),
    # width=350,
    height="900",
    # alignment=ft.MainAxisAlignment.CENTER,
    
)



def main(page:ft.Page):

    page.vertical_alignment="center",
    page.horizontal_alignment="center"
    page.add(
        container
    )
    

ft.app(main)