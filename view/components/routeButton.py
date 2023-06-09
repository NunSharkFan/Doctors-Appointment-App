import flet as ft
from typing import Callable

def get_route_button(page:ft.Page, buttonName: str, route: str) -> ft.Container:
    return ft.Container(content = ft.Row([ft.Text(value = buttonName,
                                                  expand = True),
                                          ft.Icon(name = ft.icons.ARROW_FORWARD_IOS_SHARP,
                                                  visible = True if page.route == route else False)]),
                        on_click = lambda _: page.go(route),
                        disabled = True if page.route == route else False)