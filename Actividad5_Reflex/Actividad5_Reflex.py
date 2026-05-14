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

# Navbar
def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(
                "CAPSULA",
                font_family="'Cormorant Garamond', serif",
                font_size="1.1rem",
                font_weight="300",
                letter_spacing="0.35em",
                color=PAPER,
            ),
            rx.hstack(
                rx.link("Coleccion", href="#coleccion", color=GRAPHITE, font_size="0.72rem", letter_spacing="0.15em", text_transform="uppercase", _hover={"color": AMBER}),
                rx.link("Nosotros", href="#nosotros", color=GRAPHITE, font_size="0.72rem", letter_spacing="0.15em", text_transform="uppercase", _hover={"color": AMBER}),
                rx.link("Contacto", href="#footer", color=GRAPHITE, font_size="0.72rem", letter_spacing="0.15em", text_transform="uppercase", _hover={"color": AMBER}),
                gap="2.5rem",
            ),
            justify="between",
            align="center",
            width="100%",
            padding="1.5rem 3rem",
        ),
        position="fixed",
        top="0",
        left="0",
        right="0",
        z_index="999",
        background=f"linear-gradient(to bottom, {INK}EE 0%, {INK}00 100%)",
    )


# Hero
def hero() -> rx.Component:
    titulo = "CAPSULA"
    letras = [
        rx.el.span(
            letra,
            class_name="hero-letter",
            style={"animation_delay": f"{0.05 + i * 0.07}s"},
        )
        for i, letra in enumerate(titulo)
    ]

    return rx.box(
        rx.vstack(
            rx.text(
                "Edicion N. 001",
                font_size="0.7rem",
                letter_spacing="0.5em",
                color=AMBER,
                text_transform="uppercase",
                margin_bottom="1.5rem",
            ),
            rx.heading(
                *letras,
                class_name="hero-title",
                font_family="'Cormorant Garamond', serif",
                font_weight="300",
                font_size=["3rem", "5rem", "8rem"],
                letter_spacing="0.25em",
                color=PAPER,
                line_height="1",
            ),
            rx.box(
                background=AMBER,
                height="1px",
                width="60px",
                margin_y="2rem",
            ),
            rx.text(
                "Diez piezas. Ninguna igual.",
                font_family="'Cormorant Garamond', serif",
                font_size="1.3rem",
                font_weight="300",
                color=GRAPHITE,
                letter_spacing="0.1em",
                font_style="italic",
            ),
            rx.box(height="2.5rem"),
            rx.link(
                rx.button(
                    "Ver la coleccion",
                    background="transparent",
                    color=AMBER,
                    border=f"1px solid {AMBER}",
                    font_size="0.72rem",
                    letter_spacing="0.2em",
                    text_transform="uppercase",
                    padding="1rem 3rem",
                    border_radius="0",
                    _hover={"background": AMBER, "color": INK},
                    cursor="pointer",
                    transition="all 0.3s ease",
                ),
                href="#coleccion",
            ),
            align="center",
            justify="center",
            width="100%",
            min_height="100vh",
            padding="2rem",
        ),
        width="100%",
        background=f"radial-gradient(ellipse at 50% 40%, {AMBER}12 0%, {INK} 60%)",
        id="inicio",
    )


# Pagina principal (temporal hasta el commit 5)
@rx.page(route="/", title="Capsula - Edicion N.001")
def index() -> rx.Component:
    return rx.box(
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(
            rel="stylesheet",
            href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=DM+Sans:wght@300;400;500&display=swap",
        ),
        navbar(),
        hero(),
        background=INK,
        min_height="100vh",
        font_family="'DM Sans', sans-serif",
        color=PAPER,
    )

app = rx.App(stylesheets=["styles.css"])