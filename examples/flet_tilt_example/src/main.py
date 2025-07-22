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
    page.title = "Flet Tilt - Complete Examples"
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

    # Example 1: Default Tilt
    default_tilt = FletTilt(
        border_radius=30,
        child=ft.Container(
            width=350,
            height=200,
            alignment=ft.alignment.center,
            gradient=ft.LinearGradient(
                begin=ft.alignment.bottom_left,
                end=ft.alignment.top_right,
                colors=["#2196f3", "#1976d2"],
            ),
            content=ft.Column(
                [
                    ft.Icon(
                        ft.Icons.TOUCH_APP,
                        size=80,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Text(
                        "Default Tilt",
                        size=24,
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Text(
                        "Basic tilt functionality",
                        size=14,
                        color=ft.Colors.WHITE70,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )

    # Example 2: Tilt Direction Control
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
                    ft.Icon(
                        ft.Icons.CONTROL_CAMERA,
                        size=80,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Text(
                        "Direction Control",
                        size=24,
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Text(
                        "TOP & BOTTOM only",
                        size=14,
                        color=ft.Colors.WHITE70,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )

    # Example 3: Light Configuration
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
                colors=["#ff9800", "#f57c00"],
            ),
            content=ft.Column(
                [
                    ft.Icon(
                        ft.Icons.LIGHTBULB,
                        size=80,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Text(
                        "Light Effects",
                        size=24,
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Text(
                        "AROUND direction",
                        size=14,
                        color=ft.Colors.WHITE70,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )

    # Example 4: Disable Effects
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
                colors=["#607d8b", "#37474f"],
            ),
            content=ft.Column(
                [
                    ft.Icon(
                        ft.Icons.BLOCK,
                        size=80,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Text(
                        "Disabled Effects",
                        size=24,
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Text(
                        "Light & Shadow OFF",
                        size=14,
                        color=ft.Colors.WHITE70,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )
    # Example 5: Initial Tilt Position
    initial_tilt = FletTilt(
        border_radius=30,
        tilt_config=TiltConfig(
            initial=ft.Offset(-1.6, -1.0),
        ),
        child_layout_outer=[
            ft.Container(
                width=80,
                height=80,
                alignment=ft.alignment.center,
                border_radius=40,
                bgcolor=ft.Colors.with_opacity(0.7, ft.Colors.GREEN),
                content=ft.Text(
                    "OUTER",
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
                    ft.Icon(
                        ft.Icons.SETTINGS_BACKUP_RESTORE,
                        size=80,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Text(
                        "Initial Tilt",
                        size=24,
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Text(
                        ft.Offset(-1.6, -1.0),
                        size=14,
                        color=ft.Colors.WHITE70,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )

    # Example 6: Reverse Tilt
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
                colors=["#66bb6a", "#1b5e20"],
            ),
            content=ft.Column(
                [
                    ft.Icon(
                        ft.Icons.REFRESH,
                        size=80,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Text(
                        "Reverse Tilt",
                        size=24,
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Text(
                        "Enable revert & reverse",
                        size=14,
                        color=ft.Colors.WHITE70,
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        ),
    )

    # Example 7: Parallax Layers
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
            # Layer 3 (behind - furthest)
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
                                        ft.Icon(
                                            ft.Icons.HEXAGON,
                                            size=80,
                                            color=ft.Colors.WHITE,
                                        ),
                                        ft.Text(
                                             "Behind 3",
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
            # Layer 2 (behind - middle)
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
                                        ft.Icon(
                                            ft.Icons.PENTAGON,
                                            size=70,
                                            color=ft.Colors.WHITE,
                                        ),
                                        ft.Text(
                                             "Behind 2",
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
                                    ft.Icon(
                                        ft.Icons.SQUARE,
                                        size=60,
                                        color=ft.Colors.WHITE,
                                    ),
                                    ft.Text(
                                         "Main Child",
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

    # Example 8: Shadow Configuration
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
                    ft.Icon(
                        ft.Icons.SQUARE,
                        size=80,
                        color=ft.Colors.WHITE,
                    ),
                    ft.Text(
                        "Shadow Effects",
                        size=24,
                        color=ft.Colors.WHITE,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Text(
                        "Max intensity: 0.6",
                        size=14,
                        color=ft.Colors.WHITE70,
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
                "1. Default Tilt",
                "Basic tilt functionality with default settings",
                default_tilt,
            ),
            create_example_card(
                "2. Tilt Direction Control",
                "Control tilt direction (TOP & BOTTOM only)",
                tilt_direction,
            ),
            create_example_card(
                "3. Light Configuration",
                "Configure light effects with AROUND direction",
                light_direction,
            ),
            create_example_card(
                "4. Disable Effects",
                "Selectively disable light and shadow effects",
                disable_effects,
            ),
            create_example_card(
                "5. Initial Tilt Position",
                "Set initial tilt position with dx/dy values",
                initial_tilt,
            ),
            create_example_card(
                "6. Reverse Tilt",
                "Enable revert and reverse shadow effects",
                reverse_tilt,
            ),
            create_example_card(
                "7. Parallax Layers",
                "Multiple layers with child_layout_behind configuration",
                layout_parallax,
            ),
            create_example_card(
                "8. Shadow Configuration",
                "Advanced shadow settings with custom intensity",
                light_shadow_mode,
            ),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    page.add(examples)


if __name__ == "__main__":
    ft.app(target=main)
