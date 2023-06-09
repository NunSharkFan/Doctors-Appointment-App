import flet as ft
from view.components.sideBar import get_side_bar
def get_menu_view(page: ft.Page, view: ft.View) -> ft.View:
    view.controls = [ft.ResponsiveRow(controls = [get_side_bar(page)])]
    return view