import reflex as rx

# Colores
INK = "#0D0D0D"
PAPER = "#F0EBE1"
GRAPHITE = "#555555"
AMBER = "#C9A96E"
CARBON = "#161616"
GOLD_LIGHT = "#E8D5A3"

# Estado global
class PageState(rx.State):
    email: str = ""
    joined: bool = False
    selected_sizes: dict = {
        "01": "",
        "02": "",
        "03": "",
        "04": "",
    }

    def set_email(self, value: str):
        self.email = value

    def set_size(self, product_id: str, size: str):
        self.selected_sizes = {**self.selected_sizes, product_id: size}

    def join_waitlist(self):
        if self.email:
            self.joined = True


app = rx.App(stylesheets=["styles.css"])