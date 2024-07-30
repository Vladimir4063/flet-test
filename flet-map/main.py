import flet as ft
import flet.map as map


def main(page: ft.Page):
    # page.window.always_on_top = True

    def handle_tap(e: map.MapTapEvent):
        print(
            f"{e.local_x}, {e.local_y}, {e.global_x}, {e.global_y}"
            "___"
            f"{e.coordinates}"
        )

    page.add(
        map.Map(
            expand=True,
            configuration=map.MapConfiguration(
                on_init=lambda e: print("Map Init"), on_tap=handle_tap
            ),
            layers=[
                map.TileLayer(
                    url_template="https://tile.openstreetmap.org/{z}/-37.129257066810155/-56.89651960321249.png"
                )
            ],
        )
    )


ft.app(main)
