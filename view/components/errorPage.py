import flet as ft

def get_error_page(view: ft.View) -> ft.View:
    view.controls = [ft.Text(f'Page Error: Page Not Found!', color = ft.colors.RED_700, size = 30),
                     ft.TextButton("Click Here To Return")]
    
    return view