import flet as ft
import os.path


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    login_text = ft.Text(value="Login Screen", size=40, weight=ft.FontWeight.BOLD)
    login_subtext = ft.Text(value="Just a convenient look for a log-in screen", size=15)
    email_field = ft.TextField(label='Username or Email', width=300)
    pass_field = ft.TextField(label='Password', width=300, password=True, can_reveal_password=True)
    # email_field = ft.CupertinoTextField(placeholder_text='Username or Email', width=300)
    # pass_field = ft.CupertinoTextField(placeholder_text='Password', width=300)
    login_button = ft.ElevatedButton(text='Enter')

    if os.path.isfile("./bg_image.jpg"):
        bg = ft.Image(
            src="bg_image.jpg",
            fit=ft.ImageFit.COVER,
            expand=True,
            width=page.width,
            height=page.height
        )
        page.bgcolor = ft.colors.ORANGE_50
    else:
        page.bgcolor = ft.colors.BLUE_50

    page.add(
        # Add background image (bg) and overlay it using Flet Stack
        ft.Row(controls=[
            ft.Container(content=ft.Column(controls=[
                login_text,
                login_subtext
            ]), padding=ft.padding.only(right=100)),
            ft.Column(controls=[
                email_field,
                pass_field,
                login_button
            ])
        ],
        alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)