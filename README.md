# QuickTerm

A lightweight, customizable terminal emulator for Linux, built with Python, PyQt6, and QTermWidget.

## Features

- Custom terminal colour schemes
- Adjustable terminal opacity
- Configurable font family and size
- Optional scrollbar
- JSON-based configuration

## Dependencies

- Python
- PyQt6
- QTermWidget 6

## Running from source

Run QuickTerm with:

```bash
QT_QPA_PLATFORMTHEME=generic python quickterm.py
```

## Configuration

QuickTerm reads its configuration from:

`~/.config/quickterm/config.json`

Example:

```json
{
  "font": {
    "family": "DejaVu Sans Mono",
    "size": 12
  },
  "color_scheme": "QuickTerm",
  "opacity": 0.7,
  "scrollbar": false
}
```

Custom colour schemes can be placed in `~/.config/quickterm/colors/`.

## Status

Early development. Contributions and feedback are welcome.
