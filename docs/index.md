# Introduction

FletTilt for Flet.

## Examples

```
import flet as ft

from flet_tilt import FletTilt


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(

                ft.Container(height=150, width=300, alignment = ft.alignment.center, bgcolor=ft.Colors.PURPLE_200, content=FletTilt(
                    tooltip="My new FletTilt Control tooltip",
                    value = "My new FletTilt Flet Control", 
                ),),

    )


ft.app(main)
```

## Classes

[FletTilt](FletTilt.md)


