import flet as ft
from view.loginView import get_login_view
from view.menuView import get_menu_view
from view.components.errorPage import get_error_page
def main(page: ft.Page):
    page.title = "Temp App Title"

    views: list[ft.View] = [get_login_view(page, ft.View(route = "/login")),
                            get_menu_view(page, ft.View(route = "/menu"))]

    def change_route(route):
        page.views.clear()

        viewsTuple = tuple(filter(lambda l: l.route == page.route, views))
        currentView = viewsTuple[0] if len(viewsTuple) > 0 else get_error_page(ft.View(route = "/enk2"))
        page.views.append(currentView)
        page.go(currentView.route)

    page.on_route_change = change_route
    page.go("/login")