

import sys
import json
from pathlib import Path

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QFont
from QTermWidget import QTermWidget
from PyQt6.QtCore import Qt

CONFIG = Path.home() / ".config/quickterm/config.json"

DEFAULTS = {
    "font": {"family": "DejaVu Sans Mono", "size": 11},
    "color_scheme": "Linux",
    "opacity": 1.0,
    "scrollbar": False
}


def load_config():
    config = DEFAULTS.copy()

    try:
        with CONFIG.open() as file:
            saved = json.load(file)

        for key, value in saved.items():
            if isinstance(value, dict) and isinstance(config.get(key), dict):
                config[key] = {**config[key], **value}
            else:
                config[key] = value
    except FileNotFoundError:
        pass
    except (json.JSONDecodeError, OSError) as error:
        print(f"QuickTerm config error: {error}")

    return config


class QuickTerm(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setAttribute(
            Qt.WidgetAttribute.WA_TranslucentBackground, True
        )

        config = load_config()
        opacity = float(config["opacity"])
        self.setWindowOpacity(opacity)
        self.setWindowTitle("QuickTerm")
        self.resize(900, 550)

        terminal = QTermWidget()
        terminal.addCustomColorSchemeDir(
    str(Path.home() / ".config/quickterm/colors")
)
        terminal.addCustomColorSchemeDir(
            str(Path.home() / ".config/quickterm/colors")
        )
        terminal.setColorScheme(config["color_scheme"])
        terminal.setTerminalOpacity(float(config["opacity"]))
        terminal.setTerminalFont(QFont(
            config["font"]["family"],
            int(config["font"]["size"])
        ))
        terminal.setScrollBarPosition(
            QTermWidget.ScrollBarPosition.NoScrollBar
            if not config["scrollbar"]
            else QTermWidget.ScrollBarPosition.ScrollBarRight
        )
        terminal.setShellProgram("/bin/bash")
        terminal.setArgs([])

        self.setCentralWidget(terminal)
        terminal.startShellProgram()


app = QApplication(sys.argv)
app.setApplicationName("QuickTerm")

window = QuickTerm()
window.show()

sys.exit(app.exec())
