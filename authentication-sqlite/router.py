import flet as ft

from pages.authentication.login import Login
from pages.authentication.signup import SignUp

from utils.colors import customBgColor

def views_handler(page):
    return {
        "/login":ft.View(route="/login",bgcolor=customBgColor, controls=[Login(page)]),
        "/signup":ft.View(route="/signup", controls=[SignUp(page)]),
    }