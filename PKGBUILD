# Maintainer: xoraw
pkgname='cmake_example'
_module='cmake_example'
_src_folder='cmake_example'
pkgver='0.0.1'
pkgrel=1
pkgdesc="Add fuction binded from pybinds11 testing"
depends=('python')
makedepends=('python-build' 'python-installer' 'python-wheel' 'cmake' 'python-scikit-build-core')
chechdepends=('python-pytest')
license=('MIT')
arch=('x86_64')
source=("cmake_example.tar.gz")
sha256sums=('SKIP')

build() {
    cd "${srcdir}/${_src_folder}"
    python -m build --wheel --no-isolation
}
check(){
    cd "${srcdir}/${_src_folder}"
    unzip dist/*.whl '*.so' -d tests
    pytest tests/test.py
    rm tests/*.so
}
package() {

    cd "${srcdir}/${_src_folder}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
