# Maintainer: Saeed Badreldeen <your-email@example.com>
pkgname=hpm
pkgver=1.0.0
pkgrel=1
pkgdesc="Helwan Package Manager - a simple package manager frontend for Arch Linux."
arch=('x86_64')
url="https://github.com/helwan-linux/helwan-pkg-manager"
license=('MIT')
depends=('python-rich' 'python-typer' 'python' 'sudo' 'pacman')
source=("git+https://github.com/helwan-linux/helwan-pkg-manager.git")
md5sums=('SKIP')

build() {
    cd "$srcdir/helwan-pkg-manager"
    # لا build حقيقي لأننا لا نستخدم setup.py
    :
}

package() {
    cd "$srcdir/helwan-pkg-manager"

    mkdir -p "$pkgdir/usr/bin"
    # wrapper script
    cat > "$pkgdir/usr/bin/hpm" <<'EOF'
#!/usr/bin/env bash
PYTHONPATH=/usr/lib/hpm python3 /usr/lib/hpm/main.py "$@"
EOF
    chmod +x "$pkgdir/usr/bin/hpm"

    mkdir -p "$pkgdir/usr/lib/hpm"
    cp -r hpm/* "$pkgdir/usr/lib/hpm/"
    cp -r hpm/assets "$pkgdir/usr/lib/hpm/assets"
}

