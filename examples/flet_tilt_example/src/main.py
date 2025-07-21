import flet as ft
from flet_tilt import (
    FletTilt,
    TiltConfig,
    LightConfig,
    ShadowConfig,
    TiltDirection,
    LightDirection,
    ParallaxConfig,
)


def main(page: ft.Page):
    page.title = "Flet Tilt - All Examples"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    def create_example_card(
        title: str, description: str, tilt_widget: FletTilt
    ) -> ft.Container:
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(title, size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(description, size=14, color=ft.Colors.GREY_700),
                    ft.Container(height=20),
                    tilt_widget,
                    ft.Container(height=30),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=20,
            margin=10,
            border_radius=10,
            bgcolor=ft.Colors.WHITE,
            shadow=ft.BoxShadow(
                spread_radius=1,
                blur_radius=10,
                color=ft.Colors.with_opacity(0.1, ft.Colors.BLACK),
            ),
        )

    # Example 1: Default Tilt - Pikachu
    default_tilt = FletTilt(
        border_radius=30,
        child=ft.Container(
            width=350,
            height=200,
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.bottom_left,
                end=ft.alignment.top_right,
                colors=["#ffeb3b", "#ff9800"],
            ),
            content=ft.Column(
                [
                    ft.Image(
                        src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/25.svg",
                        width=120,
                        height=120,
                    ),
                    ft.Text(
                        "Pikachu ⚡",
                        size=20,
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )

    # Example 2: Tilt Direction - Mewtwo
    tilt_direction = FletTilt(
        border_radius=30,
        tilt_config=TiltConfig(
            angle=20.0,
            direction=[TiltDirection.TOP, TiltDirection.BOTTOM],
        ),
        child=ft.Container(
            width=350,
            height=200,
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["#9c27b0", "#673ab7"],
            ),
            content=ft.Column(
                [
                    ft.Image(
                        src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/150.svg",
                        width=120,
                        height=120,
                    ),
                    ft.Text(
                        "Mewtwo 🧠",
                        size=20,
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )

    # Example 3: Light Direction - Lugia
    light_direction = FletTilt(
        border_radius=30,
        light_config=LightConfig(
            direction=LightDirection.AROUND,
            max_intensity=0.8,
        ),
        child=ft.Container(
            width=350,
            height=200,
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#2196f3", "#0d47a1"],
            ),
            content=ft.Column(
                [
                    ft.Image(
                        src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/249.svg",
                        width=120,
                        height=120,
                    ),
                    ft.Text(
                        "Lugia 🌊",
                        size=20,
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )

    # Example 4: Disable Effects - Gyarados
    disable_effects = FletTilt(
        border_radius=30,
        tilt_config=TiltConfig(disable=False),
        light_config=LightConfig(disable=True),
        shadow_config=ShadowConfig(disable=True),
        child=ft.Container(
            width=350,
            height=200,
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["#2196f3", "#1565c0"],
            ),
            content=ft.Column(
                [
                    ft.Image(
                        src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/130.svg",
                        width=120,
                        height=120,
                    ),
                    ft.Text(
                        "Gyarados 🐉",
                        size=20,
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )

    # Example 5: Initial Tilt - Bulbasaur
    initial_tilt = FletTilt(
        border_radius=30,
        tilt_config=TiltConfig(
            initial={"dx": -1.0, "dy": -1.0},
        ),
        child_layout_outer=[
            ft.Container(
                width=80,
                height=80,
                alignment=ft.alignment.center,
                border_radius=40,
                bgcolor=ft.Colors.with_opacity(0.2, ft.Colors.GREEN),
                content=ft.Text(
                    "#001",
                    size=12,
                    color=ft.Colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                ),
            )
        ],
        child=ft.Container(
            width=350,
            height=200,
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_right,
                end=ft.alignment.bottom_left,
                colors=["#4caf50", "#2e7d32"],
            ),
            content=ft.Column(
                [
                    ft.Image(
                        src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/1.svg",
                        width=120,
                        height=120,
                    ),
                    ft.Text(
                        "Bulbasaur 🌱",
                        size=20,
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )

    # Example 6: Reverse Tilt - Rayquaza
    reverse_tilt = FletTilt(
        border_radius=30,
        tilt_config=TiltConfig(enable_revert=True),
        shadow_config=ShadowConfig(enable_reverse=True),
        child=ft.Container(
            width=350,
            height=200,
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                colors=["#4caf50", "#1b5e20"],
            ),
            content=ft.Column(
                [
                    ft.Image(
                        src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/384.svg",
                        width=120,
                        height=120,
                    ),
                    ft.Text(
                        "Rayquaza 🐲",
                        size=20,
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )
    # Example 7: Layout with Parallax - Charmander Evolution Line
    layout_parallax = FletTilt(
        border_radius=30,
        tilt_config=TiltConfig(
            angle=20.0,
            leave_duration=ft.Duration(milliseconds=700),
            leave_curve=ft.AnimationCurve.FAST_OUT_SLOWIN,
        ),
        shadow_config=ShadowConfig(disable=False),
        child_layout_outer=[
            ft.Container(
                width=80,
                height=80,
                alignment=ft.alignment.center,
                border_radius=40,
                bgcolor=ft.Colors.with_opacity(0.3, ft.Colors.ORANGE),
                content=ft.Text(
                    "Outer",
                    size=12,
                    color=ft.Colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                ),
            ),
        ],
        child_layout_inner=[
            ft.Container(
                width=60,
                height=60,
                alignment=ft.alignment.center,
                border_radius=30,
                bgcolor=ft.Colors.with_opacity(0.4, ft.Colors.RED),
                content=ft.Text(
                    "Inner",
                    size=10,
                    color=ft.Colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                ),
            ),
        ],
        child_layout_behind=[
            # Charizard (behind - furthest)
            ft.Stack(
                [
                    ft.Container(
                        width=350,
                        height=200,
                        border_radius=30,
                        opacity=0.8,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_left,
                            end=ft.alignment.bottom_right,
                            colors=["#ff9800", "#f57c00"],
                        ),
                    ),
                    ft.Container(
                        width=350,
                        height=200,
                        alignment=ft.alignment.center,
                        content=ft.Row(
                            [
                                ft.Column(
                                    [
                                        ft.Image(
                                            src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/6.svg",
                                            width=120,
                                            height=120,
                                        ),
                                        ft.Text(
                                            "Charizard 🔥",
                                            size=20,
                                            color=ft.Colors.WHITE,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ),
                ]
            ),
            # Charmeleon (behind - middle)
            ft.Stack(
                [
                    ft.Container(
                        width=350,
                        height=200,
                        border_radius=30,
                        opacity=0.6,
                        gradient=ft.LinearGradient(
                            begin=ft.alignment.top_left,
                            end=ft.alignment.bottom_right,
                            colors=["#ff7043", "#e64a19"],
                        ),
                    ),
                    ft.Container(
                        width=350,
                        height=200,
                        alignment=ft.alignment.center,
                        content=ft.Row(
                            [
                                ft.Column(
                                    [
                                        ft.Image(
                                            src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/5.svg",
                                            width=110,
                                            height=110,
                                        ),
                                        ft.Text(
                                            "Charmeleon",
                                            size=18,
                                            color=ft.Colors.WHITE,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                    ],
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ),
                ]
            ),
        ],
        child=ft.Stack(
            [
                ft.Container(
                    width=350,
                    height=200,
                    border_radius=30,
                    opacity=0.4,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_left,
                        end=ft.alignment.bottom_right,
                        colors=["#ff5722", "#d84315"],
                    ),
                ),
                ft.Container(
                    width=350,
                    height=200,
                    alignment=ft.alignment.center,
                    content=ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Image(
                                        src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/4.svg",
                                        width=100,
                                        height=100,
                                    ),
                                    ft.Text(
                                        "Charmander",
                                        size=16,
                                        color=ft.Colors.WHITE,
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                ),
            ]
        ),
    )

    # Example 8: Light Shadow Mode - Arceus
    light_shadow_mode = FletTilt(
        border_radius=30,
        tilt_config=TiltConfig(
            leave_curve=ft.AnimationCurve.EASE_IN_OUT_CUBIC_EMPHASIZED,
            leave_duration=ft.Duration(milliseconds=600),
        ),
        light_config=LightConfig(disable=True),
        shadow_config=ShadowConfig(
            max_intensity=0.6,
        ),
        child=ft.Container(
            width=350,
            height=200,
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=["#ffd700", "#ffb300"],
            ),
            content=ft.Column(
                [
                    ft.Image(
                        src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/493.svg",
                        width=120,
                        height=120,
                    ),
                    ft.Text(
                        "Arceus ✨",
                        size=20,
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )

    # Create the main layout
    examples = ft.Column(
        [
            ft.Text(
                "Flet Tilt - Complete Examples",
                size=32,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Container(height=20),
            create_example_card(
                "1. Default Tilt - Pikachu ⚡",
                "Basic tilt effect with the most iconic Pokémon",
                default_tilt,
            ),
            create_example_card(
                "2. Tilt Direction - Mewtwo 🧠",
                "Control tilt direction with the legendary psychic Pokémon",
                tilt_direction,
            ),
            create_example_card(
                "3. Light Direction - Lugia 🌊",
                "Configure light effects with the guardian of the seas",
                light_direction,
            ),
            create_example_card(
                "4. Disable Effects - Gyarados 🐉",
                "Selectively disable effects with the fierce water dragon",
                disable_effects,
            ),
            create_example_card(
                "5. Initial Tilt - Bulbasaur 🌱",
                "Set initial tilt position with the first Pokémon (#001)",
                initial_tilt,
            ),
            create_example_card(
                "6. Reverse Tilt - Rayquaza 🐲",
                "Enable reverse effects with the sky high dragon",
                reverse_tilt,
            ),
            create_example_card(
                "7. Parallax Evolution - Charmander Line 🔥",
                "Complete evolution line with parallax layers (Charmander → Charmeleon → Charizard)",
                layout_parallax,
            ),
            create_example_card(
                "8. Shadow Effects - Arceus ✨",
                "Advanced shadow configuration with the Alpha Pokémon",
                light_shadow_mode,
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(examples)


if __name__ == "__main__":
    ft.app(target=main)
