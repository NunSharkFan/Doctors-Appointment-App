import flet as ft
from view.components.routeButton import get_route_button

def get_side_bar(page: ft.Page) -> ft.Column:
    sidebar = ft.Column(controls=[ft.Image(),
                                  ft.Column(controls = [get_route_button(page = page,
                                                                         buttonName = "Appointments",
                                                                         route = "/appointments")]),
                                  ft.Row()],
                        alignment = ft.MainAxisAlignment.SPACE_BETWEEN)
    return sidebar