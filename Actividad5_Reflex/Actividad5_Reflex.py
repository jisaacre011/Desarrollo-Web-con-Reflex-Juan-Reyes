import reflex as rx

def index() -> rx.Component:
    return rx.container(
        rx.text("Landing Page", font_size="2em"),
        padding="2em"
    )

app = rx.App()
app.add_page(index)