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


# Separador de seccion
def section_divider(label: str) -> rx.Component:
    return rx.hstack(
        rx.box(flex="1", height="1px", background=GRAPHITE, opacity="0.3"),
        rx.text(
            label,
            font_size="0.65rem",
            letter_spacing="0.4em",
            color=GRAPHITE,
            text_transform="uppercase",
            padding_x="2rem",
            white_space="nowrap",
        ),
        rx.box(flex="1", height="1px", background=GRAPHITE, opacity="0.3"),
        align="center",
        width="100%",
        padding_x="3rem",
        padding_y="4rem",
    )


# Card de producto horizontal
def product_card(
    product_id: str,
    name: str,
    subtitle: str,
    price: str,
    image_url: str,
    reverse: bool = False,
) -> rx.Component:
    sizes = ["XS", "S", "M", "L", "XL"]

    image_side = rx.box(
        style={
            "background_image": f"url('{image_url}')",
            "background_size": "cover",
            "background_position": "center",
            "min_height": "520px",
            "flex": "1",
        },
    )

    details_side = rx.vstack(
        rx.text(
            f"N. {product_id}",
            font_size="0.65rem",
            letter_spacing="0.4em",
            color=AMBER,
            text_transform="uppercase",
        ),
        rx.heading(
            name,
            font_family="'Cormorant Garamond', serif",
            font_size="2.8rem",
            font_weight="300",
            color=PAPER,
            letter_spacing="0.05em",
            line_height="1.1",
        ),
        rx.text(
            subtitle,
            font_family="'Cormorant Garamond', serif",
            font_size="1rem",
            font_weight="300",
            color=GRAPHITE,
            font_style="italic",
            margin_top="0.25rem",
        ),
        rx.box(height="2rem"),
        rx.text(
            price,
            font_size="1.8rem",
            font_weight="300",
            color=PAPER,
            letter_spacing="0.05em",
            font_family="'Cormorant Garamond', serif",
        ),
        rx.box(height="1.5rem"),
        rx.text(
            "Seleccionar talla",
            font_size="0.65rem",
            letter_spacing="0.25em",
            color=GRAPHITE,
            text_transform="uppercase",
        ),
        rx.hstack(
            *[
                rx.button(
                    s,
                    on_click=PageState.set_size(product_id, s),
                    background=rx.cond(
                        PageState.selected_sizes[product_id] == s,
                        AMBER,
                        "transparent",
                    ),
                    color=rx.cond(
                        PageState.selected_sizes[product_id] == s,
                        INK,
                        GRAPHITE,
                    ),
                    border=rx.cond(
                        PageState.selected_sizes[product_id] == s,
                        f"1px solid {AMBER}",
                        f"1px solid {GRAPHITE}",
                    ),
                    border_radius="0",
                    font_size="0.65rem",
                    letter_spacing="0.1em",
                    padding="0.5rem 0.9rem",
                    cursor="pointer",
                    transition="all 0.2s ease",
                    _hover={"border_color": AMBER, "color": AMBER},
                )
                for s in sizes
            ],
            gap="0.5rem",
            flex_wrap="wrap",
            margin_top="0.5rem",
        ),
        rx.box(height="2rem"),
        rx.button(
            "Anadir al carrito",
            background=AMBER,
            color=INK,
            border_radius="0",
            font_size="0.7rem",
            letter_spacing="0.2em",
            text_transform="uppercase",
            padding="1rem 2.5rem",
            cursor="pointer",
            _hover={"background": GOLD_LIGHT},
            transition="all 0.3s ease",
            width="100%",
        ),
        rx.text(
            "Edicion limitada - Solo 10 unidades",
            font_size="0.65rem",
            color=GRAPHITE,
            letter_spacing="0.1em",
            margin_top="0.75rem",
        ),
        align="start",
        justify="center",
        flex="1",
        padding="4rem",
        background=CARBON,
        min_height="520px",
    )

    children = [image_side, details_side] if not reverse else [details_side, image_side]

    return rx.flex(
        *children,
        direction="row",
        width="100%",
        max_width="1200px",
        margin="0 auto",
    )


# Grid de productos
def grid_cards() -> rx.Component:
    products = [
        {
            "product_id": "01",
            "name": "Abrigo Sombra",
            "subtitle": "Lana merino, corte oversize",
            "price": "RD$ 18,500",
            "image_url": "https://placehold.co/700x900/1a1a1a/C9A96E?text=Pieza+01",
            "reverse": False,
        },
        {
            "product_id": "02",
            "name": "Camisa Velo",
            "subtitle": "Algodon organico, tejido artesanal",
            "price": "RD$ 9,800",
            "image_url": "https://placehold.co/700x900/161616/C9A96E?text=Pieza+02",
            "reverse": True,
        },
        {
            "product_id": "03",
            "name": "Pantalon Silencio",
            "subtitle": "Lino natural, tiro alto",
            "price": "RD$ 12,200",
            "image_url": "https://placehold.co/700x900/1a1a1a/C9A96E?text=Pieza+03",
            "reverse": False,
        },
        {
            "product_id": "04",
            "name": "Blazer Noche",
            "subtitle": "Seda cruda, confeccion a mano",
            "price": "RD$ 24,000",
            "image_url": "https://placehold.co/700x900/111111/C9A96E?text=Pieza+04",
            "reverse": True,
        },
    ]

    return rx.box(
        section_divider("La Coleccion"),
        rx.vstack(
            *[
                rx.box(
                    product_card(**p),
                    padding_y="0.5rem",
                    width="100%",
                )
                for p in products
            ],
            gap="3rem",
            width="100%",
            padding_x="2rem",
            padding_bottom="6rem",
            align="center",
        ),
        width="100%",
        id="coleccion",
    )


# Pagina principal
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
        grid_cards(),
        background=INK,
        min_height="100vh",
        font_family="'DM Sans', sans-serif",
        color=PAPER,
    )


app = rx.App(stylesheets=["styles.css"])