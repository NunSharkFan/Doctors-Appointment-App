import flet as ft

def get_login_view(page: ft.Page, view: ft.View) -> ft.View:
    usernameField = ft.TextField(label = "Username",
                                 prefix_icon = ft.icons.PERSON_2_OUTLINED,
                                 width = page.width/2)
    passwordField = ft.TextField(label = "Password",
                                 prefix_icon = ft.icons.PASSWORD_OUTLINED,
                                 width = page.width/2,
                                 password = True,
                                 can_reveal_password = True)
    
    def updateFields(_):
        usernameField.width = page.width/2
        passwordField.width = page.width/2
        page.update()
    def verify(_):
        if usernameField.value == "Leaf" and passwordField.value == "Void":
            usernameField.value = ""
            passwordField.value = ""
            page.go("/menu")
        else:
            passwordField.value = ""
            page.snack_bar = ft.SnackBar(ft.Text("EYJAFJALLA", color = "#ff0000"), bgcolor = "#ffcccb")
            page.snack_bar.open = True
        page.update()

    view.vertical_alignment = ft.MainAxisAlignment.CENTER
    view.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    view.controls = [usernameField,
                     passwordField,
                     ft.TextButton("Log In",
                                   on_click = verify)]
    
    page.on_resize = updateFields
    return view