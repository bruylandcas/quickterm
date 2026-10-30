
pkgname=quickterm
pkgver=0.1.0
pkgrel=1
pkgdesc="A lightweight customizable terminal emulator"
arch=('any')
url="https://github.com/bruylandcas/quickterm"
license=('MIT')
depends=('python' 'python-pyqt6' 'qtermwidget')

source=(
    'quickterm.py'
    'quickterm'
    'LICENSE'
    'QuickTerm.colorscheme'
)
sha256sums=('SKIP' 'SKIP' 'SKIP' 'SKIP')

package() {
    install -Dm755 "$srcdir/quickterm.py" \
        "$pkgdir/usr/share/quickterm/quickterm.py"

    install -Dm755 "$srcdir/quickterm" \
        "$pkgdir/usr/bin/quickterm"

    install -Dm644 "$srcdir/QuickTerm.colorscheme" \
        "$pkgdir/usr/share/quickterm/colors/QuickTerm.colorscheme"

    install -Dm644 "$srcdir/LICENSE" \
        "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

    install -Dm644 /dev/stdin "$pkgdir/usr/share/applications/quickterm.desktop" <<'EOF'
[Desktop Entry]
Name=QuickTerm
Comment=Lightweight terminal emulator
Exec=quickterm
Icon=utilities-terminal
Terminal=false
Type=Application
Categories=System;TerminalEmulator;
StartupNotify=true
EOF
}

